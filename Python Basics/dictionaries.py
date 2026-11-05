# Initialize a dictionary with employee/user data
user_profile = {"name": "tarun", "age": 17, "salary": 60000}
print(user_profile)

# Update the value of an existing key ('age')
user_profile["age"] = 16
print(user_profile)

# Insert a new key-value pair ('school': 'dsp') into the dictionary
user_profile["school"] = "dsp"
print(user_profile)

# Get the total number of key-value pairs (length) in the dictionary
print("Length:", len(user_profile))

# Convert the dictionary into its equivalent string representation
print("Equivalent String:%s" % str(user_profile))

# Create a shallow copy of the dictionary
user_profile_copy = user_profile.copy()
print(user_profile_copy)

# Safely retrieve a value using a key (returns None if key doesn't exist)
print("value:%s" % user_profile.get("age"))

# Retrieve a view object containing all key-value tuples
print("value:%s" % user_profile.items())

# Retrieve a view object containing all keys from the dictionary
print("value:%s" % user_profile.keys())

# Retrieve a view object containing all values from the dictionary
print("value:%s" % user_profile.values())

# Get key value; if key doesn't exist, insert it with the specified default
print("value:%s" % user_profile.setdefault("age", None))
print(user_profile)

# Initialize two distinct dictionaries to demonstrate merging
target_dict = {"nm": "tarun", "age": 25}
source_dict = {"gender": "male"}

# Merge the source dictionary into the target dictionary
target_dict.update(source_dict)
print(target_dict)
