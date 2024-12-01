from src.user.account import UserServiceConfiguration
from src.user.client_user import DefaultClientUserServiceConfiguration
from app.user.account.django_exists_user import DjangoExistsUser
from .django_repository_configuration import DjangoClientUserRepositoryConfiguration


class DependenciesManager:
    @staticmethod
    def get_client_services() -> UserServiceConfiguration:
        repository_config = DjangoClientUserRepositoryConfiguration()
        global_exists_user = DjangoExistsUser()
        services = DefaultClientUserServiceConfiguration(global_exists_user, repository_config)
        return services