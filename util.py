import sys

def print_stderr(message):
    print(message, file=sys.stderr)

def send_feedback(score, feedback):
    print(f"{{\"fractionalScore\": {score}, \"feedback\": \"{feedback}\"}}")
