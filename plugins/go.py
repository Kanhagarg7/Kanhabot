
from telethon import events, TelegramClient
from asyncio import sleep as zzz
from random import randint

from . import *

chat = 572621020
hunt = False
list = ["A wild"]

@kanha_bot.on(events.NewMessage(outgoing=True, pattern='.go'))
async def begin(event):
    global hunt
    hunt = True
    try:
        async with kanha_bot.conversation('@Hexamonbot') as conv:
            x = await conv.send_message(chat, "/hunt")
            await conv.get_response(x.id)
    except:
        await zzz(1, 3)
        await conv.send_message(chat, "/hunt")

@kanha_bot.on(events.NewMessage(chats=chat, incoming=True))
async def handle_hunt(event):
    global hunt
    if hunt:
        text = event.message.text
        hun = True
        message = await bot.get_messages(chat, ids=event.message.id)
        if "A shiny" in text:
            await bot.disconnect()
        elif "TM" in text:
            print(event.message.text)
            await zzz(randint(5, 7))
            try:
                async with bot.conversation('@Hexamonbot') as conv:
                    x = await client.send_message(chat, "/hunt")
                    await conv.get_response(x.id)
            except:
                await zzz(3, 7)
                await conv.send_message(chat, "/hunt")
        elif any(item in text for item in list) and hunt:
            await message.click(0)
            await message.click(0, 1)
            await message.click(text="Battle")
        elif "An expert" in text and hunt:
            if not hun:
                pass
            else:
                await zzz(randint(6, 8))
                try:
                    async with bot.conversation('@Hexamonbot') as conv:
                        x = await conv.send_message(chat, "/hunt")
                        await conv.get_response(x.id)
                except:
                    await zzz(3, 5)
                    await conv.send_message(chat, "/hunt")
        elif "Daily limit for battling" in text:
            await stop(None)  # Execute .bstop command

@kanha_bot.on(events.MessageEdited(chats=chat))
async def cacther(event):
    if hunt:
        message = await bot.get_messages(chat, ids=event.message.id)
        await message.click(1, 1)
        await message.click(0, 1)
        await message.click(1, 0)
        
        if any(keyword in event.message.text for keyword in ['fled', 'fainted', 'caught', '+']):
            await zzz(randint(2, 5))
            try:
                async with kanha_bot.conversation('@Hexamonbot') as conv:
                    x = await conv.send_message(chat, "/hunt")
                    await conv.get_response(x.id)
            except:
                await zzz(1, 3)
                await conv.send_message(chat, "/hunt")

@kanha_bot.on(events.NewMessage(outgoing=True, pattern='.bstop'))
async def stop(event):
    global hunt
    hunt = False

@kanha_bot.on(events.NewMessage(chats=chat, incoming=True))
async def handle_battle(event):
    if hunt:
        print(event.message.text)
        if event.message.text[:13] == "Battle begins":
            message = await conv.get_messages(chat, ids=event.message.id)
            await zzz(2)
            await message.click(0, 1)
            await message.click(1, 1)
            await message.click(1, 0)
