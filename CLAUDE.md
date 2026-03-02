# 多代理小说创作系统 | Multi-Agent Novel Writing System

## Overview

This is a 10-agent collaborative novel writing framework that combines:
- **Transparent Inner Monologue**: Every agent records a 5-act internal dialogue so decisions are visible and traceable
- **Strict Handoff Protocol**: Versioned, binary-validated (YES/NO only) YAML handoffs between agents
- **State Machine Workflow**: `plan → research → design → write → review → publish → done`
- **File System as External Memory**: Structured directories persist all state across agent calls
- **Engineering-Grade Quality Control**: 12 quantified metrics that must all PASS before delivery

## The Agent Team

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

## Slash Command

When a user types `/start-novel [theme]`, execute the following orchestration:

```
/start-novel [theme description]
```

**Examples:**
- `/start-novel 2025年，AI冲击下，一个33岁程序员的求生故事`
- `/start-novel A 40-year-old nurse navigating the collapse of her hospital during a pandemic`
- `/start-novel 一个在北京漂泊十年的外来务工者，面对房价和家庭压力的人生选择`

---

## ORCHESTRATION PROTOCOL

When `/start-novel [theme]` is invoked, YOU (the main Claude session) are the **Orchestrator**. Execute the following 15-step workflow by invoking subagents in sequence. Do NOT proceed to the next step until all gate conditions for the current step are verified.

### STEP 00 — Initialize Project Structure
**Execute directly (no subagent needed):**

Create the following directory and file structure:
```
state/
  STATUS.yaml         ← Copy from templates/STATUS.yaml.template, fill in theme
  LOG.md              ← Initialize with header only
  MATERIAL_AUDIT.md   ← Empty, to be filled by Coordinator
  HANDOFF_QUEUE.yaml  ← Empty handoff registry
bible/
  world.md            ← Empty
  rules.md            ← Empty
  style.md            ← Empty
facts/
  research_cards.md   ← Empty
characters/
  profiles.md         ← Empty
  relationships.md    ← Empty
beats/
  structure.md        ← Empty
  scenes.md           ← Empty
continuity/
  checks.md           ← Empty
  threads.json        ← Initialize as empty array []
draft/
  (empty, chapters go here as chapter_01.md, chapter_02.md, etc.)
out/
  checklist.json      ← Copy from templates/checklist.json.template
  novel_final.md      ← Empty, final destination
```

Initialize `state/STATUS.yaml` with phase `plan` and status `in_progress`.
Initialize `state/LOG.md` with:
```
# Novel Agent System — Execution Log
# Project: [theme]
# Started: [timestamp]
# ============================================
```

### STEP 01 — Coordinator: Material Audit & Project Brief
**Invoke: Coordinator subagent**

The Coordinator audits the user's theme, creates `state/MATERIAL_AUDIT.md`, identifies research gaps, and sets the project brief. Updates `state/STATUS.yaml`.

**Gate G1 — before proceeding:**
- [ ] `state/MATERIAL_AUDIT.md` exists and has content
- [ ] Research gaps are listed (minimum 8 directions)
- [ ] Core tension/theme is articulated in one sentence
- [ ] Coordinator handoff in `state/HANDOFF_QUEUE.yaml` is COMPLETED

### STEP 02 — Coordinator: Technical Specifications
**Invoke: Coordinator subagent**

Lock the technical specs: POV, tense, tone, forbidden word list, target word count, chapter count. Write to `bible/rules.md`.

**Gate G2 — before proceeding:**
- [ ] `bible/rules.md` exists with all 6 spec fields filled
- [ ] Forbidden word list has ≥10 items
- [ ] Handoff status: COMPLETED

### STEP 03 — Researcher: Fact Research
**Invoke: Researcher subagent**

Collect ≥30 fact cards covering: technology, economics, geography, culture, psychology, industry specifics relevant to the theme. Write to `facts/research_cards.md`. All facts must have verifiable sources (not hallucinated).

**Gate G3 — before proceeding:**
- [ ] `facts/research_cards.md` has ≥30 numbered fact cards
- [ ] Each card has: fact, source category, confidence level (HIGH/MEDIUM)
- [ ] No fact card has confidence level LOW
- [ ] Handoff status: COMPLETED

