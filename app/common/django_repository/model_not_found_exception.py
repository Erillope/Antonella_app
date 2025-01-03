from ..django_exception import DjangoException

class ModelNotFoundException(DjangoException):
    @classmethod
    def not_found(cls, model: str) -> "ModelNotFoundException":
        return cls(f"{model} no se encuentra registrado")