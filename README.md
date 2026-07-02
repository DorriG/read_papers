# read-papers

一个面向 Codex 的论文精读 skill，支持单篇阅读与批量阅读，并生成结构一致、可追溯证据的 Markdown 笔记。

它会重点提取：

- 研究背景与具体任务
- 方法流程、问题形式化与核心推导
- 创新点及其相对已有工作的技术差异
- 作者承认的局限与基于证据的批判性分析
- 数据集、评价指标、对比模型、主要结果与消融实验
- 批量论文的横向对比、研究脉络与开放问题

## 安装到 Codex

克隆仓库后，将 `read-papers` 目录复制到 Codex skills 目录。

PowerShell：

```powershell
git clone https://github.com/<YOUR_GITHUB_USERNAME>/read-papers.git
Copy-Item -Recurse -Force .\read-papers\read-papers "$HOME\.codex\skills\read-papers"
```

macOS / Linux：

```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/read-papers.git
cp -R ./read-papers/read-papers "${CODEX_HOME:-$HOME/.codex}/skills/read-papers"
```

重新打开 Codex 会话后即可显式调用 `$read-papers`。请在发布仓库后将示例 URL 中的 `<YOUR_GITHUB_USERNAME>` 替换为真实 GitHub 用户名。

## 使用示例

```text
$read-papers 精读这篇 PDF，重点解释核心公式推导，并生成中文 Markdown 笔记。
```

```text
$read-papers 批量阅读这个目录下的论文，为每篇生成笔记，再输出横向对比与推荐阅读顺序。
```

```text
$read-papers 比较这些 DOI 对应论文的方法、数据集、指标、基线与局限，合并输出为 review.md。
```

默认情况下，单篇任务生成一份 Markdown；批量任务生成每篇独立笔记和一个 `index.md` 综合报告。所有无法确认或论文未报告的信息都会被明确标记。

## 仓库结构

```text
read-papers/
├── README.md
├── LICENSE
└── read-papers/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/
    ├── references/
    └── scripts/
```

## 开源许可

[MIT License](LICENSE)

