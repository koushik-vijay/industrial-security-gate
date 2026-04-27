# app.py
# This is a sample industrial data processing script
# It contains a deliberate vulnerability for the security scanner to catch.
# This uses a hardcoded password, which Bandit *definitely* catches.
import os
password = "admin145"

def process_data(user_input):
    # SECURITY VULNERABILITY: eval() is dangerous because it executes arbitrary code.
    # A real-world security scanner like Bandit will flag this as a 'High' severity issue.
    return eval(user_input)

if __name__ == "__main__":
    print("Industrial Automation Data Processor: Initializing...")
    data = "2 + 2"
    print(f"Result: {process_data(data)}")