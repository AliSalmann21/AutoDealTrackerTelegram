# Deal Tracker Bot

This is a Telegram bot that can track a URL for deals and notify the user when a deal is available.

## Getting Started

### Prerequisites

- Python 3.x
- `requests` library
- `BeautifulSoup` library
- `python-telegram-bot` library

### Installing

1. Clone this repository:

     git clone https://github.com/AliSalmann21/AutoDealTrackerTelegram

2. Install the required Python libraries:

     pip install -r requirements.txt


### Usage

1. Create a new Telegram bot by following the instructions [here](https://core.telegram.org/bots#3-how-do-i-create-a-bot).
2. Copy the bot token.
3. Run the script with the bot token as a command-line argument:

     python deal_tracker_bot.py YOUR_BOT_TOKEN


4. In Telegram, start a conversation with the bot and use the `/track` command followed by the URL to start tracking a deal:

     /track https://www.example.com/item

## Contributing

Contributions are welcome! If you would like to contribute, please follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes.
4. Test your changes.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
