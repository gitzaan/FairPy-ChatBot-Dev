'''This python script maps the updated_delivery_with_vehicle_info.py 
with the vehicle_listing file using the vehicle id and then gets the 
year , make , color , model and adds it as a single string to the 
vehicle_type file. It maintains the 10 Not found vehicles problem that 
occured in the last script
Output file : Updated_conversations_with_vehicle_type.json'''

import json

def extract_vehicle_info(vehicle_listing_data, vehicle_id):
    # Search for the vehicle with the given ID in the vehicle listing data
    for vehicle in vehicle_listing_data:
        if vehicle.get("vehicle_id") == vehicle_id:
            year = vehicle["details"]["details"]["year"]
            model = vehicle["details"]["details"]["model"]
            make = vehicle["details"]["details"]["make"]
            if vehicle["details"]["color"] is not None:
                color = vehicle["details"]["color"]
                return f"{year} {make} {model} {color}"
            return f"{year} {make} {model}"
    return "Not Found"

def add_vehicle_type_to_conversations(conversations_data, vehicle_listing_data):
    # Add vehicle type to conversations data
    for conversation in conversations_data:
        vehicle_id = conversation.get("vehicle_id")
        if vehicle_id is not None:
            vehicle_type = extract_vehicle_info(vehicle_listing_data, vehicle_id)
            conversation["vehicle_type"] = vehicle_type

    return conversations_data

# Read updated_conversations_with_delivery.json and vehicle_listing.json
with open("updated_conversations_with_vehicle_info.json", "r", encoding="utf-8") as conv_file, \
     open("vehicle_listing.json", "r", encoding="utf-8") as vehicle_file:
    conversations_data = json.load(conv_file)
    vehicle_listing_data = json.load(vehicle_file)

# Add vehicle type to conversations
updated_conversations_with_vehicle_type = add_vehicle_type_to_conversations(conversations_data, vehicle_listing_data)

# Save the updated conversations to a new file
with open("updated_conversations_with_vehicle_type.json", "w", encoding="utf-8") as updated_conv_file:
    json.dump(updated_conversations_with_vehicle_type, updated_conv_file, indent=2)
