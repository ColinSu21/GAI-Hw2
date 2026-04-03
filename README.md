# Sales Follow-Up Email Prototype

## Workflow

This project focuses on drafting sales follow-up emails after an initial customer interaction such as a meeting, discovery call, or product demo.

## User

The primary user is a sales representative who needs a fast first draft after speaking with potential clients.

## Input

The system receives short notes that may include:

- customer name
- company name
- context of the interaction
- key points discussed
- next steps or timing

## Output

The system produces a professional follow-up email with a subject line and body. The email should summarize the conversation, reinforce relevant points, and suggest a reasonable next step without inventing missing details.

## Value of Automation

This task is valuable to automate because it is repetitive, time-sensitive, and important for maintaining customer relationships. A strong first draft saves time, improves consistency, and still leaves room for human review before sending.

## Reproducibility

1. Install the Google Generative AI Python package.
2. Set `GOOGLE_API_KEY` or `GEMINI_API_KEY` in your shell.
3. Run `python3 app.py`.
4. Paste meeting notes into the terminal and press Enter on an empty line to finish.
5. The generated email is printed and also saved to `output.txt`. And the video link is https://youtu.be/Pqssy-EDiGk. 
