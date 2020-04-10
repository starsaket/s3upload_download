import boto3


def upload_file(file_name, bucket):
    """
    Function to upload a file to an S3 bucket
    """
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)

    return response


def download_file(file_name, bucket):
    """
    Function to download a given file from an S3 bucket
    """
    s3 = boto3.resource('s3')
    output = f"downloads/{file_name}"
    s3.Bucket(bucket).download_file(file_name, output)

    return output


def list_files(BUCKET):
    """
    Function to list files in a given S3 bucket
    """
    import boto3
    contents = []
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket(BUCKET)
    try:
        for file in my_bucket.objects.all():
            print(file.key)
            contents.append(file)
    except Exception as e:
        pass
    return contents