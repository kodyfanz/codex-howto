---
name: lesson-quiz
description: Quiz a learner on one completed Codex How To module with ten sourced questions, immediate feedback, scoring, and targeted review links. Use when someone asks to be quizzed or test their knowledge of a specific lesson. Do not use for an overall level assessment or to teach a topic without testing it.
---

# Codex lesson quiz

Quiz only modules marked complete in
[references/question-bank.md](references/question-bank.md). The current bank
covers modules 1 through 10.

## Workflow

1. Resolve the requested module by number or topic. If none is provided, offer
   only modules present in the question bank.
2. Read that module's `README.md` and only its section of the question bank.
3. Ask whether this is a pre-test, progress check, or mastery check.
4. Present ten questions in five rounds of two. Use the host's structured
   user-input UI when available; otherwise use numbered plain-text options.
5. Shuffle options for each question and track the correct answer by its full
   text, not by the original letter.
6. After each round, state whether each answer was correct and explain misses.
7. Score one point per correct answer and use the grade scale below.
8. Produce the report shape in
   [references/results-template.md](references/results-template.md).

## Grade scale

- 9–10: Mastered
- 7–8: Proficient
- 5–6: Developing
- 3–4: Beginning
- 0–2: Start with the lesson

## Constraints

- Never invent questions, answers, or lesson sections.
- Stop and explain when a module has no completed question bank.
- If the learner stops, report a partial score out of questions attempted.
- Keep a question's options together and score against the tracked answer text.
- Do not expose the answer key before the learner answers.
- Tailor the final message to quiz timing without changing the score.

End by offering a retake, another completed lesson, an explanation of one missed
concept, or the next module in the learning roadmap.
