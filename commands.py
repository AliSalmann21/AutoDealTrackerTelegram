from telegram import Update, Bot
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a deal tracker bot! Use /track <item_url> to start tracking a deal.")


def track(update: Update, context: CallbackContext):
    # Get the item URL from the command argument
    url = context.args[0]

    # Send a message to the user to confirm that tracking has started
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Tracking {url}...")

    # Schedule the URL tracker to run every 5 minutes
    job_queue = context.job_queue
    job_queue.run_repeating(track_url, interval=300, first=0, context=[url, context.bot])
