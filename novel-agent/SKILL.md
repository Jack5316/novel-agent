---
name: novel-agent
description: 10代理协作写小说；从一句话主题生成2万字小说，包含调研/人物/情节/世界观/写作/校对/发布全流程；用户想写小说、生成故事或提及多代理写作时使用
dependency:
  python:
    - pyyaml>=6.0
---

# Novel Agent - 多代理小说创作系统

## 任务目标
- **核心能力**：10代理协作，将一句话主题转化为2万字以上完整小说
- **交付物**：`out/novel_final.md` + `state/LOG.md`（透明日志）
- **触发场景**：用户想写小说、创作长篇 fiction、生成故事、提及"多代理写小说"等

## 启动命令
```
/novel-agent [主题]
```

**示例主题**：
- `2025年，AI冲击下，一个33岁程序员的求生故事`
- `一个在北京漂泊十年的外来务工者，面对房价和家庭压力的人生选择`

## 工作流程（15步骤，6阶段）

| 阶段 | 步骤 | 代理 | 产出 |
|------|------|------|------|
| Plan | 01-02 | coordinator | MATERIAL_AUDIT.md, rules.md |
| Research | 03 | researcher | research_cards.md (≥30条事实) |
| Design | 04, 07b | character_designer | profiles.md, relationships.md, style.md |
| Design | 05-06 | plot_designer | structure.md, scenes.md, threads.json |
| Design | 07a | world_builder | world.md |
| Write | 08, 10 | writer | chapter_01-04.md (≥2万字) |
| Write | 09 | continuity_checker | checks.md (0错误) |
| Review | 11 | sensitivity_reader | 敏感性检查通过 |
| Review | 12-14 | editor | 12项质量指标全部PASS |
| Publish | 15 | publisher | novel_final.md |

## 守门条件（Gates）

| Gate | 条件 |
|------|------|
| G1 | MATERIAL_AUDIT存在，≥8个研究方向，核心张力明确 |
| G2 | rules.md全部6字段填写，禁用词≥10条 |
| G3 | ≥30事实卡片，全部HIGH/MEDIUM，≥5类别 |
| G4 | ≥3主角+≥3配角，全部字段填写 |
| G5 | 4章节，≥5 beats/章，弧线匹配人物 |
| G6 | ≥20场景，≥12伏笔线索 |
| G7a | ≥5地点，多感官细节 |
| G7b | ≥3样本段落，风格一致 |
| G8 | 4章节存在，≥2.5万字 |
| G9 | 0错误，≥12伏笔确认 |
| G10 | ≥2万字，对话25-35% |
| G11 | 0敏感性标志PASS |
| G12 | 全部章节主题存在ADEQUATE+ |
| G13 | 100%事实核实 |
| G14 | 12项指标PASS |

## 质量指标

| ID | 指标 | 阈值 |
|----|------|------|
| M01 | 故事完整性 | 3-6章节，每章≥5段落 |
| M02 | 字数 | ≥20,000 |
| M03 | 对话比例 | 25%-35% |
| M04 | 人物弧线 | ≥3主角有文档 |
| M05 | 事实准确性 | ≥30卡片，全HIGH/MEDIUM |
| M06 | 伏笔 | ≥12线索全部回收 |
| M07 | 连贯性 | 0错误 |
| M08 | 敏感性 | 0标志 |
| M09 | 主题共鸣 | 100%章节存在 |
| M10 | 技术准确性 | 100%核实 |
| M11 | 风格一致性 | 0 POV/时态/禁用词违规 |
| M12 | 场景饱和度 | 每关键场景≥3种感官 |

## 初始化（首次使用）

```bash
bash scripts/setup.sh [项目路径]
```

## 内心独角戏协议

每个代理每次执行需追加到 `state/LOG.md`：

```markdown
## [AGENT_NAME] | STEP [N] | [TIMESTAMP]
### Act 1 - Character Introduction
### Act 2 - Input Observation
### Act 3 - Inner Monologue
### Act 4 - Decision Process
### Act 5 - Action Execution
Handoff prepared: YES
```

## 交接协议

追加到 `state/HANDOFF_QUEUE.yaml`：
- `status: COMPLETED` 或 `BLOCKED`（仅二值）
- `result: YES` 或 `NO`（禁止模糊）

## 禁用词

禁止：约、大概、基本上、左右、可能（承诺）、建议（决策）、待定

## 资源索引

- 脚本：[scripts/setup.sh](scripts/setup.sh)（初始化项目结构）
- 脚本：[scripts/md_to_pdf.py](scripts/md_to_pdf.py)（可选：Markdown转PDF）
- 代理配置：见 `.claude/agents/`
- 参考文档：见 [references/](references/)
  - [coordinator.md](references/coordinator.md) - 步骤01-02
  - [researcher.md](references/researcher.md) - 步骤03
  - [character_designer.md](references/character_designer.md) - 步骤04, 07b
  - [plot_designer.md](references/plot_designer.md) - 步骤05-06
  - [world_builder.md](references/world_builder.md) - 步骤07a
  - [writer.md](references/writer.md) - 步骤08, 10
  - [continuity_checker.md](references/continuity_checker.md) - 步骤09
  - [sensitivity_reader.md](references/sensitivity_reader.md) - 步骤11
  - [editor.md](references/editor.md) - 步骤12-14
  - [publisher.md](references/publisher.md) - 步骤15
- 模板：见 [assets/](assets/)
  - [STATUS.yaml.template](assets/STATUS.yaml.template)
  - [LOG.md.template](assets/LOG.md.template)
  - [checklist.json.template](assets/checklist.json.template)

## 文件结构

```
state/     STATUS.yaml, LOG.md, MATERIAL_AUDIT.md, HANDOFF_QUEUE.yaml
bible/     world.md, rules.md, style.md
facts/     research_cards.md
characters/ profiles.md, relationships.md
beats/     structure.md, scenes.md
continuity/ checks.md, threads.json
draft/     chapter_01.md ... chapter_04.md
out/       checklist.json, novel_final.md
```
