from src.user import (UserAccountServiceConfiguration, RoleServiceConfiguration,
                      DefaultUserAccountServiceConfiguration, DefaultRoleServiceConfiguration)
from .django_user_repository_configuration import DjangoUserRepositoryConfiguration
from .django_role_repository_configuration import DjangoRoleRepositoryConfiguration


class DependenciesManager:
    @classmethod
    def get_user_services(cls) -> UserAccountServiceConfiguration:
        return DefaultUserAccountServiceConfiguration(
            user_repository_configuration = DjangoUserRepositoryConfiguration(),
            role_service_configuration = cls.get_role_services()
        )
    
    @staticmethod
    def get_role_services() -> RoleServiceConfiguration:
        return DefaultRoleServiceConfiguration(
            role_repository_configuration = DjangoRoleRepositoryConfiguration()
        )