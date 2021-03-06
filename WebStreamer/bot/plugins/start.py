import urllib.parse
from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant

db = Database(Var.DATABASE_URL, Var.SESSION_NAME)

START_TEXT = """
<i>Hello There,</i>{}\n
<i>A Telegram Bot To Generate Direct Download Link For Any Telegram File, Video, Image Or Anything Else!</i>\n
<i>Clickk On Help Button Get Get Info!</i>\n
<i><u>πͺππ₯π‘ππ‘π </u></i>
<b>π Porn Content May Lead You To A Permanent Ban</b>\n\n
<i><b>Developer:</b>@Harshu_xD</i>"""

HELP_TEXT = """
<i>- Forward Any Telegram File Or Media.</i>
<i>- The Direct Link Will Be Generated ASAP!.</i>
<i>- You Can Add Me To Your Group/Channel For Instant Links</i>
<i>- This Is A Permanent Link</i>\n
<u> πͺππ₯π‘ππ‘π </u>\n
<b>π Porn Content May Lead You To A Permanent Ban</b>\n
<i>Contact Developer Or Report Bugs</i> <b>: <a href='https://t.me/Harshu_xD'>[ Click Here]</a></b>"""

ABOUT_TEXT = """
<b>π§π»MΚ Ι΄α΄α΄α΄ : Direct-Link-Bot</b>\n
<b>πΈMovie Channel : <a href='https://t.me/+0Oi54BOKV_A2YTI1'>Movies</a></b>\n
<b>πΉOur Community : <a href='https://telegram.me/StarterNetworkz'>Network</a></b>\n
<b>πΉDα΄α΄ α΄Κα΄α΄α΄Κ : <a href='https://telegram.me/Harshu_XD'>Harsh</a></b>\n
<b>πΈLeech & Mirror Group : <a href='https://t.me/StarterLeech'>Leech & Mirror Group</a></b>"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hα΄Κα΄', callback_data='help'),
        InlineKeyboardButton('AΚα΄α΄α΄', callback_data='about'),
        InlineKeyboardButton('CΚα΄sα΄', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hα΄α΄α΄', callback_data='home'),
        InlineKeyboardButton('AΚα΄α΄α΄', callback_data='about'),
        InlineKeyboardButton('CΚα΄sα΄', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hα΄α΄α΄', callback_data='home'),
        InlineKeyboardButton('Hα΄Κα΄', callback_data='help'),
        InlineKeyboardButton('CΚα΄sα΄', callback_data='close')
        ]]
    )

@StreamBot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()

def get_media_file_size(m):
    media = m.video or m.audio or m.document
    if media and media.file_size:
        return media.file_size
    else:
        return None


def get_media_file_name(m):
    media = m.video or m.document or m.audio
    if media and media.file_name:
        return urllib.parse.quote_plus(media.file_name)
    else:
        return None


@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**New Mate Joined:** \n\n__MΚ Nα΄α΄‘ FΚΙͺα΄Ι΄α΄__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sα΄α΄Κα΄α΄α΄ Yα΄α΄Κ Bα΄α΄ !!__"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="__Hey, Yα΄α΄ α΄Κα΄ Bα΄Ι΄Ι΄α΄α΄ α΄α΄ α΄sα΄ α΄α΄. Cα΄Ι΄α΄α΄α΄α΄ α΄Κα΄ Dα΄α΄ α΄Κα΄α΄α΄Κ__\n\n @AafuSam13 **TΚα΄Κ WΙͺΚΚ Hα΄Κα΄ Yα΄α΄**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>Join Our Channel To Use The Bot π</i>",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton("Jα΄ΙͺΙ΄ Ι΄α΄α΄‘ π", url=f"https://t.me/StarterMods")
                            ]]
                    ),
                    parse_mode="HTML"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>Sα΄α΄α΄α΄ΚΙͺΙ΄Ι’ α΄‘Κα΄Ι΄Ι’ α΄α΄Ι΄α΄α΄α΄α΄ α΄Κ α΄α΄α΄ α΄Κα΄α΄α΄Κ</i> <b><a href='http://t.me/Harshu_xD'>[ Click Here ]</a></b>",
                    parse_mode="HTML",
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text=START_TEXT.format(m.from_user.mention),
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
              )                                                                         
                                                                                       
                                                                            
    else:
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**Sα΄ΚΚΚ SΙͺΚ, Yα΄α΄ α΄Κα΄ Bα΄Ι΄Ι΄α΄α΄ α΄α΄ α΄sα΄ α΄α΄. Qα΄Ιͺα΄α΄ΚΚ α΄α΄Ι΄α΄α΄α΄α΄** @AafuSam13",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Join Our Partner Channel To Use The Bot**!\n\n**Dα΄α΄ α΄α΄ Oα΄ α΄ΚΚα΄α΄α΄, OΙ΄ΚΚ CΚα΄Ι΄Ι΄α΄Κ Sα΄Κsα΄ΚΙͺΚα΄Κs α΄α΄Ι΄ α΄sα΄ α΄Κα΄ Bα΄α΄**!",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                          InlineKeyboardButton("π€ Join Partner Channel", url=f"https://t.me/StarterMods")],
                         [InlineKeyboardButton("π Refresh / Try Again", url=f"https://t.me/{(await b.get_me()).username}?start=HarshxD_{usr_cmd}")
                        
                        ]]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Sα΄α΄α΄α΄ΚΙͺΙ΄Ι’ α΄‘α΄Ι΄α΄ WΚα΄Ι΄Ι’. Cα΄Ι΄α΄α΄α΄α΄ α΄α΄** [Harsh](https://t.me/Harshu_xD).",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))
        file_name = get_media_file_name(get_msg)
        file_size = humanbytes(get_media_file_size(get_msg))

        stream_link = "https://{}/{}/{}".format(Var.FQDN, get_msg.message_id, file_name) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.message_id,
                                     file_name)

        msg_text ="""
