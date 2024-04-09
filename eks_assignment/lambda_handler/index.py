import boto3

def handler(event, context):
    ssm_value = get_ssm_parameters()

    if ssm_value == "development":
        replica_count = 1
    elif (ssm_value == "staging") or (ssm_value == "production"):
        replica_count = 2

    return {
        "Data": {
            "ReplicaCount": replica_count,
        }
    }

# Retrieve value from SSM parameter Store
def get_ssm_parameters():
    ssm_parameter_name = "/platform/account/env"
    ssm_client = boto3.client("ssm")
    
    try:
        response = ssm_client.get_parameter(
            Name=ssm_parameter_name,
            WithDecryption=False
        )
        return response["Parameter"]["Value"]
    except Exception as e:
        return {
            "statusCode": 400,
            "body": "Error retrieving SSM parameter: " + str(e),
        }