### STEP 04 — CharacterDesigner: Character Profiles
**Invoke: CharacterDesigner subagent**

Create ≥3 main characters and ≥3 supporting characters. Each character needs: name, age, background, core fear, character arc, signature phrase, and physical anchor (one vivid physical detail). Write to `characters/profiles.md` and `characters/relationships.md`.

**Gate G4 — before proceeding:**
- [ ] ≥3 main characters with all required fields
- [ ] ≥3 supporting characters
- [ ] Character relationship map in `characters/relationships.md`
- [ ] Each main character has a documented arc trajectory
- [ ] Handoff status: COMPLETED

### STEP 05 — PlotDesigner: Story Structure
**Invoke: PlotDesigner subagent**

Design a 4-chapter structure with key beats: inciting incident, catalyst, midpoint reversal, dark night of the soul, final transformation. Write to `beats/structure.md`.

**Gate G5 — before proceeding:**
- [ ] 4 chapters defined with title and purpose
- [ ] Each chapter has ≥5 key beats documented
- [ ] Arc trajectory matches character arcs from Step 04
- [ ] Handoff status: COMPLETED

### STEP 06 — PlotDesigner: Scene Design + Foreshadowing
**Invoke: PlotDesigner subagent**

Design ≥20 scenes using Goal-Conflict-Result (GCR) pattern. Set up ≥12 foreshadowing threads in `continuity/threads.json`. Write scenes to `beats/scenes.md`.

**Gate G6 — before proceeding:**
- [ ] ≥20 scenes documented with GCR pattern
- [ ] `continuity/threads.json` has ≥12 foreshadowing threads
- [ ] Each thread has: setup chapter, setup paragraph description, activation point, resolution point
- [ ] Handoff status: COMPLETED

### STEP 07 — WorldBuilder + CharacterDesigner: World & Style
**Invoke: WorldBuilder subagent, then CharacterDesigner subagent**

WorldBuilder creates the setting bible: geography, atmosphere, socioeconomic context, sensory palette. Write to `bible/world.md`.

CharacterDesigner creates a style guide with 3 sample paragraphs demonstrating tone. Write to `bible/style.md`.

**Gate G7 — before proceeding:**
- [ ] `bible/world.md` has: setting, atmosphere, sensory palette, 5 specific location descriptions
- [ ] `bible/style.md` has ≥3 sample paragraphs (≥150 words each)
- [ ] Both handoffs: COMPLETED

### STEP 08 — Writer: Full Draft ("Write Everything")
**Invoke: Writer subagent**

Write all chapters without word limits. Goal: ≥25,000 words total. Each chapter goes in `draft/chapter_0N.md`. Do not self-edit. Write rich, then we refine.

**Gate G8 — before proceeding:**
- [ ] All 4 chapters exist in `draft/`
- [ ] Total word count ≥25,000 words (verify with actual count)
- [ ] Each chapter ≥5 paragraphs
- [ ] Dialogue ratio is in range 20%-45% (loose check here, tightened in Step 10)
- [ ] Handoff status: COMPLETED

### STEP 09 — ContinuityChecker: Logic & Timeline Audit
**Invoke: ContinuityChecker subagent**

Find and document all continuity errors: timeline gaps, contradictory facts, name inconsistencies, data mismatches. Write findings to `continuity/checks.md`. Fix all errors directly in the draft files.

**Gate G9 — before proceeding:**
- [ ] `continuity/checks.md` documents every error found (0 is acceptable if truly clean)
- [ ] All documented errors have been fixed in the draft
- [ ] All ≥12 foreshadowing threads from threads.json have their activation points confirmed
- [ ] Handoff status: COMPLETED

### STEP 10 — Writer: Refinement ("Extract the Best")
**Invoke: Writer subagent**

Trim redundancy. Strengthen key scenes. Target: final word count ≥20,000 words. Ensure dialogue ratio 25-35%. Update draft files in place.

**Gate G10 — before proceeding:**
- [ ] Total word count ≥20,000 words
- [ ] Dialogue ratio 25%-35%
- [ ] Each chapter improved (not just cut)
- [ ] Handoff status: COMPLETED

