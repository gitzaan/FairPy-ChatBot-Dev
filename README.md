# Project Overview

This README file provides an overview of the various tasks and scripts involved in processing reservation, conversation, and vehicle data. Each task is explained with its objective, output, and the script used.

## Task 1: Mapping Reservations with Conversations

**Objective:** 
Map the reservation IDs from `reservations.json` with the corresponding entries in `conversations.json` using timestamps.

**Details:** 
- 1469 out of 1491 reservations were mapped successfully.
- 22 reservations remained unmapped as their conversations didn't exist.

**Output:** 
- `updated_conversations.json`

**Script:** 
- `update_conv_resv_id.py`

**Description:** 
This python script maps the reservation ids from the `reservations.json` file and creates a corresponding entry in the respective `conversations.json` file and outputs a new `updated_conversations.json` file.

A utility script was also written to find unmapped reservation IDs.

## Task 2: Adding Trip Start and End Time

**Objective:** 
Find the reservation status and the trip start and end times.

**Output:** 
- `updated_conversations_with_trip.json`

**Script:** 
- `update_conv_with_trip.py`

**Description:** 
This python script maps the reservation ids from the `reservations.json` file and creates a corresponding entry in the respective `conversations.json` file and adds the trip start and trip end time and outputs the file: `updated_conversations_with_trip.json`.

**Output:** 
- `updated_conversations_with_status.json`

**Script:** 
- `update_conv_with_status.py`

**Description:** 
This python script maps the reservation ids from the `reservations.json` file and creates a corresponding entry in the respective `conversations.json` file and adds the trip start and trip end time, and also finds the trip status based on the start and end time (3 categories: Past, Ongoing, and Future) and outputs the file: `updated_conversations_with_status.json`.

**Note:** Status was determined using the file download time as a reference.

## Task 3: Further Classification of Trip Status

**Objective:** 
Classify the trip status into more detailed categories.

**Instructions:** 
Assume now as Jan 28, file download time.

**Categories:**
- **Past Trips:**
  - Recent Past: Trip ended in the last 24 hours.
  - Pre Past: Trip ended 24+ hours before.
- **Ongoing Trips:**
  - Recent Start Ongoing: Trip started in the past 24 hours.
  - End Soon Ongoing: Trip ends in the next 24 hours.
  - Non-Recent Ongoing: Trips which started 24 hours prior or end 24 hours post.
- **Future Trips:**
  - Recent Future: Trip starts in the next 24 hours.
  - Post Future: Trip will start after 24 hours.

**Output:** 
- `updated_conversations_with_type.json`

**Script:** 
- `update_conv_with_type.py`

## Task 4.1: Adding Trip Duration and Delivery Location

**Objective:** 
Calculate the duration of the trip in a string format and add the delivery location.

**Output:** 
- `updated_conversations_with_duration.json`

**Script:** 
- `Update_conv_with_duration.py`

**Description:** 
This python script takes the `update_conv_with_type.json` file as input and calculates the duration of the trip in a string format: for example 3 days and 2 hours or 4 days etc... The output file is: `updated_conversations_with_duration.json`.

**Output:** 
- `updated_conversations_with_delivery.json`

**Script:** 
- `Update_conv_with_location.py`

**Description:** 
This python script maps the reservation with the corresponding conversation in the `updated_conversations_with_duration.json` file using the res id and adds the pickup address as the delivery location. In the res file, pickup address and dropoff are always the same.

## Task 4.2: Adding Vehicle Information

**Objective:** 
Add vehicle ID, make, model, and year to the conversation entries.

**Output:** 
- `updated_conversations_with_vehicles_info.json`

**Script:** 
- `add_vehicle_info.py`

**Description:** 
This Python script gets the vehicle id, make, and model from the `reservation.json` file from the "vehicle_url" field and adds 2 fields to a new file: 1) Vehicle id and 2) Vehicle_type: Ford Escape. Output file: `updated_conversations_with_vehicle_info.json`.

**Note:** Vehicle Make and Model were added by scraping the URL.

## Task 5: Adding Vehicle Color and Type

**Objective:** 
Add color and compile vehicle details as a single string in the vehicle type field.

**Output:** 
- `updated_conversations_with_vehicle_type.json`

**Script:** 
- `add_vehicle_color&year.py`

**Description:** 
This python script maps the `updated_delivery_with_vehicle_info.py` with the `vehicle_listing` file using the vehicle id and then gets the year, make, color, model, and adds it as a single string to the vehicle_type file. It maintains the 10 Not found vehicles problem that occurred in the last script. Output file: `updated_conversations_with_vehicle_type.json`.

**Note:** There were invalid vehicle types because the URL wasn't there.

## Task 6: Categorizing Delivery Location

**Objective:** 
Classify the delivery location into specific categories.

**Instructions Given:**
- DFW Airport - 2400 Aviation Drive, DFW Airport, TX 75261
- DAL Airport - 8008 Herb Kelleher Way, Dallas, TX 75235
- Home/Office - 4443 Zahir Court, Irving, TX 75061
- Home/Office - 4425 West Airport Freeway, Irving, TX 75062

**Categories:**
- DFW Airport
- DFW Rental Car Center
- DAL Airport
- Home/Office
- Custom Address

**Output:** 
- `updated_conv_with_delivery_cat.json`

**Script:** 
- `add_delivery_category.py`

**Description:** 
This python script takes the `updated_conversations_with_vehicle_type` file as input and categorizes the delivery locations into 5 categories and outputs `updated_conv_with_delivery_cat.json`.

**Note:** A utility script was used to find the list of all addresses and another utility script was written to count the delivery locations.

## Task 7: Extracting FAQs from Reservations

**Objective:** 
Extract frequently asked questions (FAQs) from the reservations.json file.

**Output:** 
- List of questions and answers (QA pairs).

**Script:** 
- `FairPy Questions extraction.ipynb`

**Description:** 
This python script extracts questions and their answers based on the occurrence of a question mark in the conversation field. It also attaches an immediate message to add context to the question.

**Method:** 
The extracted QA pairs were fed to ChatGPT to generate the final FAQs.

