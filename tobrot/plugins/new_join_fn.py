#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

import logging

import pyrogram
from tobrot import AUTH_CHANNEL, LOGGER


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(f"Current CHAT ID: <code>{message.chat.id}</code>")
        # leave chat
        await client.leave_chat(chat_id=message.chat.id, delete=True)
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    # await message.reply_text("no one gonna help you 🤣🤣🤣🤣", quote=True)
    # channel_id = str(AUTH_CHANNEL)[4:]
    # message_id = 99
    # display the /help

    await message.reply_text(
        """here is a list of CMDS available for the bot.👇\n\nytdl_1 - This command should be used as reply to a supported link.\npytdl_1 - This command will download videos from youtube playlist link and will upload to telegram.\nleech_1 - leech any torrent/magnet/direct-download link to Telegram.=\nleechunzip_1 - This will unarchive file and upload to telegram.\nsavethumbnail_1 - To Add Thumbnail To File.\nclearthumbnail_1 - To Remove Previously Added Thumbnail.\nstatus_1 - show status of current downloads and stuff.\ntoggledoc_1 - choose whether the file shall be uploaded as doc or not.\ntogglevid_1 - choose whether the file shall be uploaded as streamable or not.\nhelp_1 - send help.\nrenewme_1 - clear all downloads.(admin only)⚠️\nlog_1 - This will send you a txt file of the logs.(admin only)⚠️""",
        disable_web_page_preview=True,
    )
