# Initialize a set with unique literal elements
char_set = {"a", "b", "c"}
print(char_set)

# Add a single element to the set (has no effect if element already exists)
char_set.add("d")
print(char_set)

# Remove a specific element; raises a KeyError if the element is missing
char_set.remove("a")
print(char_set)

# Safely remove an element; does nothing if the element is not found
char_set.discard("b")
print(char_set)

# Remove and return an arbitrary element from the set (raises KeyError if empty)
popped_element = char_set.pop()
print(char_set)

# Add multiple individual elements to the set sequentially
char_set.add("e")
char_set.add("r")
print(char_set)

# Remove all elements from the set, leaving it entirely empty
char_set.clear()
print(char_set)
