from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU


# ------------- main_menu клавиатура -------------
# Кнопки для main_menu
button_inst: KeyboardButton = KeyboardButton(text=LEXICON_RU['button_inst'])
button_wb: KeyboardButton = KeyboardButton(text=LEXICON_RU['button_wb'])
comp_services_button: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['comp_services'])
additional_price_button: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['additional_price'])
about_us_button: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['about_us'])
add_questions_button: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['add_questions'])

# инициализируем билдер для клавиатуры main_menu
main_menu_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
# добавляем кнопки в билдер
main_menu_builder.add(button_inst, button_wb, comp_services_button,
                      additional_price_button, about_us_button,
                      add_questions_button)
# выравниваем клавиатуру
main_menu_builder.adjust(2, 2, 2)
# создаем клавиатуру
main_menu_kb = main_menu_builder.as_markup(resize_keyboard=True)
# ------------- main_menu клавиатура -------------


# ------------- comp_services клавиатура -------------
# кнопки для comp_services_menu
comp_services_brandbook_button: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['comp_services_brandbook_button'])
comp_services_logo_button: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['comp_services_logo_button'])
comp_services_style_button: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['comp_services_style_button'])
comp_services_shooting_button: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['comp_services_shooting_button'])
comp_services_shooting_lb_button: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['comp_services_shooting_lb_button'])
back_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['back_button'])

# инициализируем билдер для клавиатуры comp_services_menu
comp_services_menu_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
# добавляем кнопки в билдер
comp_services_menu_builder.row(comp_services_brandbook_button,
                               comp_services_logo_button,
                               comp_services_style_button,
                               comp_services_shooting_button,
                               comp_services_shooting_lb_button,
                               back_button, width=2)
# создаем клавиатуру
comp_services_kb = comp_services_menu_builder.as_markup(resize_keyboard=True)

# ------------- comp_services клавиатура -------------


# ------------- wildberries клавиатура -------------

wildberries_infographics_button: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['wildberries_infographics_button'])
wildberries_copywriting_button: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['wildberries_copywriting_button'])
wildberries_comp_services_shooting_button: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['wildberries_comp_services_shooting_button'])
back_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['back_button'])

wildberries_menu_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

wildberries_menu_builder.row(wildberries_infographics_button,
                             wildberries_copywriting_button,
                             wildberries_comp_services_shooting_button,
                             back_button, width=2)

wildberries_menu_kb = wildberries_menu_builder.as_markup(resize_keyboard=True)

# ------------- wildberries клавиатура -------------


# ------------- inst клавиатура -------------
inst_full_maintenance_button: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['inst_full_maintenance_button'])
inst_content_shooting_button: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['inst_content_shooting_button'])
inst_visual_button: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['inst_visual_button'])
inst_reels_button: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['inst_reels_button'])
inst_graphics_button: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['inst_graphics_button'])

inst_menu_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

inst_menu_kb_builder.row(inst_full_maintenance_button,
                         inst_content_shooting_button,
                         inst_visual_button, inst_reels_button,
                         inst_graphics_button, back_button, width=2)

inst_menu_kb = inst_menu_kb_builder.as_markup(resize_keyboard=True)

# ------------- inst клавиатура -------------
