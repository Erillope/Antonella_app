from src.user.client_user.data_providers import ClientUserRepositoryConfiguration
from src.user.account.data_providers import UserAccountRepository
from ..repository.django_client_user_repository import DjangoClientUserRepository
from singleton_decorator import singleton

@singleton
class DjangoClientUserRepositoryConfiguration(ClientUserRepositoryConfiguration):
    def construct_user_repository(self) -> UserAccountRepository:
        return DjangoClientUserRepository()