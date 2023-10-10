import boto3

# Create Lambda Client
lambda_client = boto3.client('lambda')

# Create Lambda Function
lambda_function = lambda_client.create_function(
    FunctionName='automated_backup',
    Runtime='python3.9',
    Role='arn:aws:iam::123456789012:role/lambda_role',
    Handler='automated_backup.handler',
    Code={
        'ZipFile': open('automated_backup.zip', 'rb').read()
    },
    Description='Automated Backup Function',
    Timeout=300,
    MemorySize=512
)

# Create Event Source
lambda_client.create_event_source_mapping(
    EventSourceArn='arn:aws:s3:::my_bucket',
    FunctionName='automated_backup',
    Enabled=True
)