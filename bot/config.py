from decouple import config

try:
    APP_ID = int(config("APP_ID", "16768772"))
    API_HASH = config("API_HASH", "08d78fb05bdb90f1be4a4f1f0fef5f1e")
    BOT_TOKEN = config("BOT_TOKEN", "6638585728:AAFOannafCxDwgiG0QKRhugAg9r9zVExozk")
    DEV = 1664850827
    OWNER = config("OWNER", "5725206423")
    ffmpegcode = ["-preset superfast -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 12 -metadata title='𝙰𝚗𝚒𝚖𝚎_𝚆𝚊𝚛𝚒𝚘𝚛' -metadata author='𝙰𝚗𝚒𝚖𝚎_𝚆𝚊𝚛𝚒𝚘𝚛' -metadata:s:s title='𝙰𝚗𝚒𝚖𝚎_𝚆𝚊𝚛𝚒𝚘𝚛' -metadata:s:a title='𝙰𝚗𝚒𝚖𝚎_𝚆𝚊𝚛𝚒𝚘𝚛' -metadata:s:v title='𝙰𝚗𝚒𝚖𝚎_𝚆𝚊𝚛𝚒𝚘𝚛'"]
    THUMB = config("THUMBNAIL", default="https://te.legra.ph/file/dbf430121d50d9324a3b7.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
