from aiogram import Router
from aiogram.types import Message


router: Router = Router()


@router.message()
async def send_answer(message: Message): ...
