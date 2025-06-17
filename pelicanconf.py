# pelicanconf.py
# # 用 Pelican 把网页输出到 docs/ 文件夹
# 输入指令 pelican content -o docs -s pelicanconf.py
# ──────────────────────────────────────────────────────────
# 站点基本信息
# ──────────────────────────────────────────────────────────
# AUTHOR      = ''
SITENAME    = "Xiaoxin's work"
SITEURL     = ''              # 本地调试留空；上线时改成你的域名

# ──────────────────────────────────────────────────────────
# 内容路径与语言、时区
# ──────────────────────────────────────────────────────────
PATH        = 'content'       # 放 Markdown 文件的目录
TIMEZONE    = 'Europe/Rome'
DEFAULT_LANG= 'en'

# ──────────────────────────────────────────────────────────
# Feed 配置（开发时通常关闭）
# ──────────────────────────────────────────────────────────
FEED_ALL_ATOM        = None
CATEGORY_FEED_ATOM   = None
TRANSLATION_FEED_ATOM= None
AUTHOR_FEED_ATOM     = None
AUTHOR_FEED_RSS      = None

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
    ("GitHub", "https://github.com/littlexx15/AI-4-Media-Project-XiaoxinXiang"),
    ("Another link", "#"),
)

# ──────────────────────────────────────────────────────────
# 分页设置
# ──────────────────────────────────────────────────────────
DEFAULT_PAGINATION = False   # 一页展示所有文章；若想分页可改为 True 或数字

# ──────────────────────────────────────────────────────────
# 主题与 URL 设置
# ──────────────────────────────────────────────────────────
THEME           = 'themes/basic'
RELATIVE_URLS   = True       # 本地调试时使用相对链接

# ──────────────────────────────────────────────────────────
# 静态资源（图片 & 自定义 CSS）
# ──────────────────────────────────────────────────────────
STATIC_PATHS = [
    'images',            # content/images/
    'extra/custom.css',  # content/extra/custom.css
]

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}

# ──────────────────────────────────────────────────────────
# （可选）首页标题替换
# ──────────────────────────────────────────────────────────
# INDEX_TITLE = "My Projects 我的项目"

# ──────────────────────────────────────────────────────────
# （可选）按日期排序，最新在前
# ──────────────────────────────────────────────────────────
# ARTICLE_ORDER_BY = 'date'
# pelicanconf.py

# …（前面已有内容省略）…

# 主题与 URL 设置
THEME           = 'themes/basic'
RELATIVE_URLS   = True

# 关闭文章页和列表中作者显示
DISPLAY_AUTHOR  = False

# …（后续已有静态资源、分页等配置）…
# pelicanconf.py

# … 其余配置不变 …
# 让 Pelican 从模板覆盖目录优先读取
THEME_TEMPLATES_OVERRIDES = ['templates']



