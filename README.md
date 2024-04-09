
# eks-assignment

Create a new [Python-based CDK project](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html) and create the following resources:

- Create a simple [EKS cluster](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_eks-readme.html).

- Create a [SSM parameter](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ssm-readme.html) with the name `/platform/account/env` and the value `development`, `staging` or `production`.

- Install the [ingress-nginx](https://artifacthub.io/packages/helm/ingress-nginx/ingress-nginx) [Helm Chart](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_eks.HelmChart.html) into the previously created EKS cluster. Get the values to be used in the Helm chart from a CustomResource attribute (see next step). The Helm chart doesn't need to be integrated with the rest of the EKS cluster.

- Create a Lambda backed [CustomResource](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.CustomResource.html). Write a Lambda function in Python that retrieves the account environment value from the previously created SSM parameter via `boto3`. Generate Helm values that can be referenced from a CustomResource attribute. If the environment is `development` than the Helm chart value `controller.replicaCount` should be set to `1`. If the environment is `staging` or `production` than `controller.replicaCount` should be set to `2`.

- Write unit tests using `pytest` but only for the Python code used in the Lambda function. Test the returned Helm values based on the different account environments.

There are no hidden objectives or obstacles. Feel free to create other resources as required to complete the tasks. Once completed, please share your Git repository with us, either by hosting it somewhere or by emailing an archive as attachment the day before.

We cannot provide AWS accounts. You will need to use your own AWS account.

# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
