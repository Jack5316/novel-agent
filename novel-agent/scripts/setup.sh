#!/usr/bin/env bash
# novel-agent setup script
# Run once in your project folder before using /novel-agent
#
# Usage:
#   bash [skill_path]/scripts/setup.sh
#   bash [skill_path]/scripts/setup.sh /path/to/project

set -e

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROJECT_DIR="${1:-$(pwd)}"

echo "novel-agent setup"
echo "skill:   $SKILL_DIR"
echo "project: $PROJECT_DIR"
echo ""

# Create directories
for d in state bible facts characters beats continuity draft out .claude/agents; do
    mkdir -p "$PROJECT_DIR/$d"
done
echo "✓ directories created"

# Install agent definitions into .claude/agents/
cp "$SKILL_DIR/references/"*.md "$PROJECT_DIR/.claude/agents/"
echo "✓ 10 agents installed to .claude/agents/"

# Initialize state files from templates (skip if already exist)
T="$SKILL_DIR/assets"

[ ! -f "$PROJECT_DIR/state/STATUS.yaml" ]        && cp "$T/STATUS.yaml.template"    "$PROJECT_DIR/state/STATUS.yaml"
[ ! -f "$PROJECT_DIR/state/LOG.md" ]             && cp "$T/LOG.md.template"         "$PROJECT_DIR/state/LOG.md"
[ ! -f "$PROJECT_DIR/out/checklist.json" ]       && cp "$T/checklist.json.template" "$PROJECT_DIR/out/checklist.json"
[ ! -f "$PROJECT_DIR/continuity/threads.json" ]  && echo "[]" > "$PROJECT_DIR/continuity/threads.json"
[ ! -f "$PROJECT_DIR/state/HANDOFF_QUEUE.yaml" ] && printf "handoffs: []\n" > "$PROJECT_DIR/state/HANDOFF_QUEUE.yaml"
echo "✓ state files initialized"

# Touch empty placeholder files
for f in state/MATERIAL_AUDIT.md \
          bible/world.md bible/rules.md bible/style.md \
          facts/research_cards.md \
          characters/profiles.md characters/relationships.md \
          beats/structure.md beats/scenes.md \
          continuity/checks.md \
          out/novel_final.md; do
    [ ! -f "$PROJECT_DIR/$f" ] && touch "$PROJECT_DIR/$f"
done
echo "✓ placeholder files created"

echo ""
echo "Ready. Open Claude Code in $PROJECT_DIR and run:"
echo ""
echo "  /novel-agent [your theme]"
