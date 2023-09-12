from aiogram import types,Dispatcher
from config import bot
from const import START_TEXT
from database.sql_commands import Database
from keybords.inline_buttons import question_first_keyboard


async def start_quesrionnaire_call(call:types.CallbackQuery):
    print(call)
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Male or Female",
        reply_markup=await question_first_keyboard()
    )
async def male_answer_call(call:types.CallbackQuery):
    print(call)
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Yes you are male"

    )

async def female_answer_call(call:types.CallbackQuery):
    print(call)
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Yes you are female"

    )



def register_callback_handlers(dp:Dispatcher):
    dp.register_callback_query_handler(start_quesrionnaire_call,
                                       lambda call:call.data== "start_questionnaire")
    dp.register_callback_query_handler(male_answer_call,
                                       lambda call:call.data== "male_answer")
    dp.register_callback_query_handler(female_answer_call,
                                       lambda call:call.data== "female_answer")