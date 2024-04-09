from aws_cdk import (
    aws_ssm as ssm,
)
from constructs import Construct

class ParameterStoreConstruct(Construct):
    def __init__(self, scope: Construct, construct_id: str, parameter_name: str, string_value: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        parameter = ssm.StringParameter(self, "Parameter",
            string_value=string_value,
            parameter_name=parameter_name
        )
        
        self.parameter = parameter