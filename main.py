def main():
    # Path to the book file
    path_to_file = "books/frankenstein.txt"

    # Open and read the file
    with open(path_to_file) as f:
        file_contents = f.read()

    # Print the contents to the console
    print(file_contents)

    words = file_contents.split()

    # Create a dictionary of String -> Integer and populate it with each character and the number of times it appears in the text after converting the text to lowercase
    character_count = {}
    for character in file_contents.lower():
        if character.isalpha():
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1
    # Print the character count using the following format: The 'x' character was found n times
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{len(words)} words found in the document\n")
    for character, count in character_count.items():
        print(f"The '{character}' character was found {count} times")
    print(f"--- End report ---")



# Execute the main function
if __name__ == "__main__":
    main()
