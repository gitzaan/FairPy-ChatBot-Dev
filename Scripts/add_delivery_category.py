'''This python script takes the updated_conversations_with_vehicle_type
file as input and categorizes the delivery locations into 5 and outputs
updated_conv_with_delivery_cat.json'''


import json

def classify_delivery_location(delivery_location):
    # Dictionary to map delivery locations to categories
    location_categories = {
        "2424 East 38th Street, Irving, TX 75062": "DFW Rental Car Center",
        "3600 Passport Avenue, Irving, TX 75062": "DFW Rental Car Center",
        "2400 Aviation Drive, DFW Airport, TX 75261": "DFW Airport",
        "8008 Herb Kelleher Way, Dallas, TX 75235": "DAL Airport",
        "4443 Zahir Court, Irving, TX 75061": "Home/Office",
        "4425 West Airport Freeway, Irving, TX 75062": "Home/Office"
    }

    # Check if the delivery location is in the predefined categories
    if delivery_location in location_categories:
        return location_categories[delivery_location]
    else:
        return "Custom Address"

def add_delivery_location_category(conversations_data):
    # Add delivery location category to conversations data
    for conversation in conversations_data:
        delivery_location = conversation.get("delivery_location")
        if delivery_location:
            category = classify_delivery_location(delivery_location)
            conversation["delivery_location_category"] = category
        else:
            conversation["delivery_location_category"] = "Not Specified"

    return conversations_data

# Read updated_conversations_with_vehicle_type.json
with open("updated_conversations_with_vehicle_type.json", "r", encoding="utf-8") as conv_file:
    conversations_data = json.load(conv_file)

# Add delivery location category to conversations
updated_conversations_with_delivery_cat = add_delivery_location_category(conversations_data)

# Save the updated conversations with delivery location category to a new file
with open("updated_conv_with_delivery_cat.json", "w", encoding="utf-8") as updated_conv_file:
    json.dump(updated_conversations_with_delivery_cat, updated_conv_file, indent=2)
