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
    UPDATES_CHANNEL = "mjfileupload"
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
    SHORT_LINK_API_URL = os.environ.get("SHORT_LINK_API_URL", "https://za.gl/api")
    SHORT_LINK_API_KEY = os.environ.get("SHORT_LINK_API_KEY", "")
    IS_TEAM_DRIVE = True
    USE_SERVICE_ACCOUNTS = True
    INDEX_URL = "https://filestream.webshacks.workers.dev/0:"
    parent_id = "0AIPy88fEh11tUk9PVA"
    STRIP_FILE_NAMES = os.environ.get("STRIP_FILE_NAMES","www.1TamilMV.life - |www.1TamilMV.life -|www.1TamilMV.org - |www.1TamilMV.org -|www.1TamilMV.xyz - |www.1TamilMV.xyz -|@MoviesFlixers_DL|@TellyFun_Official|[MM].|[MM]|[MM] -|www_Telugupalaka_com|@MM_New|@MM_Links|@MM_Linkz|www.TamilRockers.ws -|@Animationmovies|HT_BEATS_|-@lubokvideo|@lubokvideo|@english_movieschannel_|@english_movieschannel|@themovies_channel_|@themovies_channel|@telugu_bluray|@TVshows_HD|[Movies Vip]|[CC].|[CC]|@CC_Links.|@CC_Links|@CC_x265.|@CC_x265|@CC.|@CC|@CC_ALL|@CPR_|@CPR|Moviez_India.|Moviez_India")
    CHANNEL_URL = "@MJNewRelease"
    # Sql Database url
    DB_URI = "postgres://upkvjoduavonpd:e89e8af580ca1292251f405450d91c6e0a633ba0395e9cc44f178aff25f5deeb@ec2-52-48-159-67.eu-west-1.compute.amazonaws.com:5432/dfr8j2f3erinl8"
    
