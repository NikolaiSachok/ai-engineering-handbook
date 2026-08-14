#!/usr/bin/env bash
#
# Structural-parity gate: every translated locale must have the same SHAPE as the English source.
#
# Why this exists. Parity between locales used to be enforced only by the build, which catches a
# missing file or a dead link and nothing else. A whole defect class shipped silently: a section
# dropped in translation, a card node that never made it across, a figure that drifted. The symptom
# is always the same — the translated page is *plausible*, so no reader flags it, and the canon then
# records decisions about text no page contains. That is not hypothetical: a Slovak canon entry once
# settled the wording of a `:::note` label that existed in no page at all, and it stood for two
# phases. The build was green the whole time.
#
# So this asserts the things a translation must NOT change, and deliberately says nothing about the
# things it must. Per locale, per course tree, against the English source:
#
#   1. file set          — identical set of relative .md paths
#  1b. frontmatter      — block present in both; `id` and `sidebar_position` equal
#   2. heading shape     — identical H1/H2 count and level sequence per file
#   3. heading anchors   — identical ORDERED sequence of explicit `\{#id}` heading ids
#   4. component counts  — identical counts of `<InfoCard`, `<Node`, `<YouTube`
#  4b. admonitions      — identical ordered kinds, titled-or-not, and blank-line padding
#   5. fenced blocks     — identical count per fence language (```text excepted)
#  5b. mermaid shape     — identical layout direction, node-id set and edge count per diagram
#   6. numeric drift     — no percentage/decimal figure differing in value between the two
#
# --- Why 1b exists, added 2026-08-15 -----------------------------------------------------------
#
# This file used to strip the frontmatter and say so in a comment: the fields that must match "are
# already enforced by the build's sidebar assembly". That is true of a field that DISAGREES and
# false of a block that is ABSENT. Docusaurus infers a doc id from the path and a title from the H1,
# so a page whose frontmatter vanished still builds — it just quietly loses `sidebar_position` and
# moves in the sidebar.
#
# Measured 2026-08-15: a rebuilt Russian glossary shipped with its entire block missing, and every
# check here passed — headings, anchors, components, admonitions, fences, figures. The block is the
# one part of a page with no prose to compare, which is exactly why nothing looked at it. On its
# first corpus run 1b also caught a defect nobody had filed: `part-2-agents/real-agents.md` sat at
# `sidebar_position: 8` in English and `7` in all three translations, colliding with `mcp` — so the
# lesson's place in the sidebar differed between the English site and every translated one.
#
# Only `id` and `sidebar_position` are compared by value. `title` and `description` are translated
# by design and `slug` may localise; one of the self-test cases is the control for exactly that.
#
# --- Why 4b exists, added 2026-08-14 -----------------------------------------------------------
#
# Everything above keys on headings, components, fences or figures. An admonition is the one content
# container that has none of those: `:::note[Field note]` carries no heading, no MDX tag and no
# fence, so a whole block can vanish from a locale without moving a single thing this file measures.
# Measured against the shipped corpus: all four `Field note` blocks of the AI-SDLC course — 189
# words of first-hand material, present in English and Russian — were absent from Slovak, and a
# `:::warning` in the RAG ingestion deep dive was absent from Russian while German carried it. This
# gate passed clean on all five pages, every run, for as long as they had existed.
#
# It was found by a session-local checker built for the Russian rebuild, which is the general point:
# a gate gap is worth more than the defect that exposed it. The gap was a missing blank line on one
# page; the check written to catch it swept 66 page/locale pairs and found five missing blocks.
#
# What 4b compares is the SHAPE, never the words: the ordered sequence of kinds, whether each block
# carries a title in both locales, and the blank-line padding. Title TEXT is not compared —
# translating «:::note[Field note]» to «:::note[Из практики]» is the entire point of a locale, and
# one of the self-test cases is the anti-false-positive control for exactly that. Padding is in
# scope because it is the same defect one level down and three Russian pages had drifted that way.
#
# --- Why 5b exists, added 2026-08-03 -----------------------------------------------------------
#
# Check 5 weighs a fence; it never looks inside one. So a diagram could be authored into a
# completely different picture in one locale and every check above would still pass. Measured
# against the shipped corpus: 28 diagrams had drifted, 27 of them Russian. One rendered at
# 2 062px where its English counterpart was 635px, because two English diagrams had been merged
# into a single horizontal row. Another put the local MCP server OUTSIDE the trust boundary that
# English puts it inside — and carried a caption asserting the opposite of what English teaches.
# All of it shipped, in a corpus with six other parity checks and a full CI suite.
#
# What 5b compares is the GRAPH, never the words: layout direction (TD and TB normalised — they
# are the same axis), the set of node ids, and the edge count. Node ids are not content; they are
# the diagram's code, and holding them equal is what makes four locale files diffable. Everything
# a translator legitimately changes — every label, every edge label, every note — is stripped
# before ids are read, because label prose is full of words that look like identifiers
# (`LD["Ranked list (dense)"]` would otherwise yield a phantom node `list`). Two of the self-test
# cases are anti-false-positive controls for exactly that.
#
# --- What was relaxed, and on what evidence ----------------------------------------------------
#
# The first draft of this gate asserted the strictest form of each check and was run against the
# existing ru and sk trees before being wired into CI. It reported 128 findings across 134 files.
# Triaging them showed three of the five checks were, in their strict form, measuring wording rather
# than structure. Each was narrowed to the assertion that survived the evidence — narrowed, not
# suppressed, and never with an ignore list, because a gate people route around is worse than none.
#
# HEADINGS — strict form compared every level, H1..H6, and failed on 4 of 134 files. All four were a
# natively-authored locale subdividing its own prose with extra `###` (RU's guardrails deep-dive
# carries 19 headings against English's 10 and covers exactly the same ground). RU is audience-
# primary and written natively, not translated, so `###` pacing is an editorial choice. Restricting
# to H1/H2 left exactly one finding — and that one was real: the Slovak observability lesson had
# promoted the Part I wrap-up to an `##` heading that neither English nor Russian has. Fixed in the
# same change. H2 is the page's section contract (sidebar, right-hand TOC, the canon's book units);
# H3 is internal pacing. That is the line.
#
# FENCED BLOCKS — strict form demanded every fence be byte-identical and failed on 28 files. Two
# separate lessons came out of triage. First, ```mermaid and ```text hold PROSE: mermaid node labels
# are rendered to the reader and all eight ```text blocks are ASCII diagrams with translated
# captions, so locales redraw them, correctly. Second — and this is the one that overturned the
# check — the locales here are not translations. RU is audience-primary and written natively; SK is
# composed from English MEANING. They author their own examples: the Russian tooling-ecosystem
# deep-dive teaches the Guardrails validator API with a different validator, different error strings
# and a different `on_fail` action than English, followed by two paragraphs English does not have.
# That is editorial, not drift. So fence CONTENT is not asserted at all. What is asserted is COUNT
# per language: a dropped ```mermaid is a lost diagram, a dropped ```bash is a lost copyable command.
# ```text and unlabelled fences are exempt even from that, because a locale may inline the same
# formula (RU renders two English ```text formula blocks as inline code in a numbered list).
# The count check kept one true finding: the Russian tooling-ecosystem deep-dive had no ```bash block
# where English and Slovak both hand the reader a copyable install command. Fixed in the same change.
#
# (If the project ever decides code samples are shared verbatim across locales, byte-identity on the
# executable fences is the right check to bring back — it is unsupported by today's corpus, not wrong
# in principle.)
#
# NUMBERS — strict form compared the multiset of every numeric token and failed on 96 files. Almost
# all of it was notation, not content: "Part 2" against «Часть II», ISO dates against spelled-out
# ones, `10,000` against `10 000` with a non-breaking space, `11k` against `11 000`, `429s` (the
# plural of an HTTP status) parsed as 429 seconds. Normalising the punctuation and dropping years,
# ordinals and word-expressed magnitudes narrowed it to percentages and decimals — 8 findings, and on
# inspection all 8 were legitimate: a locale states a figure the other only implies ("a deterministic
# fraction" against «оставлять 10%") or paraphrases one away ("the roughly 50% chance would have
# handed you" against «лишь подбрасыванием монеты»). A one-sided figure is therefore a paraphrase
# decision and is COUNTED, not failed — the same tolerate-and-report shape scripts/i18n-link-check.sh
# uses. What fails is DRIFT: both sides carrying a figure of the same kind with a different value,
# which is what "20% became 25% in translation" looks like and cannot be a paraphrase.
#
# The file set and component counts were already clean on ru and sk and are asserted at full
# strictness. They are the two checks a German tree will exercise from its first translated page.
#
# HEADING ANCHORS came later (#307's companion) and needed no relaxation: it was clean on ru and sk
# from the first run. #306 gave 123 glossary headings an explicit `\{#id}` across six files, applied
# BY HEADING INDEX and checked by hand afterwards — correct exactly once. Insert one entry mid-file
# in a single locale and every id below it shifts: each id still exists, the counts still match,
# the SET is still equal, and every inbound `glossary.md#id` link into that locale now lands on the
# neighbouring entry. So the sequence is compared in ORDER, which catches the insert and the plain
# swap alike. The escaped `\{` is the on-disk form (`future.v4: true` removes the MDX1 heading-id
# escape, so a bare `{` parses as JSX and fails the build); the escape is markup, not id, and is
# stripped before comparing.
#
# PER-COURSE SCOPE. A course declares the locales it claims (`locales` in docusaurus.config.ts).
# This gate checks a course/locale pair only when the course claims it, and prints the pairs it
# skipped. The scope is a declaration, not an inference from a missing directory — absence still
# fails for a claimed locale that ships, which is the whole point of the earlier fix that stopped
# treating "no translation dir" as "this course isn't translated here". Not translating a course
# in a locale is a decision, so it is made in the config, where the landing card shows it too.
#
# Usage: scripts/locale-parity-check.sh [locale…]   (default: every locale under i18n/)
#        scripts/locale-parity-check.sh --self-test (assert the scope verdicts, no corpus needed)
# Exit code: 0 if every locale is in parity, 1 otherwise.

set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

exec python3 scripts/locale_parity.py "$@"
