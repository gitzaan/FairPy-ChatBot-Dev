'''This python script maps the reservation ids from the reservation.json file and creates
a corresponding entry in the respective conversation.json file and adds the trip 
start and trip end time and outputs the file: updated_conversations_with_trip.json '''

import json

def find_reservation_created(reservation):
    if "reservation_state_history" in reservation:
        for history_entry in reservation["reservation_state_history"]:
            if "created" in history_entry:
                return history_entry["created"]
            
    if "reservation_state" in reservation and "created" in reservation["reservation_state"]:
        return reservation["reservation_state"]["created"]

    return None

def update_conversations_with_reservation(conversations, reservations):
    for conversation in conversations:
        conversation_created = conversation.get("created")
        for reservation in reservations["as_host"]:
            reservation_created = find_reservation_created(reservation)
            if conversation_created == reservation_created:
                conversation["reservation_id"] = reservation["reservation_id"]
                conversation["trip_start"] = reservation["reservation_state"]["trip_start"]
                conversation["trip_end"] = reservation["reservation_state"]["trip_end"]
                break

    return conversations

# Read conversations.json and reservations.json with explicit encoding
with open("conversations.json", "r", encoding="utf-8") as conv_file, open("reservations.json", "r", encoding="utf-8") as res_file:
    conversations_data = json.load(conv_file)
    reservations_data = json.load(res_file)

# Update conversations with reservation_id, trip_start, and trip_end
updated_conversations = update_conversations_with_reservation(conversations_data, reservations_data)

# Save the updated conversations to a new file or overwrite the original file
with open("updated_conversations_with_trip.json", "w", encoding="utf-8") as updated_conv_file:
    json.dump(updated_conversations, updated_conv_file, indent=2)
