import json
import boto3


def lambda_handler(event, context):
    file_name = event['Records'][0]['s3']['object']['key']
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    print("File name is :", file_name)
    print("Bucket name is :", bucket_name)

    glue = boto3.client('glue')
    response = glue.start_job_run(JobName='s3_lambda_trigger_glue_redshift_auto',
                                  Arguments={"--VAL1": file_name, "--VAL2": bucket_name})
    print("Lambda invoked")