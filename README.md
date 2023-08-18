# Word List Manipulator 2.0

Word List Manipulator 2.0 is a powerful tool for editing and optimizing wordlists. With its easy-to-use command-line interface, you can perform various operations on your wordlists, including removing duplicates, optimizing for WPA/WPA2, and more.

## Features

Word List Manipulator 2.0 offers a wide range of features for manipulating wordlists:

### Case Options

- **Change case of first letter**: This function changes the case of the first letter in each line of the wordlist. You can choose to capitalize or lowercase the first letter.
- **Change case of last letter**: This function changes the case of the last letter in each line of the wordlist. You can choose to capitalize or lowercase the last letter.
- **Change all lower case to upper case**: This function changes all lowercase letters in the wordlist to uppercase.
- **Change all upper case to lower case**: This function changes all uppercase letters in the wordlist to lowercase.
- **Invert case (lower to upper, upper to lower)**: This function inverts the case of each letter in the wordlist.

### Combination Options

- **Combine words from one list to each word in another list**: This function combines each line from one wordlist with each line in another wordlist, creating a new wordlist with the combined lines.
- **Combine all wordlists in a directory to one wordlist**: This function combines all the wordlists in a specified directory into a single wordlist.

### Prepend/Prefix Options

- **Prefix numeric values in sequence to a wordlist (ie. 0 - 99999)**: This function prefixes a sequence of numeric values to each line in the wordlist.
- **Prefix fixed number of numeric values in sequence to a wordlist (ie. 00000 - 99999)**: This function prefixes a fixed number of numeric values in sequence to each line in the wordlist.
- **Prefix word/characters to a wordlist**: This function prefixes a specified word or characters to each line in the wordlist.

### Append/Suffix Options

- **Suffix numeric values in sequence to a wordlist (ie. 0 - 99999)**: This function appends a sequence of numeric values to each line in the wordlist.
- **Suffix fixed number of numeric values in sequence to a wordlist (ie. 00000 - 99999)**: This function appends a fixed number of numeric values in sequence to each line in the wordlist.
- **Suffix word/characters to a wordlist**: This function appends a specified word or characters to each line in the wordlist.

### Inclusion Options

- **Include characters/word in a defined position from the START of a word**: This function inserts specified characters or a word at a defined position from the start of each line in the wordlist.
- **Include characters/word in a defined position from the END of a word**: This function inserts specified characters or a word at a defined position from the end of each line in the wordlist.

### Substitution Options

- **Substitute/Replace characters from START of word**: This function replaces specified characters from the start of each line in the wordlist.
- **Substitute/Replace characters from END of word**: This function replaces specified characters from the end of each line in the wordlist.
- **Substitute/Replace characters at a certain position**: This function replaces specified characters at a certain position in each line of the wordlist.

### Clean/Optimize Wordlist Options

- **Full optimization of wordlist**: This function performs a full optimization of the wordlist, including removing duplicates, non-ASCII characters, comments, and more.
- **Optimize wordlist for WPA**: This function optimizes the wordlist for WPA/WPA2 by removing lines less than 8 or greater than 63 characters.
- **Sort wordlist on length of words**: This function sorts the wordlist based on the length of the words.

### Split Files Options

- **Split wordlists files by size**: This function splits the wordlist into multiple files based on a specified file size.
- **Split wordlists into a defined number of files**: This function splits the wordlist into a specified number of files with an equal number of lines.
- **Split wordlists by maximum line count per file**: This function splits the wordlist into multiple files based on a specified maximum line count per file.

### Removal/Deletion Options

- **Remove X number of characters from the start of a word**: This function removes a specified number of characters from the start of each line in the wordlist.
- **Remove X number of characters from the end of a word**: This function removes a specified number of characters from the end of each line in the wordlist.
- **Remove specific characters globally from words**: This function removes specified characters globally from each line in the wordlist.
- **Remove words containing specific characters**: This function removes lines containing specified characters from the wordlist.
- **Remove lines with X number of identical adjacent characters**: This function removes lines with a specified number of identical adjacent characters from the wordlist.
- **Remove lines from one list that exist in another list**: This function removes lines from the wordlist that exist in another specified wordlist.
- **Remove words which do NOT have X number of numeric values**: This function removes lines that do not have a specified number of numeric values from the wordlist.
- **Remove words which have X number of repeated characters**: This function removes lines that have a specified number of repeated characters from the wordlist.
- **Remove words of a certain length**: This function removes lines of a specified length from the wordlist.
- **Remove characters from and including a specified character**: This function removes characters from and including a specified character in each line of the wordlist.

### Miscellaneous Fun Options

- (Coming in the future)

### File Information Options

- **Line count and most counted word**: This function displays the total line count of the wordlist and the most frequently occurring word.

### Update Options

- **Check for updates**: This function checks for updates to the Word List Manipulator 2.0.
- **Update Word List Manipulator from Github**: This function updates the Word List Manipulator 2.0 from the Github repository.

## How to Use

1. **Clone the repository**: Download or clone the Word List Manipulator 2.0 repository from GitHub.
2. **Run the script**: Run the script by executing `python3 WordListManipulator.py` in your terminal or command prompt.
3. **Follow the prompts**: The script will guide you through the available options. Follow the prompts to select the desired operation and provide any required input.
4. **Process your wordlists**: The script will process your wordlists based on your selections and display any relevant results.

## Requirements

- Python 3.x

## Contributing

If you'd like to contribute to the Word List Manipulator 2.0, please feel free to submit a pull request on GitHub.

## License

Word List Manipulator 2.0 is open-source software released under the MIT License.




