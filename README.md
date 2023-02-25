## AutoDealTrackerTelegram

This Python script is a Telegram bot that can track deals on websites. It uses the `requests` and `BeautifulSoup` libraries to scrape websites for deal information and the `telegram.ext` library to interact with users on Telegram.

### Prerequisites

To use this script, you will need to have the following libraries installed on your machine:

- `requests`
- `BeautifulSoup`
- `telegram`

You will also need a Telegram bot token, which you can obtain by creating a bot with the Telegram BotFather.

### Setup

1. Clone this repository to your local machine or download the script directly.

2. Replace the `BOT_TOKEN` placeholder with your own Telegram bot token.

3. Customize the code inside the `track` function to match the website and deal information you want to track.

4. Run the script.

### Usage

To use this script, start the bot by running the script and then send a message to your bot on Telegram with the command `/start`. This will trigger the `start` function and the bot will respond with a message indicating that it is ready to start tracking deals.

To track a deal, send a message to the bot with the command `/track <item_url>`, where `<item_url>` is the URL of the item you want to track.

The bot will start scraping the website for deal information and will notify you on Telegram if a deal is found. It will continue to check the website every 5 minutes[can be changed] until you manually stop the script.

To stop the script, simply interrupt the program by pressing `Ctrl + C`.

### License

This project is licensed under the terms of the [MIT license](https://opensource.org/licenses/MIT).

