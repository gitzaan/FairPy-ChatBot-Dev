'''This python script outputs 18 unique locations in the 
updated_conversations_with_delivery.json file and finds the unique addresss'''

import json

def extract_unique_delivery_locations(conversations_data):
    unique_delivery_locations = set()
    for conversation in conversations_data:
        if "delivery_location" in conversation:
            unique_delivery_locations.add(conversation["delivery_location"])
    return unique_delivery_locations

# Read updated_conversations_with_delivery.json
with open("updated_conversations_with_delivery.json", "r", encoding="utf-8") as conv_file:
    conversations_data = json.load(conv_file)

# Extract unique delivery locations
unique_delivery_locations = extract_unique_delivery_locations(conversations_data)

# Write unique delivery locations to a text file
with open("unique_delivery_locations.txt", "w", encoding="utf-8") as txt_file:
    for location in unique_delivery_locations:
        txt_file.write(location + "\n")
