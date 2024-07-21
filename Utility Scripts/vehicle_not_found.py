import json

def find_not_found_vehicle_ids(conversations_data):
    not_found_vehicle_ids = []
    for conversation in conversations_data:
        if conversation.get("vehicle_type") == "Not Found":
            vehicle_id = conversation.get("vehicle_id")
            if vehicle_id is not None:
                not_found_vehicle_ids.append(vehicle_id)
    return not_found_vehicle_ids

# Read updated_conversations_with_vehicle_info.json
with open("updated_conversations_with_vehicle_info.json", "r", encoding="utf-8") as conv_file:
    conversations_data = json.load(conv_file)

# Find vehicle IDs of cars that are not found
not_found_vehicle_ids = find_not_found_vehicle_ids(conversations_data)

# Print the vehicle IDs of cars that are not found
print("Vehicle IDs of cars that are not found:")
for vehicle_id in not_found_vehicle_ids:
    print(vehicle_id)
