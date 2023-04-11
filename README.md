# Asuna - ChatGPT Discord Bot

Asuna is a powerful, intelligent, and user-friendly Discord bot that leverages the OpenAI ChatGPT API to provide an engaging and interactive chat experience in Discord servers. Additionally, it can detect and automatically delete any messages containing racist, sexist, or other negative content to maintain a safe and welcoming environment for all users.

## Table of Contents

- [Features](#features)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contribute](#contribute)
- [License](#license)

## Features

- Engaging chat experience with OpenAI ChatGPT integration
- Real-time detection and deletion of racist, sexist, or negative messages
- Customizable configurations for server-specific needs
- Easy-to-use commands for users and admins
- Regular updates and improvements

## Installation and Setup

1. **Clone the repository**

```bash
git clone git@github.com:danielgvco/Asuna-DiscordBot.git
cd Asuna-DiscordBot
```

2. **Install dependencies**

\```bash
pip3 install openai
pip3 install discord.py
pip3 install python-dotenv
\```

3. **Configure environment variables**

Copy the `.env.example` file to a new file named `.env` and fill in the necessary values:
- Discord API Token
- OpenAI API Key
- SSL CERT PATH only if neccesary

\```bash
cp .env.example .env
\```

4. **Start the bot**

\```bash
python3 main.py
\```

Asuna should now be running on your Discord server.

## Usage

- `!asuna <message>` - Chat with Asuna using the ChatGPT API.
- `!asuna help` - Display a list of available commands and their descriptions.
- `!asuna config` - Display the current configuration settings.
- `!asuna config set <setting> <value>` - Set a new value for a specific configuration setting (admin only).

## Configuration

Asuna can be configured to fit the needs of your specific server. Available configuration settings include:

- `delete_negative_messages`: (default: `true`) Enable or disable automatic deletion of detected negative messages.
- `custom_greeting`: (default: `Hello! I'm Asuna.`) Set a custom greeting message for Asuna to use when joining a server.

## Contribute

I welcome contributions from the community! If you'd like to help improve Asuna, please feel free to create an issue or submit a pull request on the [GitHub repository](https://github.com/danielgvco/Asuna-DiscordBot).

## License

Asuna is released under the [MIT License](https://opensource.org/licenses/MIT).
