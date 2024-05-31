from aiogram import Router

from .start import router as start_router
from .help import router as help_router


router = Router()
router.include_router(start_router)
router.include_router(help_router)
