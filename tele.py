from telegram import *
from telegram.ext import *

bot = Bot("")
#print(bot.get_me())
updater = Updater("", use_context=True)

dispatcher= updater.dispatcher


def test_func(update:Update, context:CallbackContext):
    bot.send_message(
        chat_id = update.effective_chat.id,
        text ="tutorial link : https://m.me/112053085065108?ref=hotro",
    )
start_value = CommandHandler('motion_detection',test_func)

dispatcher.add_handler(start_value)

updater.start_polling()
