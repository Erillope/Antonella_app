from src.user.employee_user import EmployeeUserServiceConfiguration, DefaultEmployeeUserServiceConfiguration
from app.user.account.django_exists_user import DjangoExistsUser
from .django_repository_configuration import DjangoEmployeeUserRepositoryConfiguration

class DependenciesManager:
    @staticmethod
    def get_employee_services() -> EmployeeUserServiceConfiguration:
        repository_config = DjangoEmployeeUserRepositoryConfiguration()
        global_exists_user = DjangoExistsUser()
        services = DefaultEmployeeUserServiceConfiguration(global_exists_user, repository_config)
        return services
    