# pelicanconf.py
# 用 Pelican 把网页输出到 docs/ 文件夹：
# 运行：pelican content -o docs -s pelicanconf.py

# ──────────────────────────────────────────────────────────
# 站点基本信息
# ──────────────────────────────────────────────────────────
SITENAME     = "Xiaoxin's work"
SITEURL      = ""                 # 本地调试留空；上线时改成你的域名

# ──────────────────────────────────────────────────────────
# 内容路径与语言、时区
# ──────────────────────────────────────────────────────────
PATH         = "content"          # 放 Markdown 文件的目录
TIMEZONE     = "Europe/Rome"
DEFAULT_LANG = "en"               # 主站语言：英文（/）

# ──────────────────────────────────────────────────────────
# Feed 配置（开发时通常关闭）
# ──────────────────────────────────────────────────────────
FEED_ALL_ATOM         = None
CATEGORY_FEED_ATOM    = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM      = None
AUTHOR_FEED_RSS       = None

# ──────────────────────────────────────────────────────────
# 右侧链接与社交
# ──────────────────────────────────────────────────────────
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("Modify these links in your config file", "#"),
)

SOCIAL = (
    ("GitHub", "https://github.com/littlexx15"),
    ("linkedin", "https://www.linkedin.com/in/xiaoxin-xiang/"),
    ("Instagram", "https://www.instagram.com/littlexx155/"),
)

# ──────────────────────────────────────────────────────────
# 分页设置
# ──────────────────────────────────────────────────────────
DEFAULT_PAGINATION = False         # 一页展示所有文章；若想分页可改为 True 或数字
DISPLAY_AUTHOR     = False         # 关掉作者显示（文章页与列表）

# ──────────────────────────────────────────────────────────
# 主题与 URL 设置
# ──────────────────────────────────────────────────────────
THEME               = "themes/basic"
RELATIVE_URLS       = True         # 本地调试时使用相对链接
THEME_TEMPLATES_OVERRIDES = ["templates"]  # 优先读取你自定义的 templates/

# 分类页面 URL（如需）
CATEGORY_URL      = "category/{slug}.html"
CATEGORY_SAVE_AS  = "category/{slug}.html"

# ──────────────────────────────────────────────────────────
# 静态资源（图片 & 自定义 CSS）
# ──────────────────────────────────────────────────────────
STATIC_PATHS = [
    "images",             # content/images/
    "extra/custom.css",   # content/extra/custom.css
]

EXTRA_PATH_METADATA = {
    "extra/custom.css": {"path": "static/custom.css"},
}

# ──────────────────────────────────────────────────────────
# 多语言（i18n_subsites）
# pip install pelican-i18n-subsites Babel
# ──────────────────────────────────────────────────────────
PLUGINS = [
    "i18n_subsites",      # 启用多语言子站
]

# 让 Jinja2 模板支持 i18n（模板中可用 gettext、trans 等）
JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n"]
}

# 为中文子站（/zh/）定义覆盖项
I18N_SUBSITES = {
    "zh": {
        "SITENAME": "小欣的作品",
        "LOCALE": "zh_CN",    # 影响日期/本地化格式
        # 需要的话可在此处为中文站单独设置 THEME、MENUITEMS 等
    }
}

# 模板的“默认翻译语言”（可保持为主站语言）
I18N_TEMPLATES_LANG = "en"
