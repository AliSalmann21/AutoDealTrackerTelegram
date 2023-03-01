import os
import logging
import threading
from telegram import Bot
from telegram.ext import Updater, CommandHandler

from utils import setup_logger
from url_tracker import track_url
from commands import start, track


# Use environment variables to store sensitive information
BOT_TOKEN = os.environ.get('BOT_TOKEN')


def main():
    # Create a logger
    logger = logging.getLogger('url_tracker')
    setup_logger(logger)

    # Create a Telegram bot object
    bot = Bot(token=BOT_TOKEN)

    # Create an updater object
    updater = Updater(token=BOT_TOKEN, use_context=True)

    # Get the dispatcher object
    dispatcher = updater.dispatcher

    # Register the /start command handler
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Register the /track command handler
    track_handler = CommandHandler('track', track, pass_args=True, pass_job_queue=True)
    dispatcher.add_handler(track_handler)

    # Start the bot
    updater.start_polling()

    # Get the URLs
    updater.idle()


if __name__ == '__main__':
    main()
