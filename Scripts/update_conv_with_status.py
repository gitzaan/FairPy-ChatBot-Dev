'''This python script maps the reservation ids from the reservation.json file and creates
a corresponding entry in the respective conversation.json file and adds the trip 
start and trip end time , and also finds the trip status based on the start and end time 
.3 categories : Past , Ongoing and future and outputs the file: 
updated_conversations_with_status.json '''


import json
from datetime import datetime

def find_reservation_created(reservation):
    if "reservation_state_history" in reservation:
        for history_entry in reservation["reservation_state_history"]:
            if "created" in history_entry:
                return history_entry["created"]
            
    if "reservation_state" in reservation and "created" in reservation["reservation_state"]:
        return reservation["reservation_state"]["created"]

    return None

def classify_reservation_status(trip_start, trip_end, download_time):
    trip_start_time = datetime.strptime(trip_start, "%Y-%m-%dT%H:%M:%S.%fZ")
    trip_end_time = datetime.strptime(trip_end, "%Y-%m-%dT%H:%M:%S.%fZ")
    download_time = datetime.strptime(download_time, "%d/%m/%Y %H:%M:%S")

    if trip_start_time > download_time:
        return "Future"
    elif trip_start_time <= download_time and trip_end_time >= download_time:
        return "Ongoing"
    else:
        return "Past"

def update_conversations_with_reservation_status(conversations, reservations, download_time):
    for conversation in conversations:
        conversation_created = conversation.get("created")
        for reservation in reservations["as_host"]:
            reservation_created = find_reservation_created(reservation)
            if conversation_created == reservation_created:
                conversation["reservation_id"] = reservation["reservation_id"]
                conversation["trip_start"] = reservation["reservation_state"]["trip_start"]
                conversation["trip_end"] = reservation["reservation_state"]["trip_end"]
                conversation["reservation_status"] = classify_reservation_status(
                    reservation["reservation_state"]["trip_start"],
                    reservation["reservation_state"]["trip_end"],
                    download_time
                )
                break

    return conversations

# Read conversations.json and reservations.json with explicit encoding
with open("conversations.json", "r", encoding="utf-8") as conv_file, open("reservations.json", "r", encoding="utf-8") as res_file:
    conversations_data = json.load(conv_file)
    reservations_data = json.load(res_file)

# Download time in dd/mm/yyyy HH:mm:ss format
download_time = "28/01/2024 11:20:00"

# Update conversations with reservation_id, trip_start, trip_end, and reservation_status
updated_conversations = update_conversations_with_reservation_status(
    conversations_data,
    reservations_data,
    download_time
)

# Save the updated conversations to a new file or overwrite the original file
with open("updated_conversations_with_status.json", "w", encoding="utf-8") as updated_conv_file:
    json.dump(updated_conversations, updated_conv_file, indent=2)
