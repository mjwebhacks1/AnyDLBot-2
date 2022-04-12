import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = "5195870093:AAHhzSFtXzwpaTITa_HygoBWi3NyMO6cEPI"
    # The Telegram API things
    APP_ID = 3796974
    API_HASH = "9511d0112631f9990337eb724d1a7d0d"
    # Get these values from my.telegram.org
    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    # Array to store users who are authorized to use the bot
    AUTH_USERS = "1464063686"
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    #ToDo Forcesubscribe to The Users to use the bot
    UPDATES_CHANNEL = -1001771465683
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = ""
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = "134.209.148.107:8080"
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 100000
    # watermark file
    DEF_WATER_MARK_FILE = "© @MJNewRelease"
    SHORT_LINK_API_URL = os.environ.get("SHORT_LINK_API_URL", "")
    SHORT_LINK_API_KEY = os.environ.get("SHORT_LINK_API_KEY", "")
    IS_TEAM_DRIVE = True
    USE_SERVICE_ACCOUNTS = True
    INDEX_URL = "https://filestream.webshacks.workers.dev/0:"
    parent_id = "0AIPy88fEh11tUk9PVA"
    STRIP_FILE_NAMES = os.environ.get("")
    CHANNEL_URL = "@MJNewRelease"
    # Sql Database url
    DB_URI = ""