<i><u>Hurrey! Your Link Generated !</u></i>\n
<b>π FΙͺΚα΄ Ι΄α΄α΄α΄ :</b> <i>{}</i>\n
<b>π¦ FΙͺΚα΄ κ±Ιͺα΄’α΄ :</b> <i>{}</i>\n
<b>π₯ Dα΄α΄‘Ι΄Κα΄α΄α΄ :</b> <i>{}</i>\n
<b>πΈ Nα΄α΄α΄ : LΙͺΙ΄α΄ α΄xα΄ΙͺΚα΄α΄ ΙͺΙ΄ 24 Κα΄α΄Κκ±</b>\n
<i>π Developer:</i> <b>@Harshu_xD</b>
"""

        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Dα΄α΄‘Ι΄Κα΄α΄α΄ Ι΄α΄α΄‘ π₯", url=stream_link)]])
        )



@StreamBot.on_message(filters.private & filters.command(["about"]))
async def start(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )


@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**Nα΄α΄‘ Usα΄Κ Jα΄ΙͺΙ΄α΄α΄ **\n\n__MΚ Nα΄α΄‘ FΚΙͺα΄Ι΄α΄__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i>Sα΄ΚΚΚ SΙͺΚ, Yα΄α΄ α΄Κα΄ Bα΄Ι΄Ι΄α΄α΄ α΄α΄ α΄sα΄ α΄α΄. Cα΄Ι΄α΄α΄α΄α΄ α΄Κα΄ Dα΄α΄ α΄Κα΄α΄α΄Κ</i>",
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Join Our Partner Channel To Use The Bot**\n\n__Dα΄α΄ α΄α΄ Oα΄ α΄ΚΚα΄α΄α΄, OΙ΄ΚΚ CΚα΄Ι΄Ι΄α΄Κ Sα΄Κsα΄ΚΙͺΚα΄Κs α΄α΄Ι΄ α΄sα΄ α΄Κα΄ Bα΄α΄!__",
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton("π€ Join Partner Channel", url=f"https://t.me/StarterChannel")
                        ]]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__Sα΄α΄α΄α΄ΚΙͺΙ΄Ι’ α΄‘α΄Ι΄α΄ WΚα΄Ι΄Ι’. Cα΄Ι΄α΄α΄α΄α΄ α΄α΄__ [Harsh](https://t.me/Harshu_xD).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text=HELP_TEXT,
        parse_mode="HTML",
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
        )

