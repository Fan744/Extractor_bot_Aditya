#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8124137115:AAF1mcRDL4jAssXKD-_G_C3far3vwU3Q_ZQ")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "30157302"))
    API_HASH = os.environ.get("API_HASH", "0052039fb2fca727868d0228cdaad569")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "8255552078").split())
    
