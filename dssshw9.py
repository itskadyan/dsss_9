from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from groq import Groq

def groqmsg(content):

    client = Groq(api_key="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")

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! I am Gaurav's bot. How can I assist you today?")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    bot_response = groqmsg(user_message)
    await update.message.reply_text(bot_response)


def main():
    application = Application.builder().token("7908001473:AAFL5FOyXIFuO4fJ8cpkx3Dr4e4mDznQAVY").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == "__main__":
    main()