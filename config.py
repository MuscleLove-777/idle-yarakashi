"""放置ゲームやらかしアーカイブ - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "放置ゲームやらかしアーカイブ"
BLOG_DESCRIPTION = "放置ゲームでの「廃課金・嫁バレ・サ終直撃」などのやらかし告白を笑える形で記録するメディア。喪失体験を共有することで、ガチ攻略系には書けない人間ドラマを残す。"
BLOG_URL = "https://musclelove-777.github.io/idle-yarakashi/"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/idle-yarakashi"

TARGET_CATEGORIES = [
    "廃課金やらかし告白",
    "サ終墓標アーカイブ",
    "嫁・恋人バレ事件簿",
    "リセマラ無限ループ体験記",
    "放置忘れリアル損失録",
    "復帰勢のあるある",
    "メンタル消耗ストーリー",
]

THEME = {
    "primary": "#3b1f5c",
    "accent": "#ff6b35",
    "gradient_start": "#3b1f5c",
    "gradient_end": "#ff6b35",
}

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_FALLBACK_MODEL = "gemini-2.5-flash-lite"

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

MAX_ARTICLE_LENGTH = 4000
SEO_KEYWORD_DENSITY = 0.02
