class script(object):
    START_TXT = """<b>ഞാൻ ഒരു 𝐀𝐔𝐓𝐎 𝐅𝐈𝐋𝐓𝐄𝐑 𝐁𝐎𝐓 ആണ്, എന്റെ ഉടമസ്ഥർ <a href=https://t.me/cinemavilla>𝘾𝙄𝙉𝙀𝙈𝘼𝙑𝙄𝙇𝙇𝘼 𝙏𝙀𝘼𝙈</a> ആണ്, നിങ്ങൾക്കും നിങ്ങളുടെ ഗ്രൂപ്പുകളിൽ ഇപ്പോൾ എന്നെ ഉപയോഗിക്കാവുന്നതാണ്</b>"""
    HELP_TXT = """<i>Hey</i> {}
<i>Here is the help for my commands.</i>"""
    ABOUT_TXT = """➥ Owner: <a href=https://t.me/Kuruthamkettavan>സാത്താൻ👿</a>
➥ Library: <a href=https://docs.pyrogram.org/>Pyrogram Asyncio 1.13.0</a>
➥ Language: <a href=https://www.python.org/>Python3</a>
➥ Database: <a href=https://www.mongodb.com/cloud/atlas>mongoDB</a>
➥ server: <a href=https://railway.app/>Railway</a>
➥ Build Status: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<i>ഞാൻ ഒരു 𝐀𝐔𝐓𝐎 𝐅𝐈𝐋𝐓𝐄𝐑 𝐁𝐎𝐓 ആണ്, എന്റെ ഉടമസ്ഥർ 𝘾𝙄𝙉𝙀𝙈𝘼𝙑𝙄𝙇𝙇𝘼 𝙏𝙀𝘼𝙈 ആണ്, നിങ്ങൾക്കും നിങ്ങളുടെ ഗ്രൂപ്പുകളിൽ ഇപ്പോൾ എന്നെ ഉപയോഗിക്കാവുന്നതാണ്</i>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/mflinkzbot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Mᴀsᴛᴇʀ ◢ ◤

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """➥ <b>ᴛᴏᴛᴀʟ ғɪʟᴇs</b>: <i>{}</i>
➥ <b>ᴛᴏᴛᴀʟ ᴜsᴇʀs</b>: <i>{}</i>
➥ <b>ᴛᴏᴛᴀʟ ᴄʜᴀᴛs</b>: <i>{}</i>
➥ <b>ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ</b>: <i>{}</i> 
➥ <b>ғʀᴇᴇ sᴛᴏʀᴀɢᴇ</b>: <i>{}</i> """
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
