from .auth import ISingIn, IRegisterEmployee
from .account_data import (IChangeAccountData, IDisableEmployeeUserAccount, IEnableEmployeeUserAccount,
                            IGiveRole, ITakeRole)
from .role import IAddRole, IRemoveRole
from .configuration import EmployeeUserServiceConfiguration, DefaultEmployeeUserServiceConfiguration