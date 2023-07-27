import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from nftgo_gpt import agent
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    question = update.message.text
    answer = agent.run(question)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=answer)

if __name__ == '__main__':
    application = ApplicationBuilder().token('6028853790:AAE3bvYLC-Ad87vISOXkBcR2-QcSmwpqUD4').build()

    # start_handler = CommandHandler('ask', start)
    # application.add_handler(start_handler)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # 运行bot，直到Ctrl+C终止程序
    application.run_polling()