# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โจ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
๐ญ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) allows you to play music and video on groups through the new Telegram's video chats!**

๐ก **Find out all the Bot's commands and how they work by clicking on the ยป ๐ Commands button!**

๐ **To know how to use this bot, please click on the ยป โ Basic Guide button!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ Add me to your Group โ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("โ Basic Guide", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("๐ Commands", callback_data="cbcmds"),
                    InlineKeyboardButton("โค Donate", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "๐ฅ Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "๐ฃ Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "๐ Source Code", url="https://github.com/levina-lab/video-stream"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โ **Basic Guide for using this bot:**

1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**

๐ **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

๐ก **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โจ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

ยป **press the button below to read the explanation and see the list of available commands !**

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("๐ท๐ป Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("๐ง๐ป Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("๐ Basic Cmd", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("๐ Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ here is the basic commands:

ยป /play (song name/link) - play music on video chat
ยป /vplay (video name/link) - play video on video chat
ยป /vstream - play live video from yt live/m3u8
ยป /playlist - show you the playlist
ยป /video (query) - download video from youtube
ยป /song (query) - download song from youtube
ยป /lyric (query) - scrap the song lyric
ยป /search (query) - search a youtube video link

ยป /ping - show the bot ping status
ยป /uptime - show the bot uptime status
ยป /alive - show the bot alive info (in group)

โก๏ธ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ here is the admin commands:

ยป /pause - pause the stream
ยป /resume - resume the stream
ยป /skip - switch to next stream
ยป /stop - stop the streaming
ยป /vmute - mute the userbot on voice chat
ยป /vunmute - unmute the userbot on voice chat
ยป /volume `1-200` - adjust the volume of music (userbot must be admin)
ยป /reload - reload bot and refresh the admin data
ยป /userbotjoin - invite the userbot to join group
ยป /userbotleave - order userbot to leave from group

โก๏ธ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ here is the sudo commands:

ยป /rmw - clean all raw files
ยป /rmd - clean all downloaded files
ยป /sysinfo - show the system information
ยป /update - update your bot to latest version
ยป /restart - restart your bot
ยป /leaveall - order userbot to leave from all group

โก __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\nยป revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"โ๏ธ **settings of** {query.message.chat.title}\n\nโธ : pause stream\nโถ๏ธ : resume stream\n๐ : mute userbot\n๐ : unmute userbot\nโน : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("โน", callback_data="cbstop"),
                      InlineKeyboardButton("โธ", callback_data="cbpause"),
                      InlineKeyboardButton("โถ๏ธ", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("๐", callback_data="cbmute"),
                      InlineKeyboardButton("๐", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("๐ Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("โ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
