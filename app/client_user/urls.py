from app.router import Router
from .controllers import AccountDataController, AuthController

router = Router()
router.add(AccountDataController())
router.add(AuthController())

urlpatterns = router.get_routes()