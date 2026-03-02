---
name: novel-agent
description: |
  Orchestrates a 10-agent pipeline that writes a full-length novel (≥20,000 words) from a one-line theme.
  Use this skill whenever the user wants to write a novel, create long-form fiction, generate a story from a theme,
  or mentions "multi-agent novel", "AI novel", "用多代理写小说", "write me a novel", "create fiction with agents",
  "story from one sentence", or any request for structured fiction with research, plotting, continuity checking,
  and quality verification — even if they don't explicitly say "novel-agent" or "multi-agent".
  The pipeline runs plan → research → design → write → review → publish, producing out/novel_final.md
  with a transparent inner-monologue log in state/LOG.md.
compatibility: subagents (mcp_task or equivalent) for invoking the 10 specialized agents
---

# Novel Agent — 多代理小说创作系统

A 10-agent collaborative system that turns a one-line theme into a ≥20,000-word novel. Each agent logs a 5-act inner monologue so every decision is visible and traceable.

## Skill Anatomy

```
novel-agent/
├── SKILL.md           ← You are here
├── scripts/setup.sh   ← Run once to initialize project structure
├── references/        ← Per-agent instructions (read when invoking that agent)
│   ├── coordinator.md
│   ├── researcher.md
│   ├── character_designer.md
│   ├── plot_designer.md
│   ├── world_builder.md
│   ├── writer.md
│   ├── continuity_checker.md
│   ├── sensitivity_reader.md
│   ├── editor.md
│   └── publisher.md
└── assets/            ← Templates (used by setup.sh)
    ├── STATUS.yaml.template
    ├── LOG.md.template
    └── checklist.json.template
```

## Invocation

```
/novel-agent [theme]
```

**Example themes:**
- `2025年，AI冲击下，一个33岁程序员的求生故事`
- `A nurse navigating the collapse of her hospital during a pandemic`
- `一个在北京漂泊十年的外来务工者，面对房价和家庭压力的人生选择`

---

## Setup (First Time Only)

Run the setup script to create the directory structure and install agent definitions:

```bash
bash [skill_path]/scripts/setup.sh [project_path]
```

This creates `state/ bible/ facts/ characters/ beats/ continuity/ draft/ out/` and copies the 10 agent files into `.claude/agents/`. If `setup.sh` is unavailable, see **Manual Setup** at the end.

---

## Orchestration Overview

When `/novel-agent [theme]` is invoked, you are the **Orchestrator**. Execute each step by invoking the named subagent. Do not advance until all gate conditions for that step pass.

| Phase | Steps | Agent | Read this reference when invoking |
|-------|-------|-------|-----------------------------------|
| Plan | 01–02 | coordinator | `references/coordinator.md` |
| Research | 03 | researcher | `references/researcher.md` |
| Design | 04, 07b | character_designer | `references/character_designer.md` |
| Design | 05–06 | plot_designer | `references/plot_designer.md` |
| Design | 07a | world_builder | `references/world_builder.md` |
| Write | 08, 10 | writer | `references/writer.md` |
| Write | 09 | continuity_checker | `references/continuity_checker.md` |
| Review | 11 | sensitivity_reader | `references/sensitivity_reader.md` |
| Review | 12–14 | editor | `references/editor.md` |
| Publish | 15 | publisher | `references/publisher.md` |

---

## 15-Step Workflow (Summary)

### Phase 1 — Plan (Steps 01–02)

**Step 01 · coordinator** — Read the theme. Create `state/MATERIAL_AUDIT.md` with core tension (one sentence), ≥8 research gaps, research authorization. Update `state/STATUS.yaml`.

Gate G1: MATERIAL_AUDIT exists, ≥8 gaps, core tension articulated, authorization explicit.

**Step 02 · coordinator** — Create `bible/rules.md`: POV, tense, tone, ≥10 forbidden words with reasons, target word count, chapter count.

Gate G2: All 6 spec fields filled, forbidden list ≥10 entries.

