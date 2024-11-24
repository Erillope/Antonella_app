from src.user.client_user.data_providers import ClientUserRepositoryConfiguration, ClientUserRepository
from src.common import override
from ..repository.django_client_user_repository import DjangoClientUserRepository
from singleton_decorator import singleton

@singleton
class DjangoClientUserRepositoryConfiguration(ClientUserRepositoryConfiguration):
    @override
    def construct_user_repository(self) -> ClientUserRepository:
        return DjangoClientUserRepository()