from src.user.domain import UserAccount, UserAccountFactory, Role
from ..dto import UserAccountDto, SignUpDto
from typing import List

class UserAccountMapper:
    def __init__(self) -> None:
        self.__factory = UserAccountFactory()
        
    def to_user(self, dto: SignUpDto) -> UserAccount:
        return self.__factory.create(
            account = dto.get_account(),
            name = dto.get_name(),
            password = dto.get_password(),
            birthdate = dto.get_birthdate()
        )
    
    def to_dto(self, user: UserAccount, roles: List[Role]) -> UserAccountDto:
        return UserAccountDto(
            id = user.get_id(),
            account = user.get_account(),
            name = user.get_name(),
            status = user.get_status(),
            birthdate = user.get_birthdate(),
            roles = [role.get_value() for role in roles],
            created_date = user.get_created_date()
        )