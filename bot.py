import logging
import joblib
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Load the trained model and vectorizer
MODEL_PATH = "models/toxic_model.pkl"
VECTORIZER_PATH = "models/vectorizer.pkl"

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Define the Telegram bot token
TOKEN = "7762922596:AAHZDIcMWLLlBVFMaEpxp838RmbertdYUUg"

# Function to classify message as toxic or non-toxic
def is_toxic(message):
    transformed_text = vectorizer.transform([message])
    prediction = model.predict(transformed_text)
    return prediction[0] == 1  # Returns True if toxic

# Start command
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Hello! I am a moderation bot. I will remove toxic messages automatically in this chat."
    )

# Message handler for checking toxicity
async def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    user = update.message.from_user

    logger.info(f"Message from {user.first_name}: {text}")

    if is_toxic(text):
        try:
            await update.message.delete()  # Delete toxic message
            logger.info("Toxic message deleted.")
        except Exception as e:
            logger.error(f"Error deleting message: {e}")

# Main function to start bot
def main():
    app = Application.builder().token(TOKEN).build()

    # Command handler
    app.add_handler(CommandHandler("start", start))

    # Message handler for **private chats and groups**
    app.add_handler(MessageHandler(filters.TEXT & (filters.ChatType.PRIVATE | filters.ChatType.GROUPS), handle_message))

    # Run the bot
    logger.info("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
