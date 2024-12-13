from .service_repository_exception import ServiceRepositoryException

class ServiceNotFoundException(ServiceRepositoryException):
    @classmethod
    def not_found(cls, service: str) -> "ServiceNotFoundException":
        return cls(f"No se encontró el servicio '{service}'")