### Phase 2 — Research (Step 03)

**Step 03 · researcher** — Collect ≥30 fact cards into `facts/research_cards.md`. Each card: fact, source category, confidence (HIGH or MEDIUM only), story relevance.

Gate G3: ≥30 cards, all HIGH/MEDIUM, ≥5 categories.

### Phase 3 — Design (Steps 04–07)

**Step 04 · character_designer** — Create `characters/profiles.md` (≥3 main + ≥3 supporting) and `characters/relationships.md`.

Gate G4: All character fields, arcs documented.

**Step 05 · plot_designer** — Create `beats/structure.md`: 4 chapters, ≥5 beats each, arc table.

Gate G5: 4 chapters, ≥5 beats each, arc table matches profiles.

**Step 06 · plot_designer** — Create `beats/scenes.md` (≥20 GCR scenes) and `continuity/threads.json` (≥12 foreshadowing threads).

Gate G6: ≥20 scenes, ≥12 threads with setup/reinforcement/activation/payoff.

**Step 07a · world_builder** — Create `bible/world.md`: setting, atmosphere, sensory palette, ≥5 location descriptions.

Gate G7a: ≥5 locations with multi-sensory detail.

**Step 07b · character_designer** — Create `bible/style.md`: 4 voice principles, ≥3 sample paragraphs (≥150 words each).

Gate G7b: ≥3 samples, consistent with rules.md tone.

### Phase 4 — Write (Steps 08–10)

**Step 08 · writer** — Read all bible, character, beats, continuity files. Write `draft/chapter_01.md` through `chapter_04.md`. Target ≥25,000 words. Weave foreshadowing naturally.

Gate G8: All 4 chapters exist, total ≥25,000 words, each ≥5 paragraphs.

**Step 09 · continuity_checker** — Build master timeline. Check consistency, fact cross-reference, foreshadowing setups. Document errors in `continuity/checks.md`. Fix all in draft.

Gate G9: 0 errors remaining, all ≥12 thread setups confirmed.

**Step 10 · writer** — Cut redundancy, strengthen key scenes. Target ≥20,000 words, dialogue ratio 25–35%.

Gate G10: ≥20,000 words, dialogue 25–35%, clear character change per chapter.

### Phase 5 — Review (Steps 11–14)

**Step 11 · sensitivity_reader** — Scan for stereotyping, trauma spectacle, harmful language. Document in `continuity/checks.md`. Apply fixes.

Gate G11: 0 flags remaining, verdict PASS.

**Step 12 · editor** — Grade theme presence per chapter (STRONG/ADEQUATE/WEAK/ABSENT). Strengthen WEAK/ABSENT through character action or image.

Gate G12: All chapters ADEQUATE or STRONG.

**Step 13 · editor** — Trace every technical claim to `facts/research_cards.md`. Remove or fix unverified claims.

Gate G13: 100% verified or common knowledge.

**Step 14 · editor** — Evaluate all 12 metrics in `out/checklist.json`. Fix any FAIL until all PASS.

Gate G14: All 12 metrics PASS.

### Phase 6 — Publish (Step 15)

**Step 15 · publisher** — Compile `out/novel_final.md`. Run 8-point delivery check. Update STATUS to done. Write final summary to LOG.md.

**8-Point Delivery Check:** (1) novel_final exists with all 4 chapters, (2) word count ≥20,000 verified, (3) chapter titles match structure, (4) no artifacts, (5) all 12 metrics PASS, (6) HANDOFF_QUEUE has all agents, (7) LOG complete, (8) final chapter ends story.

---

## Critical Protocols

### Inner Monologue (Every Agent, Every Step)

Append this 5-act structure to `state/LOG.md` before and after work. The log is append-only — never overwrite or delete.

```markdown
---
## [AGENT_NAME] | STEP [N] | [TIMESTAMP]
### Act 1 — Character Introduction
### Act 2 — Input Observation
### Act 3 — Inner Monologue
### Act 4 — Decision Process
### Act 5 — Action Execution
Handoff prepared: YES
---
```