### STEP 11 — SensitivityReader: Sensitivity Review
**Invoke: SensitivityReader subagent**

Scan for: harmful stereotypes, offensive portrayals, factual misrepresentation of real groups. Log findings and required changes to `continuity/checks.md`. Apply all changes to draft.

**Gate G11 — before proceeding:**
- [ ] All flagged items have been resolved
- [ ] No banned portrayals remain
- [ ] Handoff status: COMPLETED

### STEP 12 — Editor: Theme Reinforcement
**Invoke: Editor subagent**

Verify core theme appears in every chapter. Strengthen weak theme moments. Document changes in `state/LOG.md`.

**Gate G12 — before proceeding:**
- [ ] Core theme present in 100% of chapters (with specific evidence)
- [ ] Handoff status: COMPLETED

### STEP 13 — Editor: Technical Fact Verification
**Invoke: Editor subagent**

Cross-reference every technical claim in the draft against `facts/research_cards.md`. Flag any claim not backed by a fact card. Fix or remove unsupported claims.

**Gate G13 — before proceeding:**
- [ ] 100% of technical claims traced to fact cards
- [ ] No unsupported technical claims remain
- [ ] Handoff status: COMPLETED

### STEP 14 — Editor: 12-Metric Quality Audit
**Invoke: Editor subagent**

Evaluate all 12 quality metrics in `out/checklist.json`. Every metric must be PASS. Any FAIL triggers a targeted fix + re-check before proceeding.

**Gate G14 — before proceeding:**
- [ ] All 12 metrics in `out/checklist.json` show status: PASS
- [ ] Handoff status: COMPLETED

### STEP 15 — Publisher: Final Delivery
**Invoke: Publisher subagent**

Compile all chapters into `out/novel_final.md`. Do a final 8-point user-experience check. Update `state/STATUS.yaml` to `done`. Log the final summary.

**Gate G15 (Final) — mission complete when:**
- [ ] `out/novel_final.md` exists with complete novel
- [ ] Word count verified ≥20,000 words
- [ ] `state/STATUS.yaml` phase is `done`
- [ ] Final summary logged to `state/LOG.md`

---

## INNER MONOLOGUE PROTOCOL (All Agents Must Follow)

Every agent MUST append the following 5-act structure to `state/LOG.md` at the START of their work and then complete it at the END. Use append mode — NEVER overwrite the log.

```markdown
---
## [AGENT_NAME] | [STEP_NUMBER] | [TIMESTAMP]

### Act 1 — Character Introduction
I am [Agent Name], [role]. My task today is: [specific task from orchestrator].

### Act 2 — Input Observation
I see the following materials available:
- [list what exists in state files, what was handed off]
- Current project status: [from STATUS.yaml]
- Relevant files: [list]

### Act 3 — Inner Monologue
[Real thinking. Deliberations. Considerations. What's hard about this task. What approach to take. Genuine reasoning, not just "I will do X".]

### Act 4 — Decision Process
Judgment: [decision]
Basis:
1. [reason]
2. [reason]
3. [reason]
Conclusion: [clear conclusion]

### Act 5 — Action Execution
Actions taken:
- [specific action] → [file modified/created]
- [specific action] → [file modified/created]

Handoff prepared: [YES/NO]
---
```

---

## HANDOFF PROTOCOL (All Agents Must Follow)

When an agent completes its work, it MUST append a handoff record to `state/HANDOFF_QUEUE.yaml`:

```yaml
- handoff_id: "[AGENT]_[STEP]_[TIMESTAMP]"
  from: "[agent_name]"
  to: "[next_agent_or_orchestrator]"
  timestamp: "YYYY-MM-DD_HHMM_UTC"
  deliverables:
    - file: "path/to/file"
      status: COMPLETED   # ONLY: COMPLETED or BLOCKED
      version: "v1.0"
  verification:
    - item: "Description of check"
      result: YES   # ONLY: YES or NO. NEVER: maybe, approximately, mostly, etc.
    - item: "Description of check"
      result: YES
  signature: "[agent_name]_[YYYYMMDD]_[HHMM]_UTC"
  blocked_reason: null   # or specific reason string if status is BLOCKED
```

