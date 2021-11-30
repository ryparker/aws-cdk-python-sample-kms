from aws_cdk import (
    Stack,
    aws_kms as kms,
    aws_s3 as s3,
    aws_sqs as sqs,
    aws_s3_notifications as s3notif
)
from constructs import Construct

class AwsCdkPythonSampleKmsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        kms_key = kms.Key(self, 'ssl_s3_sqs_kms_key',
            alias='sslS3SqsKmsKey',
            description='This is kms key',
            enabled=True,
            enable_key_rotation=True,
            policy=kms_policy_document,
        )

        # Create the S3 bucket
        bucket = s3.Bucket(
            self, "ssl_s3_bucket_raw_kms",
            bucket_name="ssl-s3-bucket-kms-raw",
            encryption=s3.BucketEncryption.KMS,
            encryption_key=kms_key,
        )

        # Create the SQS queue
        queue = sqs.Queue(
            self, "ssl_sqs_event_queue",
            queue_name="ssl-sqs-kms-event-queue",
            encryption=sqs.QueueEncryption.KMS,
            encryption_master_key=kms_key,
        )

        # Create S3 notification object which points to SQS
        notification = s3notif.SqsDestination(queue)
        filter1 = s3.NotificationKeyFilter(prefix="home/")

        # Attach notificaton event to S3 bucket
        bucket.add_event_notification(s3.EventType.OBJECT_CREATED,notification,filter1)
