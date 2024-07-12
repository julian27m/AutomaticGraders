import sys
import json
import os

def print_stderr(message):
    print(message, file=sys.stderr)

def initialize_feedback():
    global feedback_data
    feedback_data = []
    print_stderr("Feedback initialized")

def append_feedback(score, feedback, filename):
    global feedback_data
    feedback_data.append({"score": score, "feedback": feedback, "file": filename})
    print_stderr(f"Feedback appended: {feedback}")

def finalize_feedback():
    global feedback_data
    result = {
        "feedback_items": feedback_data
    }
    output_dir = '/shared/'
    print_stderr(f"Finalizing feedback in {output_dir}")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print_stderr(f"Directory {output_dir} created")

    with open(os.path.join(output_dir, 'feedback.json'), 'w') as f:
        json.dump(result, f)
    print_stderr("Feedback written to feedback.json")

def send_feedback(score, feedback, filename=""):
    initialize_feedback()
    append_feedback(score, feedback, filename)
    finalize_feedback()
