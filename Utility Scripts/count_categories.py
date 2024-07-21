'''This script finds the number of reservations in each category
pre past ,past , recent start ongong , future etc...'''

import json

def count_trip_categories(conversations):
    categories_count = {
        "Past": {"Recent Past": 0, "Pre Past": 0},
        "Ongoing": {"Recent Start Ongoing": 0, "End Soon Ongoing": 0, "Non-Recent Ongoing": 0},
        "Future": {"Recent Future": 0, "Post Future": 0}  # Fix the case here
    }

    for conversation in conversations:
        status_type = conversation.get("reservation_status_type")

        if status_type:
            categories_count[conversation["reservation_status"]][status_type] += 1

    return categories_count

# Read updated_conversations_with_type.json
with open("updated_conversations_with_type.json", "r", encoding="utf-8") as updated_conv_file:
    updated_conversations_data = json.load(updated_conv_file)

# Count trips in each category
trip_categories_count = count_trip_categories(updated_conversations_data)

# Print the results
for status, types in trip_categories_count.items():
    print(f"{status} Trips:")
    for trip_type, count in types.items():
        print(f"  {trip_type}: {count}")
    print()
