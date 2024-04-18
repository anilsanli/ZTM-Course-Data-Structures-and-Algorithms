beasts = ["Centaur", "Godzilla", "Mosura", "Minotaur", "Hydra", "Nessie"]

# .index() method - Raises ValueError if the element is not found.
godzilla_index = beasts.index("Godzilla")
print(godzilla_index)

# Equivalent to .index() method.
godzilla_index = next((i for i, item in enumerate(beasts) if item == "Godzilla"), None)
print(godzilla_index)

# There is no direct equivalent of .find() method, .index() can be used instead.
# Alternatively, a list comprehension like the one above can be used.

# Equivalent of .includes() method
godzilla_included = "Godzilla" in beasts
print(godzilla_included)
