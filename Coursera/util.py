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