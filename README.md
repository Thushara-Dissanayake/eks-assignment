# eks-assignment

Create a new [Python-based CDK project](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html) and create the following resources:
- Create a simple [EKS cluster](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_eks-readme.html).
- Create a [SSM parameter](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ssm-readme.html) with the name `/platform/account/env` and the value `development`, `staging` or `production`.
- Install the [ingress-nginx](https://artifacthub.io/packages/helm/ingress-nginx/ingress-nginx) [Helm Chart](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_eks.HelmChart.html) into the previously created EKS cluster. Get the values to be used in the Helm chart from a CustomResource attribute (see next step). The Helm chart doesn't need to be integrated with the rest of the EKS cluster.
- Create a Lambda backed [CustomResource](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.CustomResource.html). Write a Lambda function in Python that retrieves the account environment value from the previously created SSM parameter via `boto3`. Generate Helm values that can be referenced from a CustomResource attribute. If the environment is `development` than the Helm chart value `controller.replicaCount` should be set to `1`. If the environment is `staging` or `production` than `controller.replicaCount` should be set to `2`.
- Write unit tests using `pytest` but only for the Python code used in the Lambda function. Test the returned Helm values based on the different account environments.

There are no hidden objectives or obstacles. Feel free to create other resources as required to complete the tasks. Once completed, please share your Git repository with us, either by hosting it somewhere or by emailing an archive as attachment the day before.

We cannot provide AWS accounts. You will need to use your own AWS account.
