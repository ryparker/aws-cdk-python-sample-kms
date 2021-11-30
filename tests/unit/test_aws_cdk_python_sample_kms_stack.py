import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_cdk_python_sample_kms.aws_cdk_python_sample_kms_stack import AwsCdkPythonSampleKmsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cdk_python_sample_kms/aws_cdk_python_sample_kms_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCdkPythonSampleKmsStack(app, "aws-cdk-python-sample-kms")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
