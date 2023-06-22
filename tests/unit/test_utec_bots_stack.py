import aws_cdk as core
import aws_cdk.assertions as assertions

from utec_bots.utec_bots_stack import UtecBotsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in utec_bots/utec_bots_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = UtecBotsStack(app, "utec-bots")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
