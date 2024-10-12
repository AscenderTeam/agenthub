from enum import Enum


class PlatformEnum(Enum):
    UNKNOWN = "unknown"
    TELEGRAM_BOT = "telegram:bot"
    TELEGRAM_SUPPORT = "telegram:support"
    INSTAGRAM_BUSINESS = "instagram:business"
    INSTAGRAM_AUTHOR = "instagram:author"
    FACEBOOK_BUSINESS = "facebook:business"
    WEB_WIDGET = "web:widget"
    WEB_APP = "web:app"
    MOBILE = "mobile:support"
    MOBILE_ANDROID = "mobile:android"
    MOBILE_IOS = "mobile:ios"
    DESKTOP_WINDOWS = "desktop:windows"
    DESKTOP_MACOS = "desktop:macos"
    DESKTOP_OSX = "desktop:osx"
    DESKTOP_LINUX = "desktop:linux"