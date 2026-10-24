---
name: self-assessment
description: Assess a learner's Codex experience across the Codex How To curriculum and produce a prioritized learning path. Use when someone asks where to start, what to learn next, to assess their Codex level, or to identify knowledge gaps. Do not use for a quiz on one lesson.
---

# Codex self-assessment

Help the learner identify demonstrated experience, not confidence alone.

## Workflow

1. Read [references/assessment.md](references/assessment.md).
2. Ask whether the learner wants the quick or deep assessment. If they already
   chose a mode, do not ask again.
3. Present one small round at a time. Use the host's structured user-input UI
   when available; otherwise ask for numbered selections in plain text.
4. Treat an item as demonstrated only when the learner says they have performed
   the observable behavior described by the item.
5. Calculate the score exactly from the reference. Preserve partial results if
   the learner stops early.
6. Read [references/recommendations.md](references/recommendations.md) and build
   a path containing only gaps and requested review topics.
7. Present the score, strengths, priority gaps, and next exercise. Link to this
   repository's modules with relative paths.

## Constraints

- Do not turn product access or account availability into a skill score.
- Do not claim that checking a box proves mastery; call it self-reported
  demonstrated experience.
- Keep recommendations in curriculum dependency order.
- Do not invent commands, configuration, or module content.
- If a recommended module is still an outline, label it as upcoming and offer
  the nearest completed module instead.
- Prefer one concrete next exercise over a generic list of resources.

## Output

Use this shape:

```markdown
## Codex self-assessment

**Level:** [Foundation / Workflow builder / Advanced operator]
**Score:** [N/8 quick or N/20 deep]

### Strengths
- [Demonstrated area]

### Priority gaps
- [Gap and why it comes next]

### Personalized path
1. [Module and focused outcome]

### Start now
[One concrete exercise with a success criterion]
```

End by offering to begin the first recommended module, take a lesson quiz, or
retake the other assessment mode.
