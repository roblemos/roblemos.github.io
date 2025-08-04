# pelicanconf.py

AUTHOR = 'Robert Lemos'
SITENAME = 'Robert Lemos'
SITESUBTITLE = 'writer, journalist, coder, data analyst'
LOGO = 'images/logo.png'  # assuming it's in 'content/extra/logo.png'

PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
WITH_FUTURE_DATES = True

# Use your local theme
THEME = 'themes/writerslog'

# These paths are relative to your content directory by default
STATIC_PATHS = ['images', 'extra/favicon.png', 'extra/logo.png', 'articles']
EXTRA_PATH_METADATA = {
    'extra/favicon.png': {'path': 'favicon.png'},
    'extra/logo.png': {'path': 'images/logo.png'},
}
ARTICLE_PATHS = ['articles']

# URL format
ARTICLE_URL = '{date:%Y}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'

# Feed generation usually disabled during development
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

DEFAULT_PAGINATION = 5

# Blogroll
LINKS = (
    ("Lemos Associates LLC", "https://www.lemosassociates.com/"),
    ("Dark Reading", "https://www.darkreading.com/"),
    ("MIT Tech Review", "https://technologyreview.com"),
    ("Pelican", "https://getpelican.com/"),
)

# Social widget
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/roblemos/"),
    ("GitHub", "https://github.com/roblemos"),
    ("Bluesky", "https://roblemos.bsky.social"),
    ("X/Twitter", "https://x.com/roblemos"),
)
