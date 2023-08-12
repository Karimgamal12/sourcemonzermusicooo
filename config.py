from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/4ba256827d2d175e7dc05.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/88b355899c7f69172dacc.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/va_source")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/sourceav")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5593884330,1400467850").split()))


FAILED = "https://telegra.ph/file/c3f36d3d0dda9d2989764.jpg"
