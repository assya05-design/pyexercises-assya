"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Information about a luxury fashion campaign.
# 2. Process: Read, update, and remove fields from a dictionary.
# 3. Out: Display every field and its value.
# 4. My object, my five fields, and why those: My object is a fashion campaign. I chose the brand, campaign name,budget, location, and channel because these are useful for managing events.


# Your code below
# Create a dictionary describing a fashion campaign
campaign = {
    "brand" : "Chanel",
    "campaign_name" :"PAris Fashion Week",
    "budget" : 5000,
    "location" : "Paris",
    "channel" : "Instagram"
}
# Read one field
print("brand:", campaign["brand"])

# Change one field
campaign["budget"] = 6000

# Remove one field
campaign.pop("channel")

# Display every field and its value
for field, value in campaign.items():
    print(field,":", value)

print(campaign.get("designer", "Designer not found"))
