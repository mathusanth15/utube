import os


class Config:

    BOT_TOKEN = os.environ.get("1991699635:AAEKPca5JvN4pxusGNTf-m7C4kxjK_GcIvU")

    SESSION_NAME = os.environ.get("YouTubeUploader", ":memory:")

    API_ID = int(os.environ.get("5615631"))

    API_HASH = os.environ.get("f65d600ff580456871cfddc086337b7a")

    CLIENT_ID = os.environ.get("921912615039-42h2eg2tsqcmbig6mae5df8vai54mbff.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("GnsnVpyT3DT9cJStuexDOJ55")

    BOT_OWNER = int(os.environ.get("1496802577"))

    AUTH_USERS_TEXT = os.environ.get("1496802577", "")

    AUTH_USERS = [BOT_OWNER, 374321319] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        felse []
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
        if UPLOAD_MODE.lower() in ["public"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = true

    CRED_FILE = "auth_token.txt"
