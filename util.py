import sys
import json

def print_stderr(message):
    print(message, file=sys.stderr)

def send_feedback(score, feedback):
    result = {
        "fractionalScore": score,
        "feedback": feedback
    }
    # Local:
    # with open('/autograder/source/feedback.json', 'w') as f:
    # Coursera
    with open('/shared/feedback.json', 'w') as f:
        json.dump(result, f)
'''
import sys
import json
import os

def print_stderr(message):
    print(message, file=sys.stderr)

def initialize_feedback():
    global feedback_data
    feedback_data = []

def append_feedback(score, feedback, filename):
    global feedback_data
    feedback_data.append({"score": score, "feedback": feedback, "file": filename})

def finalize_feedback():
    global feedback_data
    result = {
        "feedback_items": feedback_data
    }
    output_dir = '/shared/'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(os.path.join(output_dir, 'feedback.json'), 'w') as f:
        json.dump(result, f)

def send_feedback(score, feedback, filename=""):
    initialize_feedback()
    append_feedback(score, feedback, filename)
    finalize_feedback()
'''