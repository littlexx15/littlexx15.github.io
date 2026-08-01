const featuredRepos = [
  {
    name: "prompt-pocket",
    description: "个人提示词管理与案例素材库",
    language: "HTML",
    html_url: "https://github.com/littlexx15/prompt-pocket",
    pushed_at: "2026-07-30T02:54:09Z"
  },
  {
    name: "auto-video-mixer",
    description: "Windows 桌面自动视频混剪工具",
    language: "Python",
    html_url: "https://github.com/littlexx15/auto-video-mixer",
    pushed_at: "2026-07-30T02:37:27Z"
  },
  {
    name: "video-mixer",
    description: "视频智能随机混剪与预览剪辑工具",
    language: "PowerShell",
    html_url: "https://github.com/littlexx15/video-mixer",
    pushed_at: "2026-07-28T03:01:24Z"
  },
  {
    name: "feed-video-organizer",
    description: "面向内容生产流程的视频素材整理工具",
    language: "Python",
    html_url: "https://github.com/littlexx15/feed-video-organizer",
    pushed_at: "2026-07-01T00:00:00Z"
  },
  {
    name: "ai-mock-interview",
    description: "用 AI 驱动的模拟面试练习项目",
    language: "Python",
    html_url: "https://github.com/littlexx15/ai-mock-interview",
    pushed_at: "2026-04-09T11:24:46Z"
  },
  {
    name: "Algorithmic-Touch",
    description: "探索计算机视觉、交互与触觉体验的实验项目",
    language: "Python",
    html_url: "https://github.com/littlexx15/Algorithmic-Touch",
    pushed_at: "2025-06-12T19:09:34Z"
  }
];

const repoGrid = document.querySelector("#repo-grid");

const projectCopy = {
  "fruit-tasting-clip-extractor": {
    title: "人物试吃片段智能截取",
    description: "本地识别人物咬水果的关键瞬间，自动导出约 2.2 秒试吃片段，视频无需上传云端。"
  },
  "prompt-pocket": { title: "提示词口袋", description: "个人提示词管理与案例素材库。" },
  "feed-video-organizer": { title: "视频素材整理工具", description: "整理信息流视频素材，辅助内容生产与归档。" },
  "auto-video-mixer": { title: "自动视频混剪工具", description: "Windows 桌面端自动视频混剪工具。" },
  "video-mixer": { title: "智能视频混剪", description: "视频智能随机混剪与预览剪辑工具。" },
  "ai-mock-interview": { title: "AI 模拟面试", description: "使用 AI 进行模拟面试与回答练习。" },
  "metatone-lab": { title: "元音实验室", description: "把绘画内容转化为歌词与歌曲的 AI 跨媒介实验。" },
  "algorithmic-touch": { title: "算法触摸", description: "皮肤病图像分类与辅助识别实验。" },
  "idiomix": { title: "尾词接龙", description: "通过成语结尾词衔接下一条成语的聊天机器人。" }
};

function projectText(repo) {
  const preset = projectCopy[repo.name.toLowerCase()];
  if (preset) return preset;

  const descriptions = (repo.description || "")
    .split(/\s*\/\s*/)
    .map(text => text.trim())
    .filter(Boolean);
  const chineseDescription = descriptions.find(text => /[\u3400-\u9fff]/.test(text));

  return {
    title: repo.name.replace(/[-_]+/g, " "),
    description: chineseDescription || repo.description || "暂无项目介绍，点击卡片查看仓库详情。"
  };
}

function formatDate(date) {
  return new Intl.DateTimeFormat("zh-CN", { year: "numeric", month: "short" }).format(new Date(date));
}

function renderRepos(repos) {
  repoGrid.innerHTML = repos.slice(0, 6).map((repo, index) => {
    const copy = projectText(repo);
    return `
    <a class="repo-card" href="${repo.html_url}" target="_blank" rel="noreferrer" aria-label="查看 ${repo.name} 项目">
      <div class="repo-top">
        <span class="repo-index">0${index + 1}</span>
        <span class="repo-arrow" aria-hidden="true">↗</span>
      </div>
      <h3>${copy.title}<small>${repo.name}</small></h3>
      <p>${copy.description}</p>
      <div class="repo-foot">
        <span class="status">${repo.language || "Creative coding"}</span>
        <span>${formatDate(repo.pushed_at)}</span>
      </div>
    </a>
  `}).join("");
}

renderRepos(featuredRepos);

fetch("https://api.github.com/users/littlexx15/repos?per_page=100&sort=updated")
  .then(response => {
    if (!response.ok) throw new Error("GitHub API unavailable");
    return response.json();
  })
  .then(repos => {
    const currentSite = "littlexx15.github.io";
    const ordered = repos
      .filter(repo => !repo.fork && repo.name !== currentSite && !repo.archived)
      .sort((a, b) => new Date(b.pushed_at) - new Date(a.pushed_at));
    if (ordered.length) renderRepos(ordered);
  })
  .catch(() => {
    // The curated fallback above keeps the portfolio useful if GitHub is unavailable.
  });

document.querySelector("#year").textContent = new Date().getFullYear();
