import json
import uuid
import os

# Function to create a unique token
def create_token():
    return str(uuid.uuid4())

# Example list of logs with their parameters (replace this with your actual data)
logs = [
    {
        "logfile": "logs/log1",
        "vehicle": "EDGAR",
        "date_captured": "2023-07-30",
        "location": "muenchen"
    }
]

# Create log JSON structure
log_data = []
for log in logs:
    log_data.append({
        "token": create_token(),
        "logfile": os.path.join("..", "muenchen", log["logfile"]),
        "vehicle": log["vehicle"],
        "date_captured": log["date_captured"],
        "location": log["location"]
    })

# Write log data to log.json file
dataset_root = '../muenchen'
with open(os.path.join(dataset_root, 'v1.0-mini/log.json'), 'w') as f:
    json.dump(log_data, f, indent=2)

print(f"log.json created successfully at {os.path.join(dataset_root, 'v1.0-mini/log.json')}")
