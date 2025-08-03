import csv
from datetime import datetime
import os

def save_feedback(reply_text, like, dislike, comments, filepath="feedback.csv"):
    feedback = {
        "timestamp": datetime.now().isoformat(),
        "reply": reply_text,
        "like": like,
        "dislike": dislike,
        "comments": comments
    }
    file_exists = os.path.isfile(filepath)
    try:
        with open(filepath, mode="a", newline="", encoding="utf-8") as file:
            fieldnames = ["timestamp", "reply", "like", "dislike", "comments"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()  # Write header only if file does not exist
            writer.writerow(feedback)
        return True
    except Exception as e:
        # Raise the error so Streamlit can show it in the UI
        raise RuntimeError(f"Error saving feedback: {e}")
    