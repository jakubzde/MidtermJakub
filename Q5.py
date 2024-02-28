def find_pattern_occurrences_without_import(text):
    # Split the text into words
    words = text.split()

    # Initialize a counter for occurrences
    occurrences = 0

    # Iterate through each word
    for word in words:
        # Check if the word starts with "un" and ends with "an"
        if word.startswith("un") and word.endswith("an"):
            occurrences += 1

    return occurrences

# Example usage:
text = "unjhdj khcnsdan unan"
occurrences = find_pattern_occurrences_without_import(text)
print("Number of occurrences:", occurrences)