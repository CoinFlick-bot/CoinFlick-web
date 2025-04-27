from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

WEBAPP_URL = "https://coinflick-webapp-ebgk.vercel.app"  

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚀 Launch CoinFlick", web_app=WebAppInfo(url=WEBAPP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome to CoinFlick 👋\nTap the button below to launch the game!",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token("7532590160:AAGre9QQ54yAM3VpdueELMTdxwxPJBQns-4").build()
app.add_handler(CommandHandler("start", start))

print("🤖 CoinFlick bot is running...")
app.run_polling()
