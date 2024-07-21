'''This python script takes the update_conv_with_type.json file as input
and calculates the duration of the trip in a string format : for example
1)3 days and 2 hours 2) 4 days etc...
the ouput file is : updated_conversations_with_duration.json'''

import json
from datetime import datetime

def calculate_trip_duration(trip_start, trip_end):
    start_time = datetime.strptime(trip_start, "%Y-%m-%dT%H:%M:%S.%fZ")
    end_time = datetime.strptime(trip_end, "%Y-%m-%dT%H:%M:%S.%fZ")
    duration = end_time - start_time
    days = duration.days
    hours = duration.seconds // 3600
    if hours == 0:
        return f"{days} days"
    elif days == 0:
        return f"{hours} hours"
    else:
        return f"{days} days and {hours} hours"

def add_trip_duration(updated_conversations_data):
    for entry in updated_conversations_data:
        trip_start = entry.get("trip_start")
        trip_end = entry.get("trip_end")
        if trip_start and trip_end:
            trip_duration = calculate_trip_duration(trip_start, trip_end)
            entry["trip_duration"] = trip_duration
    return updated_conversations_data

# Read updated_conversations_with_type.json with explicit encoding
with open("updated_conversations_with_type.json", "r", encoding="utf-8") as updated_conv_file:
    updated_conversations_data = json.load(updated_conv_file)

# Add trip duration to each entry
updated_conversations_with_duration = add_trip_duration(updated_conversations_data)

# Save the updated conversations to a new file
with open("updated_conversations_with_duration.json", "w", encoding="utf-8") as updated_conv_file:
    json.dump(updated_conversations_with_duration, updated_conv_file, indent=2)
