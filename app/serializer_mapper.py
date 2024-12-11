from abc import ABC, abstractmethod
from rest_framework.serializers import Serializer

class SerializerMapper(ABC):
    @abstractmethod
    def to_serializer(self, dto) -> Serializer: ...