'''This python script takes the updated_conversations_with_trip: 
updated_conversations_with_type.json '''
import json
from datetime import datetime, timedelta

def classify_reservation_status_type(trip_start, trip_end, download_time):
    trip_start_time = datetime.strptime(trip_start, "%Y-%m-%dT%H:%M:%S.%fZ")
    trip_end_time = datetime.strptime(trip_end, "%Y-%m-%dT%H:%M:%S.%fZ")
    download_time = datetime.strptime(download_time, "%d/%m/%Y %H:%M:%S")

    # Calculate time differences
    time_until_start = trip_start_time - download_time
    time_since_end = download_time - trip_end_time
    # my attempt
    time_from_start = download_time - trip_start_time
    time_till_end = trip_end_time - download_time

    # Categorize based on time differences
    if trip_start_time > download_time:
        if time_until_start <= timedelta(days=1):
            return "Recent Future"
        else:
            return "Post Future"
    elif trip_end_time < download_time:
        if time_since_end <= timedelta(days=1):
            return "Recent Past"
        else:
            return "Pre Past"
    else:  # Ongoing trips
        if time_from_start <= timedelta(hours=24):
            start_category = "Recent Start Ongoing"
        elif time_till_end <= timedelta(days=1):
            start_category = "End Soon Ongoing"
        else:
            start_category = "Non-Recent Ongoing"

        return start_category

def update_conversations_with_reservation_status_type(conversations, download_time):
    for conversation in conversations:
        reservation_status = conversation.get("reservation_status")
        trip_start = conversation.get("trip_start")
        trip_end = conversation.get("trip_end")

        # Skip if reservation_status is not present or trip_start is not present
        if not reservation_status or not trip_start:
            continue

        reservation_status_type = classify_reservation_status_type(trip_start, trip_end, download_time)
        conversation["reservation_status_type"] = reservation_status_type

    return conversations

# Read updated_conversations_with_status.json with explicit encoding
with open("updated_conversations_with_status.json", "r", encoding="utf-8") as updated_conv_file:
    updated_conversations_data = json.load(updated_conv_file)

# Download time in dd/mm/yyyy HH:mm:ss format
download_time = "28/01/2024 11:20:00"

# Update conversations with reservation_status_type
updated_conversations_with_type = update_conversations_with_reservation_status_type(
    updated_conversations_data,
    download_time
)

# Save the updated conversations to a new file or overwrite the original file
with open("updated_conversations_with_type.json", "w", encoding="utf-8") as updated_conv_file:
    json.dump(updated_conversations_with_type, updated_conv_file, indent=2)