*Why:* The inner monologue makes decisions traceable. When something goes wrong, you can see exactly what each agent was thinking.

### Handoff Protocol (Every Agent, Every Step)

Append to `state/HANDOFF_QUEUE.yaml` after each step. Use `status: COMPLETED` or `BLOCKED` only. Use `result: YES` or `NO` only — never maybe, approximately, or mostly.

*Why:* Binary verification prevents handwaving. If any verification is NO, set status to BLOCKED, fix the issue, then create a new handoff. The Coordinator resolves BLOCKED states.

### Forbidden Words

Avoid these when expressing status, counts, or commitments: 约/approximately, 大概/maybe, 基本上/mostly, 左右/around, 可能 (as promise), 建议 (replacing decision), 待定/TBD. Use exact numbers and specific assessments instead.

---

## 12 Quality Metrics

All must show `"status": "PASS"` in `out/checklist.json` before Step 15.

| ID | Metric | Threshold |
|----|--------|-----------|
| M01 | Story Completeness | 3–6 chapters, each ≥5 paragraphs |
| M02 | Word Count | ≥20,000 words |
| M03 | Dialogue Ratio | 25%–35% |
| M04 | Character Arc | All main characters (≥3) documented |
| M05 | Fact Accuracy | ≥30 cards, all HIGH/MEDIUM |
| M06 | Foreshadowing | ≥12 threads, all resolved |
| M07 | Continuity | 0 errors |
| M08 | Sensitivity | 0 flags |
| M09 | Theme Resonance | Present in 100% of chapters |
| M10 | Technical Accuracy | 100% claims verified |
| M11 | Style Consistency | 0 POV/tense/forbidden violations |
| M12 | Scene Saturation | ≥3 sensory types per key scene |

---

## File System

```
state/     STATUS.yaml, LOG.md, MATERIAL_AUDIT.md, HANDOFF_QUEUE.yaml
bible/     world.md, rules.md, style.md
facts/     research_cards.md
characters/ profiles.md, relationships.md
beats/     structure.md, scenes.md
continuity/ checks.md, threads.json
draft/     chapter_01.md … chapter_04.md
out/       checklist.json, novel_final.md
```

---

## Manual Setup

If `scripts/setup.sh` is unavailable:

```bash
mkdir -p state bible facts characters beats continuity draft out .claude/agents
cp [skill_path]/references/*.md .claude/agents/
cp [skill_path]/assets/STATUS.yaml.template state/STATUS.yaml
cp [skill_path]/assets/LOG.md.template state/LOG.md
cp [skill_path]/assets/checklist.json.template out/checklist.json
echo "[]" > continuity/threads.json
printf "handoffs: []\n" > state/HANDOFF_QUEUE.yaml
touch state/MATERIAL_AUDIT.md bible/world.md bible/rules.md bible/style.md \
      facts/research_cards.md characters/profiles.md characters/relationships.md \
      beats/structure.md beats/scenes.md continuity/checks.md out/novel_final.md
```

---

## References (When to Read)

| Agent | File | Read when |
|-------|------|-----------|
| coordinator | `references/coordinator.md` | Invoking Steps 01–02 |
| researcher | `references/researcher.md` | Invoking Step 03 |
| world_builder | `references/world_builder.md` | Invoking Step 07a |
| character_designer | `references/character_designer.md` | Invoking Steps 04, 07b |
| plot_designer | `references/plot_designer.md` | Invoking Steps 05–06 |
| writer | `references/writer.md` | Invoking Steps 08, 10 |
| continuity_checker | `references/continuity_checker.md` | Invoking Step 09 |
| sensitivity_reader | `references/sensitivity_reader.md` | Invoking Step 11 |
| editor | `references/editor.md` | Invoking Steps 12–14 |
| publisher | `references/publisher.md` | Invoking Step 15 |
