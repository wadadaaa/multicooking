# -*- coding: utf-8 -*-
# Copyright (c) Eugene MechanisM 2015.
from django.conf import settings
from django.core.files.storage import get_storage_class
from storages.backends.s3boto import S3BotoStorage


class Static(S3BotoStorage):
    location = settings.STATIC_S3
    print(location)


class Media(S3BotoStorage):
    location = settings.MEDIA_S3
    print(location)

class CachedS3BotoStorage(S3BotoStorage):
    """
    S3 storage backend that saves the files locally, too.
    """

    def __init__(self, *args, **kwargs):
        super(CachedS3BotoStorage, self).__init__(*args, **kwargs)
        self.local_storage = get_storage_class(
            "compressor.storage.CompressorFileStorage")()
        print(self)

    def save(self, name, content):
        print(self)
        name = super(CachedS3BotoStorage, self).save(name, content)
        self.local_storage._save(name, content)
        return name