**Binary Rule**: Every `result` field must be exactly `YES` or `NO`. The following words are BANNED in verification items:
- 约 / approximately / roughly / around
- 大概 / probably / maybe / perhaps
- 基本上 / mostly / generally
- 差不多 / more or less
- 待定 / TBD / TODO (except in designated todo lists)

**100% Rule**: ALL verification items must be `YES` before handoff status is `COMPLETED`. If any item is `NO`, the handoff is `BLOCKED` and the agent must fix the issue.

**Failure Protocol**: When a handoff is BLOCKED:
1. Document which specific verification failed
2. Set `blocked_reason` to a specific explanation
3. Set `status: BLOCKED`
4. Fix the issue
5. Create a NEW handoff entry (do not modify the BLOCKED one)
6. The BLOCKED entry remains as permanent record

---

## FORBIDDEN WORDS (System-Wide)

The following words are prohibited in ALL agent outputs, log entries, and handoffs when used to express commitment or status:

| Forbidden | Use Instead |
|-----------|-------------|
| 约 / approximately (for counts) | Exact number |
| 大概 / maybe | Specific assessment |
| 基本上 / mostly | Exactly / specifically |
| 左右 / around | Precise value |
| 可能 (as promise) | Will / confirmed |
| 建议 (replacing decision) | Decision is |
| 待定 / TBD | Specific plan |

---

## FILE SYSTEM REFERENCE

```
state/
  STATUS.yaml         ← Single source of truth for workflow state
  LOG.md              ← Append-only execution log (5-act monologues + events)
  MATERIAL_AUDIT.md   ← Coordinator's input assessment
  HANDOFF_QUEUE.yaml  ← All agent handoffs (append-only)

bible/
  world.md            ← Setting, atmosphere, geography, sensory palette
  rules.md            ← POV, tense, tone, forbidden words, specs
  style.md            ← Sample paragraphs demonstrating target voice

facts/
  research_cards.md   ← Numbered fact cards (≥30) with sources

characters/
  profiles.md         ← All character profiles (main + supporting)
  relationships.md    ← Relationship map and dynamics

beats/
  structure.md        ← 4-chapter structure with key beats
  scenes.md           ← Scene cards (GCR pattern, ≥20 scenes)

continuity/
  checks.md           ← All errors found + resolution status
  threads.json        ← Foreshadowing thread registry (≥12 threads)

draft/
  chapter_01.md       ← Chapter 1 draft
  chapter_02.md       ← Chapter 2 draft
  chapter_03.md       ← Chapter 3 draft
  chapter_04.md       ← Chapter 4 draft

out/
  checklist.json      ← 12-metric quality audit (all must PASS)
  novel_final.md      ← Compiled final novel
```

---

## QUALITY METRICS REFERENCE (12 Metrics)

All metrics in `out/checklist.json` must show `"status": "PASS"` before publication.

| ID | Metric | Measurement | Threshold |
|----|--------|-------------|-----------|
| M01 | Story Completeness | Count chapters × paragraphs | 3-6 chapters, each ≥5 paragraphs |
| M02 | Word Count | `wc -w` on compiled draft | ≥20,000 words |
| M03 | Dialogue Ratio | Dialogue words / total words | 25%–35% |
| M04 | Character Arc | Verify arc for each main character | All main characters (≥3) have documented arc |
| M05 | Fact Accuracy | Cross-reference against fact cards | 30 fact cards, all HIGH/MEDIUM confidence |
| M06 | Foreshadowing System | Audit threads.json | ≥12 threads, all resolved before chapter 4 ends |
| M07 | Continuity | Check timeline, names, data | 0 continuity errors |
| M08 | Sensitivity | Scan against sensitivity checklist | 0 flagged items |
| M09 | Theme Resonance | Verify core theme per chapter | Present in 100% of chapters |
| M10 | Technical Accuracy | Trace all tech claims to fact cards | 100% of tech claims verified |
| M11 | Style Consistency | Check POV, tense, tone | 0 POV violations, 0 tense switches |
| M12 | Scene Saturation | Count sensory details per key scene | ≥3 distinct sensory details per key scene |
