# 多代理小说创作系统 | Multi-Agent Novel Writing System

## Overview

这是一个 10-agent 协作式小说创作框架，结合了：
- **透明内心独白**：每个代理记录 5 幕内部对话，决策过程完全可见和可追踪
- **严格交接协议**：代理间的 YAML 交接文件经过版本化、二进制验证（仅 YES/NO）
- **状态机工作流**：`plan → research → design → write → review → publish → done`
- **文件系统作为外部记忆**：结构化目录在代理调用间持久化所有状态
- **工程级质量控制**：12 项量化指标，必须全部 PASS 才能交付

## Core Features

### 10 Specialized Agents

| Agent | Role | Personality |
|-------|------|-------------|
| **Coordinator** | Project Manager | "Let me clarify priorities first." |
| **Researcher** | Research Expert | "But what's the source for that data?" |
| **WorldBuilder** | Setting Architect | "What's the atmospheric logic of this world?" |
| **CharacterDesigner** | Character Creator | "What does she fear most, and why?" |
| **PlotDesigner** | Story Architect | "The reader's mental journey should be..." |
| **Writer** | Content Creator | "This scene is too interesting to rush!" |
| **ContinuityChecker** | Logic Guardian | "Hold on — the timeline doesn't add up." |
| **SensitivityReader** | Sensitivity Reviewer | "Could this read as a harmful stereotype?" |
| **Editor** | Quality Gatekeeper | "This could be better. Here's exactly why." |
| **Publisher** | Final Ambassador | "Let me check every item on the list." |

### Key Design Principles

1. **Transparent Inner Monologue**：每个代理的思考过程被记录为 5 幕剧本，包括角色介绍、输入观察、内心独白、决策过程和行动执行
2. **Binary Handoff Protocol**：代理间的交接是严格的 YES/NO 验证，100% 通过才能继续
3. **State Machine Workflow**：工作流程分为 7 个阶段，每个阶段有明确的输入、处理和输出
4. **File System Memory**：所有状态和数据都存储在文件系统中，支持版本控制和历史追溯
5. **Quantitative Quality Control**：12 项量化指标，包括故事完整性、字数、对话比例、角色弧线等

## Usage

### Prerequisites

- Python 3.8+
- Claude Code CLI 工具
- 稳定的网络连接（用于调研）

### Installation

1. 克隆仓库：
   ```bash
   git clone https://github.com/Jack5316/novel-agent.git
   cd novel-agent
   ```

2. 运行初始化脚本：
   ```bash
   bash novel-agent/scripts/setup.sh
   ```

3. 确保代理定义文件已安装到 `.claude/agents/` 目录：
   ```bash
   ls -la .claude/agents/
   ```

### Quick Start

使用 `/start-novel` 命令启动小说创作流程：

```bash
/start-novel [theme]
```

**Example themes:**
- `2025年，AI冲击下，一个33岁程序员的求生故事`
- `A nurse navigating the collapse of her hospital during a pandemic`
- `一个在北京漂泊十年的外来务工者，面对房价和家庭压力的人生选择`

### Output

最终的小说将生成在 `out/novel_final.md` 文件中，同时会有：
- `state/LOG.md`：完整的执行日志，包含每个代理的内心独白
- `out/checklist.json`：12 项质量指标的审计结果

## Project Structure

```
novel-agent/
├── CLAUDE.md              # 项目详细文档和工作流程
├── README.md              # 项目简介（本文档）
├── .claude/
│   └── agents/            # 10个代理的定义文件
├── novel-agent/
│   ├── SKILL.md           # 技能定义文件
│   ├── references/        # 代理的详细指令
│   ├── assets/            # 项目模板文件
│   └── scripts/           # 初始化脚本
├── templates/             # 项目模板文件的副本
├── scripts/               # 其他脚本文件
├── state/                 # 项目状态文件
├── bible/                 # 世界观设定和规则
├── facts/                 # 事实卡片
├── characters/            # 角色档案和关系图
├── beats/                 # 情节结构和场景卡片
├── continuity/            # 连续性检查和伏笔线索
├── draft/                 # 草稿文件
└── out/                   # 最终输出文件
```

## Architecture

### 15-Step Workflow

1. **Plan**：协调者进行素材审计和技术规范制定
2. **Research**：研究者收集事实卡片
3. **Design**：角色设计、情节设计和世界观构建
4. **Write**：作家创作完整草稿并精炼
5. **Review**：连续性检查、敏感性阅读和编辑
6. **Publish**：出版者进行最终交付
7. **Done**：项目完成

### File System as External Memory

项目使用文件系统作为外部记忆，所有状态和数据都存储在结构化的目录中：
- `state/`：保存项目的当前状态和执行日志
- `bible/`：定义世界观、规则和风格指南
- `facts/`：收集的事实卡片
- `characters/`：角色档案和关系图
- `beats/`：情节结构和场景卡片
- `continuity/`：连续性检查和伏笔线索
- `draft/`：草稿文件
- `out/`：最终输出文件

## Quality Metrics

项目定义了 12 项量化质量指标，必须全部 PASS 才能交付：

| ID | Metric | Threshold |
|----|--------|-----------|
| M01 | Story Completeness | 3–6 chapters, each ≥5 paragraphs |
| M02 | Word Count | ≥20,000 words |
| M03 | Dialogue Ratio | 25%–35% |
| M04 | Character Arc | All main characters (≥3) have documented arc |
| M05 | Fact Accuracy | ≥30 cards, all HIGH/MEDIUM confidence |
| M06 | Foreshadowing System | ≥12 threads, all resolved |
| M07 | Continuity | 0 errors |
| M08 | Sensitivity | 0 flagged items |
| M09 | Theme Resonance | Present in 100% of chapters |
| M10 | Technical Accuracy | 100% claims verified |
| M11 | Style Consistency | 0 POV/tense violations |
| M12 | Scene Saturation | ≥3 sensory details per key scene |

## Contributing

欢迎贡献代码和改进建议！请遵循以下流程：
1. Fork 项目
2. 创建新分支
3. 进行修改
4. 提交并创建 PR
5. 等待审核

## License

MIT License

## Acknowledgments

- [Claude Code](https://claude.ai/code)：提供代理执行环境
- [Anthropic API](https://console.anthropic.com/)：提供模型支持

## Contact

如有问题或建议，请通过以下方式联系：
- GitHub Issues：https://github.com/Jack5316/novel-agent/issues
- Email：your.email@example.com
