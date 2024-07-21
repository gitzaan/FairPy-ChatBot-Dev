'''This python script finds the reservation ids that have not been processed by 
the update_conv_resv_id.py file and outputs a list of them '''

import json

# Read data from updated_conversations.json and reservations.json
with open("updated_conversations.json", "r", encoding="utf-8") as updated_conv_file, open("reservations.json", "r", encoding="utf-8") as res_file:
    updated_conversations_data = json.load(updated_conv_file)
    reservations_data = json.load(res_file)

# Extract reservation IDs from updated_conversations.json
mapped_reservation_ids = {conversation.get("reservation_id") for conversation in updated_conversations_data}

# Extract all reservation IDs from reservations.json
all_reservation_ids = {reservation["reservation_id"] for reservation in reservations_data["as_host"]}

# Find reservation IDs not present in updated_conversations.json
unmapped_reservation_ids = all_reservation_ids - mapped_reservation_ids

# Print unmapped reservation IDs
print("Unmapped Reservation IDs:", unmapped_reservation_ids)
