from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Define the /start command handler function
async def start(update: Update, context) -> None:
    await update.message.reply_text("Hello World")

# Main function to set up the bot
if __name__ == '__main__':
    # Replace 'YOUR_BOT_TOKEN' with the token you received from BotFather
    bot_token = os.getenv('BOT_TOKEN')
    
    # Create the bot application
    app = ApplicationBuilder().token(bot_token).build()
    
    # Add a command handler for the /start command
    app.add_handler(CommandHandler('start', start))
    
    # Start the bot
    app.run_polling()

