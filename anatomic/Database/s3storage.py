from abc import ABC, abstractmethod


class S3Storage(ABC):
    @abstractmethod
    def get(self, file_path, bucket_name, object_name):
        pass


class S3BackBlaze(S3Storage):
    def get(self, file_path, bucket_name, object_name):
        pass