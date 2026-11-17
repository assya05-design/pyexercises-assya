"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in? A set of permissions represented by numbers (bits).
    2. What happens to it? Bitwise OR combines permissions. Bitwise AND checks whether a permission is present. Bitwise OR adds a permission. Bitwise NOT is not needed here; XOR removes a permission.
    3. What comes out? The permissions displayed in binary at each step.
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign. The permissions are about managing a marketing campaign: view, edit and publish.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
# STEP 1: Define the permissions
VIEW = 1       # 001
EDIT = 2       # 010
PUBLISH = 4    # 100

# STEP 2: Give a user two permissions
permissions = VIEW | EDIT

print("INITIAL PERMISSIONS")
print("Binary:", format(permissions, "03b"))
print("Decimal:", permissions)

# STEP 3: Combine two permissions
print("\nCOMBINE PERMISSIONS")
combined = VIEW | EDIT
print("VIEW | EDIT =", format(combined, "03b"))

# STEP 4: Check whether EDIT permission is present
print("\nCHECK PERMISSION")
if permissions & EDIT:
    print("The user has EDIT permission.")
else:
    print("The user does not have EDIT permission.")

print("Check in binary:", format(permissions & EDIT, "03b"))

# STEP 5: Add PUBLISH permission
print("\nADD PUBLISH PERMISSION")
permissions = permissions | PUBLISH
print("New permissions:", format(permissions, "03b"))
print("Decimal value:", permissions)

# STEP 6: Remove EDIT permission
print("\nREMOVE EDIT PERMISSION")
permissions = permissions & ~EDIT
print("New permissions:", format(permissions, "03b"))
print("Decimal value:", permissions)

# STEP 7: Display final permissions
print("\nFINAL PERMISSIONS")

if permissions & VIEW:
    print("VIEW: Yes")
else:
    print("VIEW: No")

if permissions & EDIT:
    print("EDIT: Yes")
else:
    print("EDIT: No")

if permissions & PUBLISH:
    print("PUBLISH: Yes")
else:
    print("PUBLISH: No")