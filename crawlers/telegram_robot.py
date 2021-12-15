# -*- coding: utf-8 -*-

import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events


class TelegramMessager:
    api_id = 'API_id'
    api_hash = 'API_hash'
    token = 'bot token'
    source_phone = 'YOUR_PHONE_NUMBER_WTH_COUNTRY_CODE'

    def __init__(self):
        self.client = TelegramClient('session',
                                     self.api_id,
                                     self.api_hash)
        self.client.connect()

    def send_message(self, phone, message="Nothing to say..."):

        if not self.client.is_user_authorized():
            self.client.send_code_request(phone)
            self.client.sign_in(phone, input('Enter the code: '))

        try:
            receiver = InputPeerUser('user_id', 'user_hash')
            self.client.send_message(receiver, message, parse_mode='html')
        except Exception as e:
            error_message = f"Something went wrong: {e}"
            print(error_message)

    def __del__(self):
        self.client.disconnect()
