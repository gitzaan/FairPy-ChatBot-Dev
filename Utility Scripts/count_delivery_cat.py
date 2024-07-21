import json

def count_delivery_location_categories(conversations_data):
    # Dictionary to store the count of each category
    category_counts = {
        "DFW Airport": 0,
        "DFW Rental Car Center": 0,
        "DAL Airport": 0,
        "Home/Office": 0,
        "Custom Address": 0,
        "Not Specified": 0
    }

    # Count the occurrences of each category
    for conversation in conversations_data:
        category = conversation.get("delivery_location_category", "Not Specified")
        category_counts[category] += 1

    return category_counts

# Read updated_conv_with_delivery_cat.json
with open("updated_conv_with_delivery_cat.json", "r", encoding="utf-8") as conv_file:
    conversations_data = json.load(conv_file)

# Count the occurrences of each category
category_counts = count_delivery_location_categories(conversations_data)

# Print the counts of each category
print("Delivery Location Category Counts:")
for category, count in category_counts.items():
    print(f"{category}: {count}")
