def wordCount(t):
    #Reads data from the file 't' and returns a dictionary with word occurrences."""
    word_occurrences = {}  # Initialize an empty dictionary to store word occurrences

    with open(t, 'r') as file:  # Open the file 't' in read mode
        # Iterate over each line in the file, keeping track of line numbers starting from 1
        for line_number, line in enumerate(file, start=1):
            # Split the line into individual words and remove leading/trailing whitespaces
            words = line.strip().split()
            
            # Iterate over each word in the line
            for word in words:
                # Remove punctuation characters and convert the word to lowercase for uniformity
                cleaned_word = word.strip('.,!?()[]{}"\'').lower()

                # Check if the word is not in the dictionary
                if cleaned_word not in word_occurrences:
                    # If the word is not in the dictionary, add it with the current line number
                    word_occurrences[cleaned_word] = [line_number]
                else:
                    # If the word is already in the dictionary, append the current line number
                    word_occurrences[cleaned_word].append(line_number)

    return word_occurrences  # Return the dictionary containing word occurrences

# Example usage:
file_path = 'sample_text.txt'
word_occurrences = wordCount(file_path)  # Call the wordCount function with the file path
print(word_occurrences)  # Print the dictionary containing word occurrences

# - Can you avoid a function call?
# The function call has been used in line 28, although we can remove the function and merge the code of the function in the main body but it might make the code less modular and harder to maintain.

# - Can you avoid the Loop?
# There is the use of loop in line 7, the loop will help to read each and every word of the line and count the occurrences of words. 
# We can use methods or libraries in order to avoid loops but they will much more difficult to handle as compared to loop 

# - Can you avoid repetive code?
# There is no repetive code here.

# - Do you understand each and every line of your code?
# Yes, I did understand each and every line of my code.
