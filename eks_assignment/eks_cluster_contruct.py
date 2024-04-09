from aws_cdk import (
    aws_ec2 as ec2,
    aws_eks as eks
)
from constructs import Construct

class EksClusterConstruct(Construct):
    def __init__(self, scope: Construct, construct_id: str, vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cluster = eks.Cluster(
            self, 'EKS-Cluster',
            version=eks.KubernetesVersion.V1_29,
            vpc=vpc,
            default_capacity=0
        )

        # Create the EC2 node group
        nodegroup = cluster.add_nodegroup_capacity(
            'Nodegroup',
            instance_types=[ec2.InstanceType('t3.medium')],
            desired_size=1,
            min_size=1,
            max_size=3,
            ami_type=eks.NodegroupAmiType.AL2_X86_64
        )

        self.cluster = cluster
        self.nodegroup = nodegroup