# Availi Discord Bot
Availi is an availability planner application that is fully integrated as a Discord bot. The program allows a group of people to find a common free time together. 

## Authors
- [Janice] (https://github.com/janiceleee)
- [Jarod] (https://github.com/jarodlee88)

## Requirements
- [Python 3.9.5](https://www.python.org/downloads/release/python-395/)
- [discord.py 1.7.3](https://pypi.org/project/discord.py/)

## Install Discord API from Python library
- `pip install -U discord.py`

## Create a Discord Bot Token
- Head to the [Discord Developer Portal](https://discord.com/developers/applications) and click `New Application` and name your bot.

![DeveloperPortal](https://user-images.githubusercontent.com/33518649/169499858-08d1eac2-f163-4629-b006-cf0acfbf43a1.png)

- Name the bot Availi and select `Create`.

![CreateApplication](https://user-images.githubusercontent.com/33518649/169505965-043afc44-d107-4b13-967a-04f824c8bef7.png)

- Select `Bot` from the menu.

![BotButton](https://user-images.githubusercontent.com/33518649/169639719-9491408e-40de-40ad-b40b-257ca5845703.png)

- Select `Add Bot` Button.

![AddBot](https://user-images.githubusercontent.com/33518649/169639722-be010625-6e48-4ba4-8fd8-df706102a448.png)

- Select the `Click to Reveal Token` to reveal your Discord Token.

![TokenCode](https://user-images.githubusercontent.com/33518649/169639721-73196356-ade6-442d-9367-c4a5c11289e5.png)

## Setup Discord Token into config.py
- Create `config.py` in the same directory as the Availi source code.

![ConfigPy](https://user-images.githubusercontent.com/33518649/169490054-8e8ff621-3563-4c10-8a2e-bedf35d3be18.png)

- Populate `TOKEN` variable in `config.py`.

![Token](https://user-images.githubusercontent.com/33518649/163662962-5ad6c072-f24c-4413-a8e0-bf10abe0c80a.png)

## Invite Availi to a Discord server
- Head to the [Discord Developer Portal](https://discord.com/developers/applications) and select the created Availi application.
- Select `URL Generator` from the `OAuth2` option in the `SETTINGS` tab.
- Tick the `bot` checkbox in the `SCOPES` section.

![BotURLGenerate](https://user-images.githubusercontent.com/33518649/169639237-82de04f6-9fd0-48d3-ab02-43c149fa21da.png)

- Next, tick the `Administrator` in the `BOT PERMISSIONS` section.
- Obtain the Availi invite link from the `GENERATED URL` section below.

![BotURL](https://user-images.githubusercontent.com/33518649/169639235-58fb0607-98e6-4661-80a8-7848165f74f8.png)

- Paste the link into any web browser and invite Availi to your specified Discord server.

![Invite](https://user-images.githubusercontent.com/33518649/169639587-c16667b1-e112-49e9-b256-c7d3f011304b.png)

## Bot Commands
>`!start`
>- Sets up a new Availi-Channel

>`!add <time>`
>- Add available times: 'dd/mm/yyyy hh:mm with only 30 mins intervals'

>`!delete <time>`
>- Delete specific available times: 'dd/mm/yyyy hh:mm with only 30 mins intervals'

>`!show`
>- Show user's available times

>`!availi`
>- Show everybody's available times

>`!help`
>- Show a list of commands