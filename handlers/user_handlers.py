from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Text
from keyboards.keyboards import (main_menu_kb, comp_services_kb,
                                 wildberries_menu_kb, inst_menu_kb)
from lexicon.lexicon_ru import LEXICON_RU


# инициализируем роутер
router: Router = Router()


# хэндлер для "/start"
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'].format(
        message.from_user.full_name), reply_markup=main_menu_kb)


# хэндлер для "Вопросы"
@router.message(Text(text=LEXICON_RU['add_questions']))
async def process_add_questions_answer(message: Message):
    await message.answer(text=LEXICON_RU['add_questions_answer'],
                         reply_markup=main_menu_kb)


# хэндлер для "О нас"
@router.message(Text(text=LEXICON_RU['about_us']))
async def process_about_us_answer(message: Message):
    await message.answer(text=LEXICON_RU['about_us_answer'],
                         reply_markup=main_menu_kb)


# хэндлер для "Дополнительный прайс"
@router.message(Text(text=LEXICON_RU['additional_price']))
async def process_add_price_answer(message: Message):
    await message.answer(text=LEXICON_RU['additional_price_answer'],
                         reply_markup=main_menu_kb)


# хэндлер для "Дополнительные услуги"
@router.message(Text(text=LEXICON_RU['comp_services']))
async def process_comp_services_answer(message: Message):
    await message.answer(text=LEXICON_RU['comp_services_info'],
                         reply_markup=comp_services_kb)


# хэндлер для "Назад"
@router.message(Text(text=LEXICON_RU['back_button']))
async def process_back_answer(message: Message):
    await message.answer(text=LEXICON_RU['back_button_answer'],
                         reply_markup=main_menu_kb)


# хэндлер для "Брендбук"
@router.message(Text(text=LEXICON_RU['comp_services_brandbook_button']))
async def process_comp_services_brandbook_button_answer(message: Message):
    await message.answer(text=LEXICON_RU['comp_services_brandbook_answer'])


# хэндлер для "Логотип"
@router.message(Text(text=LEXICON_RU['comp_services_logo_button']))
async def process_comp_services_logo_button_answer(message: Message):
    await message.answer(text=LEXICON_RU['comp_services_logo_answer'])


# хэндлер для "Стилизация образа"
@router.message(Text(text=LEXICON_RU['comp_services_style_button']))
async def process_comp_services_style_answer(message: Message):
    await message.answer(text=LEXICON_RU['comp_services_style_answer'])


# хэндлер для "Съемка"
@router.message(Text(text=LEXICON_RU['comp_services_shooting_button']))
async def process_comp_services_shooting_button_answer(message: Message):
    await message.answer(text=LEXICON_RU['comp_services_shooting_answer'])


# хэндлер для "Съемка лукбука"
@router.message(Text(text=LEXICON_RU['comp_services_shooting_lb_button']))
async def process_comp_services_shooting_lb_button_answer(message: Message):
    await message.answer(text=LEXICON_RU['comp_services_shooting_lb_answer'])


# хэндлер для "Вайлдберрис"
@router.message(Text(text=LEXICON_RU['button_wb']))
async def process_button_wb_answer(message: Message):
    await message.answer(text=LEXICON_RU['button_wb_info'],
                         reply_markup=wildberries_menu_kb)


# хэндлер для "Инфографика"
@router.message(Text(text=LEXICON_RU['wildberries_infographics_button']))
async def process_wildberries_infographics_button_answer(message: Message):
    await message.answer(text=LEXICON_RU['wildberries_infographics_answer'])


# хэндлер для "Копирайтинг"
@router.message(Text(text=LEXICON_RU['wildberries_copywriting_button']))
async def process_wildberries_copywriting_button_answer(message: Message):
    await message.answer(text=LEXICON_RU['wildberries_copywriting_answer'])


# хэндлер для "Инстаграм"
@router.message(Text(text=LEXICON_RU['button_inst']))
async def process_button_inst_answer(message: Message):
    await message.answer(text=LEXICON_RU['button_inst_info'],
                         reply_markup=inst_menu_kb)


# хэндлер для "Полное ведение"
@router.message(Text(text=LEXICON_RU['inst_full_maintenance_button']))
async def process_inst_full_maintenance_button_answer(message: Message):
    await message.answer(text=LEXICON_RU['inst_full_maintenance_answer'])


# хэндлер для "Контент-съемка"
@router.message(Text(text=LEXICON_RU['inst_content_shooting_button']))
async def process_inst_content_shooting_button_answer(message: Message):
    await message.answer(text=LEXICON_RU['inst_content_shooting_answer'])


# хэндлер для "Визуал"
@router.message(Text(text=LEXICON_RU['inst_visual_button']))
async def process_inst_visual_button_anwer(message: Message):
    await message.answer(text=LEXICON_RU['inst_visual_answer'])


# хэндлер для "Reels"
@router.message(Text(text=LEXICON_RU['inst_reels_button']))
async def process_inst_reels_button_answer(message: Message):
    await message.answer(text=LEXICON_RU['inst_reels_answer_one'])
    await message.answer(text=LEXICON_RU['inst_reels_answer_more'])


# хэндлер для "Графика"
@router.message(Text(text=LEXICON_RU['inst_graphics_button']))
async def process_inst_graphics_button_answer(message: Message):
    await message.answer(text=LEXICON_RU['inst_graphics_answer'])
