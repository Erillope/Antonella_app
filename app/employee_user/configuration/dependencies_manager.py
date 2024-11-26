from src.user.employee_user import EmployeeUserServiceConfiguration, DefaultEmployeeUserServiceConfiguration
from .django_repository_configuration import DjangoEmployeeUserRepositoryConfiguration

class DependenciesManager:
    @staticmethod
    def get_employee_services() -> EmployeeUserServiceConfiguration:
        repository_config = DjangoEmployeeUserRepositoryConfiguration()
        services = DefaultEmployeeUserServiceConfiguration(repository_config)
        return services
    