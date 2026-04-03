# Report

## Task Overview

For this assignment, I built a small Python prototype for drafting sales follow-up emails. The workflow is realistic because sales representatives often need to turn rough meeting notes into polished client-facing communication quickly.

## System Description

The app takes plain-text notes from the command line, sends them to a Gemini model, and returns a follow-up email. The output is printed in the terminal and also saved to `output.txt`. The prompt is configurable through the `SYSTEM_PROMPT` variable in `app.py`.

## Evaluation Approach

I created a stable evaluation set with five representative cases:

- one normal case with clear customer and meeting details
- one edge case with missing information
- one likely failure case with unclear notes
- one detailed enterprise-style case
- one case with ambiguous next steps

For each case, I defined what a good output should do so the system can be judged consistently.

## What Improved During Iteration

My initial prompt only asked for a polite follow-up email. After reviewing the assignment goals, I revised the prompt to make the task more reproducible and reliable. The final prompt now tells the model to:

- use a professional business tone
- include a subject line
- summarize only the information provided
- avoid inventing names, pricing, or product details
- stay generic when information is missing
- acknowledge uncertainty when the notes are unclear

These changes were intended to reduce hallucination and make the outputs easier to evaluate honestly.

## Strengths

- The prototype is simple and easy to run from the command line.
- It makes a real LLM API call.
- It supports prompt iteration through a configurable system prompt.
- It handles incomplete inputs more safely than the initial version.
- It saves results to a file, which helps with reproducibility.

## Limitations

- The quality still depends on the quality of the user notes.
- The model may still produce wording that needs human review before sending.
- The app does not automatically score outputs, so evaluation is still manual.
- It requires an API key to reproduce the results.

## Conclusion

This prototype demonstrates a narrow business writing workflow clearly: converting rough sales notes into a usable follow-up email draft. It is not a production system, but it satisfies the assignment goal of making real LLM calls, evaluating outputs against a stable set of cases, and improving results through prompt iteration.
