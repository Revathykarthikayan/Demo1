input_string = "Guvi Geek Network Private Limited"
# Define a dictionary to store the count of each vowel
vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
# Convert input string to lowercase
input_string = input_string.lower()
# Iterate through each character in input string
for char in input_string:
                                # Check if the character is a vowel
    if char in vowel_counts:
        #increment the count of that vowel in the dictionary
        vowel_counts[char] += 1
# Print the count of each vowel
for vowel, count in vowel_counts.items():
    print(f"Number of {vowel} is:", count)