from aws_cdk import (
    aws_ec2 as ec2,
)
from constructs import Construct

class VpcConstruct(Construct):
    def __init__(self, scope: Construct, construct_id: str, vpc_cidr: str, az, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, 'Vpc',
            ip_addresses=ec2.IpAddresses.cidr(vpc_cidr),
            enable_dns_hostnames=True,
            enable_dns_support=True,
            availability_zones=az,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name=f'eks-subnet-public',
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    name=f'eks-subnet-private',
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask=24
                )
            ]
        )
        
        self.vpc = vpc