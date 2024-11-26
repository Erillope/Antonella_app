from src.user.client_user.data_providers import ClientUserRepositoryConfiguration, ClientUserRepository
from ..repository.django_client_user_repository import DjangoClientUserRepository
from singleton_decorator import singleton

@singleton
class DjangoClientUserRepositoryConfiguration(ClientUserRepositoryConfiguration):
    def construct_user_repository(self) -> ClientUserRepository:
        return DjangoClientUserRepository()