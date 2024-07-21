'''This python script maps the reservation with the corresponding conversation
in the updated_conversations_with_duration.json file using the res id
and adds the pickup address as delivery location . in the res file pickup 
address and dropoff are always same'''


import json

def map_reservation_to_conversation(reservations_data, conversations_data):
    for reservation in reservations_data["as_host"]:
        reservation_id = reservation["reservation_id"]
        pickup_address = reservation["reservation_state"]["location"]["pickup"]["address"]
        
        # Find the corresponding conversation
        for conversation in conversations_data:
            if "reservation_id" in conversation and conversation["reservation_id"] == reservation_id:
                conversation["delivery_location"] = pickup_address
                break

    return conversations_data

# Read reservations.json and updated_conversations_with_duration.json with explicit encoding
with open("reservations.json", "r", encoding="utf-8") as res_file, \
     open("updated_conversations_with_duration.json", "r", encoding="utf-8") as conv_file:
    reservations_data = json.load(res_file)
    conversations_data = json.load(conv_file)

# Map reservation to conversation and add delivery location
updated_conversations_with_delivery = map_reservation_to_conversation(reservations_data, conversations_data)

# Save the updated conversations to a new file
with open("updated_conversations_with_delivery.json", "w", encoding="utf-8") as updated_conv_file:
    json.dump(updated_conversations_with_delivery, updated_conv_file, indent=2)
