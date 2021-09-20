import os


class Config:

    BOT_TOKEN = os.environ.get("2049035615:AAGe-i1F3bqgx--u-ZCUPkFqHeX3dd9UefY")

    SESSION_NAME = os.environ.get("utubexnbot", ":memory:")

    API_ID = int(os.environ.get("5615631"))

    API_HASH = os.environ.get("f65d600ff580456871cfddc086337b7a")

    CLIENT_ID = os.environ.get("921912615039-20vufhe7in808ndndeqi6b22dku97c3d.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("n4U9JX7LI_AYOOGCNkpfIluH")

    BOT_OWNER = int(os.environ.get("1496802577"))

    AUTH_USERS_TEXT = os.environ.get("1496802577", "")

    AUTH_USERS = [BOT_OWNER, 374321319] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = ture

    CRED_FILE = "auth_token.txt"
import os


class Config:

    BOT_TOKEN = os.environ.get("BOT_TOKEN")

    SESSION_NAME = os.environ.get("SESSION_NAME", ":memory:")

    API_ID = int(os.environ.get("API_ID"))

    API_HASH = os.environ.get("API_HASH")

    CLIENT_ID = os.environ.get("CLIENT_ID")

    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

    BOT_OWNER = int(os.environ.get("BOT_OWNER"))

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER, 374321319] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
