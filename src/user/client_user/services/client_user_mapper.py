from src.user.account.services.user_account_mapper import UserAccountMapper
from ..domain import ClientUser, ClientUserFactory
from .dto import ClientUserDto, ClientUserSignUpDto
from singleton_decorator import singleton

@singleton
class ClientUserMapper(UserAccountMapper):
    def to_user(self, dto: ClientUserSignUpDto) -> ClientUser:
        return ClientUserFactory.create_default(
            account = dto.get_account(),
            name = dto.get_name(),
            password = dto.get_password(),
            birthdate = dto.get_birthdate()
        )
    
    def to_dto(self, user: ClientUser) -> ClientUserDto:
        return ClientUserDto(
            id = user.get_id(),
            account = user.get_account(),
            name = user.get_name(),
            birthdate = user.get_birthdate(),
            status = user.get_status(),
            joined_date = user.get_joined_date()
        )