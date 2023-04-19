from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🌹 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 🌹", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 𝐇𝐨𝐦𝐞 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton("🥀 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 🥀", url="https://t.me/BikashGadgetsTech"),
            InlineKeyboardButton("🥀 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🥀", url="https://t.me/Bgt_chat")
        ],
        [
            InlineKeyboardButton("✨ 𝐇𝐞𝐥𝐩 ✨", callback_data="help"),
            InlineKeyboardButton("🌺 𝐁𝐨𝐭 𝐈𝐧𝐟𝐨 🌺", callback_data="about")
        ],
        [InlineKeyboardButton("📱𝐘𝐨𝐮𝐭𝐮𝐛𝐞📱", url="https://youtube.com/@BikashGadgetsTech")],
    ]

    START = """
🥀 𝐇𝐞𝐲 {},

▷ 𝐌𝐲 𝐍𝐚𝐦𝐞 𝐈𝐬 {},
▷ 𝐈'𝐦 𝐀 𝐒𝐭𝐫𝐢𝐧𝐠 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐁𝐨𝐭 🥀
▷ 𝐈𝐟 𝐘𝐨𝐮 𝐓𝐫𝐮𝐬𝐭 𝐌𝐞 𝐓𝐡𝐞𝐧 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐒𝐞𝐬𝐬𝐢𝐨𝐧
▷ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧 𝐎𝐫 𝐏𝐲𝐫𝐨𝐠𝐫𝐦 𝐁𝐨𝐭𝐡 

🥀 𝐂𝐫𝐞𝐚𝐭𝐨𝐫™ : [𝐁𝐢𝐤𝐚𝐬𝐡](https://t.me/BikashHalder) !
    """

    HELP = """
🍁 **𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐂𝐨𝐦𝐦𝐧𝐝𝐬** 🍁

/about -  𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐁𝐨𝐭
/cancel - 𝐂𝐚𝐧𝐜𝐞𝐥 𝐀𝐥𝐥 𝐏𝐫𝐨𝐜𝐞𝐬𝐬
/donate - 𝐅𝐨𝐫 𝐃𝐨𝐧𝐚𝐭𝐞 
/generate - 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧
/help - 𝐅𝐨𝐫 𝐇𝐞𝐥𝐩
/restart - 𝐂𝐚𝐧𝐜𝐞𝐥 𝐓𝐡𝐞 𝐏𝐫𝐨𝐜𝐞𝐬𝐬
/start - 𝐒𝐭𝐚𝐫𝐭 𝐓𝐡𝐞 𝐁𝐨𝐭
"""

    ABOUT = """
**𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭** 

◉ 𝐓𝐡𝐢𝐬 𝐈𝐬 𝐀 𝐒𝐭𝐫𝐢𝐧𝐠 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐁𝐨𝐭 𝐒𝐮𝐩𝐩𝐨𝐫𝐭
𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧 𝐎𝐫 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐁𝐨𝐭𝐡 🥀

[𝐒𝐮𝐛𝐜𝐫𝐢𝐛𝐞](https://youtube.com/@BikashGadgetsTech)

[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/BikashGadgetsTech) [𝐒𝐮𝐩𝐩𝐨𝐫𝐭](https://t.me/Bgt_chat)

◉ 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : [𝐁𝐢𝐤𝐚𝐬𝐡](https://t.me/BikashHalder)
    """
