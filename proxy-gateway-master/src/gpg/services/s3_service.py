import os

import boto3
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.utils import timezone


class S3UploadService:
    def __init__(self, file):
        self.session = boto3.session.Session()

        self.client = self.session.client(
            service_name='s3',
            endpoint_url='https://hb.bizmrg.com',
            aws_access_key_id=settings.S3_ACCESS_KEY,
            aws_secret_access_key=settings.S3_SECRET_KEY
        )
        self.file = file['file']

    def __call__(self):
        current_time = timezone.now()
        dir = os.path.join(settings.BASE_DIR, 'files')

        file_name_unique = str(current_time.timestamp()).replace('.', '')
        key = f'{settings.S3_KEY}-{file_name_unique}-{self.file.name}'
        file_path = default_storage.save(f'{dir}/{key}', ContentFile(self.file.read()))

        self.client.upload_file(Filename=file_path, Bucket=settings.S3_BUCKET, Key=key)
        default_storage.delete(file_path)
        return f'{settings.S3_HOST}/{settings.S3_BUCKET}/{key}'

