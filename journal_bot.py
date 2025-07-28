# journal_bot.py

import datetime
import os

def generate_response(entry):
    # Simple AI response (can be upgraded later)
    return "Thanks for sharing. Writing things down can really help!"

def save_entry_to_file(entry_text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"journal_entries/entry_{timestamp}.txt"

    # Make sure the folder exists
    os.makedirs("journal_entries", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as file:
        file.write(entry_text)

    return filename
