from app.router import Router
from .controllers import AccountDataController, AuthController, RoleController

router = Router()
router.add(AccountDataController())
router.add(AuthController())
router.add(RoleController())

urlpatterns = router.get_routes()