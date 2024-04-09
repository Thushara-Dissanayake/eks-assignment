from aws_cdk import (
    CfnOutput,
    Stack,
    aws_eks as eks, 
    aws_lambda as _lambda,
    aws_iam as iam,
    custom_resources as cr,
    CustomResource,
)
from datetime import datetime
from constructs import Construct
from .parameterstore_contruct import ParameterStoreConstruct
from .vpc_construct import VpcConstruct
from .eks_cluster_contruct import EksClusterConstruct

class EksAssignmentStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        availability_zones = ['eu-central-1a', 'eu-central-1b']

        # Create a new VPC
        vpc = VpcConstruct(self, "Vpc",
            vpc_cidr="192.168.0.0/16",
            az=availability_zones,
        ).vpc
        
        #Create EKS cluster
        cluster = EksClusterConstruct (self, "EKS-Cluster",
            vpc=vpc
        ).cluster

        cluster.node.add_dependency(vpc)

        # Store env parameter in SSM ParameterStore
        ParameterStoreConstruct (self, "MySSMParam", 
            parameter_name='/platform/account/env', 
            # string_value='development'
            string_value='staging'
            # string_value='production'
        )

        # Lambda function to return Helm values based on env value in SSM
        my_lambda = _lambda.Function(
            self,
            "MyLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="index.handler",
            code=_lambda.Code.from_asset("eks_assignment/lambda_handler"),
        )
        
        my_lambda.add_to_role_policy(
            iam.PolicyStatement(
                actions=["ssm:GetParameter"],
                resources=["arn:aws:ssm:*:*:parameter/platform/account/env"],
            )
        )

        # Lambda backed CustomResource to return Helm values
        cr_provider = cr.Provider(self, "LambdaCustomResourceProvider",
            on_event_handler=my_lambda
        )
        lambda_cr = CustomResource (self, "LambdaCustomResource", 
            service_token=cr_provider.service_token,
            properties={
                "timestamp": datetime.now().strftime("%H%M%S")
            }
        )

        lambda_cr.node.add_dependency(my_lambda)

        # CfnOutput(self, "Rsp2", value=lambda_cr.get_att_string('ReplicaCount'))

        helm_values = {
            'controller': {
                'replicaCount': lambda_cr.get_att_string('ReplicaCount'),
            }
        }
        # Deploy ingress-nginx the Helm chart
        helm_chart = eks.HelmChart(
            self, 'x',
            cluster=cluster,
            chart="ingress-nginx",
            repository="https://kubernetes.github.io/ingress-nginx",
            values=helm_values,
            namespace='default'
        )

        helm_chart.node.add_dependency(cluster)