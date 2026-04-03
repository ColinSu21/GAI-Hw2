import os
from pathlib import Path

import google.generativeai as genai


MODEL_NAME = "gemini-2.5-flash"
OUTPUT_PATH = Path("output.txt")

SYSTEM_PROMPT = """
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
""".strip()


def configure_model():
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Missing API key. Please set GOOGLE_API_KEY or GEMINI_API_KEY before running app.py."
        )

    genai.configure(api_key=api_key)
    return genai.GenerativeModel(MODEL_NAME)


def build_prompt(input_text):
    return (
        f"{SYSTEM_PROMPT}\n\n"
        "User notes for the email:\n"
        f"{input_text.strip()}\n\n"
        "Return only the final email."
    )


def generate_email(input_text):
    if not input_text.strip():
        raise ValueError("Input is empty. Please provide customer notes before generating the email.")

    model = configure_model()
    response = model.generate_content(build_prompt(input_text))
    return response.text.strip()


def collect_user_input():
    print("Enter input for the follow-up email (press Enter on an empty line to finish):\n")
    lines = []

    while True:
        try:
            line = input()
        except EOFError:
            break

        if line == "":
            break

        lines.append(line)

    return "\n".join(lines).strip()


def save_output(output_text):
    OUTPUT_PATH.write_text(output_text, encoding="utf-8")


def main():
    try:
        user_input = collect_user_input()
        output = generate_email(user_input)
        print("\n=== Generated Email ===\n")
        print(output)
        save_output(output)
        print(f"\nSaved to {OUTPUT_PATH.resolve()}")
    except Exception as exc:
        print(f"\nError: {exc}")


if __name__ == "__main__":
    main()
