'''This Python Script gets the vehicle id, make and model from the rese
rvation.json file from the "vehicle_url" field and adds 2 fields to a new file
1) vehicle id and 2) vehicle_type : ford Escape 
Output file: updated_conversations_with_vehicle_info.json '''


import json
import re

def extract_vehicle_info(vehicle_url):
    # Extract vehicle ID and, if available, make and model from the vehicle URL
    parts = vehicle_url.split("/")
    vehicle_id = int(parts[-1])

    # Check if make and model are available
    if len(parts) < 6:  # URL doesn't contain make and model
        make_model = "Not Found"
    else:
        make = parts[-3]
        model = parts[-2]
        make_model = make + " " + model

    return vehicle_id, make_model

def add_vehicle_info_to_conversations(conversations_data, reservations_data):
    # Create a dictionary to map reservation IDs to vehicle information
    vehicle_info_map = {}
    for reservation in reservations_data["as_host"]:
        vehicle_id, make_model = extract_vehicle_info(reservation["vehicle_url"])
        vehicle_info_map[reservation["reservation_id"]] = {
            "vehicle_id": vehicle_id,
            "vehicle_type": make_model
        }

    # Add vehicle information to conversations data
    for conversation in conversations_data:
        reservation_id = conversation.get("reservation_id")
        if reservation_id in vehicle_info_map:
            vehicle_info = vehicle_info_map[reservation_id]
            conversation["vehicle_id"] = vehicle_info["vehicle_id"]
            conversation["vehicle_type"] = vehicle_info["vehicle_type"]

    return conversations_data

# Read updated_conversations_with_location.json and reservations.json
with open("updated_conversations_with_delivery.json", "r", encoding="utf-8") as conv_file, \
     open("reservations.json", "r", encoding="utf-8") as res_file:
    conversations_data = json.load(conv_file)
    reservations_data = json.load(res_file)

# Add vehicle information to conversations
updated_conversations_with_vehicle_info = add_vehicle_info_to_conversations(conversations_data, reservations_data)

# Save the updated conversations to a new file
with open("updated_conversations_with_vehicle_info.json", "w", encoding="utf-8") as updated_conv_file:
    json.dump(updated_conversations_with_vehicle_info, updated_conv_file, indent=2)
