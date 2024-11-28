from src.user.client_user import ClientUserServiceConfiguration, DefaultClientUserServiceConfiguration
from .django_repository_configuration import DjangoClientUserRepositoryConfiguration

class DependenciesManager:
    @staticmethod
    def get_client_services() -> ClientUserServiceConfiguration:
        repository_config = DjangoClientUserRepositoryConfiguration()
        services = DefaultClientUserServiceConfiguration(repository_config)
        return services