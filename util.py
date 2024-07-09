import sys
import json

def print_stderr(message):
    print(message, file=sys.stderr)

def send_feedback(score, feedback):
    result = {
        "fractionalScore": score,
        "feedback": feedback
    }
    with open('/shared/feedback.json', 'w') as f:
        json.dump(result, f)
