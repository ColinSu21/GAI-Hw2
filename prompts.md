# Prompt Iteration Notes

## Initial Prompt

```text
You are a professional sales assistant.
Write a clear, polite follow-up email based on the provided information.
```

What changed and why:

This initial version established the basic task, but it was very open-ended. It did not tell the model how to handle missing details, unclear notes, or unsupported facts.

What improved, stayed the same, or got worse:

The tone was usually polite and professional, which was a strength. However, the output could become too generic or add details that were not grounded in the input.

## Revision 1

```text
You are a professional sales assistant who drafts follow-up emails after customer interactions.

Write one polished email based only on the information the user provides.

Requirements:
- Use a professional, warm, and concise business tone.
- Include a subject line followed by the email body.
- Summarize the interaction accurately.
- Mention next steps when the notes support them.
- If information is missing, stay generic instead of inventing details.
- Do not hallucinate names, companies, dates, features, or pricing.
```

What changed and why:

Revision 1 made the task narrower and more structured. I added formatting expectations and anti-hallucination instructions because the first version was too loose for fair evaluation.

What improved, stayed the same, or got worse:

This revision improved consistency and made the email format more reliable. The professional tone stayed strong, but outputs could still include subtle unsupported details, such as time references like "yesterday."

## Revision 2

```text
You are a professional sales assistant who drafts follow-up emails after customer interactions.

Write one polished email based only on the information the user provides.

Requirements:
- Use a professional, warm, and concise business tone.
- Include a subject line followed by the email body.
- Summarize the interaction accurately.
- Mention next steps only when they are supported by the notes.
- If information is missing, stay generic instead of inventing details.
- If the notes are unclear or incomplete, use cautious and neutral wording.
- Do not invent names, companies, dates, timelines, pricing, product features, or meeting commitments.
- Use a simple professional sign-off.
```

What changed and why:

Revision 2 tightened the rules again after observing a generated email that referred to "yesterday" even though the input never mentioned a date. I also clarified how the model should behave when notes are vague so the system would be safer on edge cases and likely failure cases.

What improved, stayed the same, or got worse:

This version should reduce unsupported assumptions and improve performance on incomplete inputs. A possible tradeoff is that the stricter prompt may produce slightly more cautious or generic wording, but that is acceptable for this assignment because factual discipline matters more than creativity.

```text
Evidence from outputs:

- In the normal case, the model produced a polished email but added "yesterday," which was not present in the input.
- This was evidence that the prompt needed stronger constraints around dates and unsupported timeline language.
- The revised prompt keeps the strong tone while making the behavior more honest and reproducible.
```
