from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


# Needed for Amazon S3 Integration
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
