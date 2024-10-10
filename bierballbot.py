from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
import os, random
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

fail_texts=["Du scheiß Idioot! Voll daneben geworfen!"]
success_texts=["Starker Wurf! Flasche getroffen!"]

# Define the /start command handler function
async def wurf(update: Update, context) -> None:
    if random.randint(1,100) >= 10:
        await update.message.reply_text(random.choice(fail_texts))
    else:
        await update.message.reply_text(random.choice(success_texts))


# Main function to set up the bot
if __name__ == '__main__':
    # Replace 'YOUR_BOT_TOKEN' with the token you received from BotFather
    bot_token = os.getenv('BOT_TOKEN')
    
    # Create the bot application
    app = ApplicationBuilder().token(bot_token).build()
    
    # Add a command handler for the /start command
    app.add_handler(CommandHandler('wurf', wurf))
    
    # Start the bot
    app.run_polling()

