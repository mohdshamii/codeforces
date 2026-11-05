'''
Sometimes some words like "localization" or "internationalization" are so long that writing them many times in one text is quite tiresome.

Let's consider a word too long, if its length is strictly more than 10 characters. All too long words should be replaced with a special abbreviation.

This abbreviation is made like this: we write down the first and the last letter of a word and between them we write the number of letters between the first and the last letters. That number is in decimal system and doesn't contain any leading zeroes.

Thus, "localization" will be spelt as "l10n", and "internationalization» will be spelt as "i18n".

You are suggested to automatize the process of changing the words with abbreviations. At that all too long words should be replaced by the abbreviation and the words that are not too long should not undergo any changes.

Input
The first line contains an integer n (1 ≤ n ≤ 100). Each of the following n lines contains one word. All the words consist of lowercase Latin letters and possess the lengths of from 1 to 100 characters.

Output
Print n lines. The i-th line should contain the result of replacing of the i-th word from the input data.

Examples

Input 

4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis

Output

word
l10n
i18n
p43s
'''
n = int(input())                                     #Read the number of words
def abbreviate_word(word):                           # Function to abbreviate a word if it's too long
    if len(word) > 10:                               # If the word is too long
        return f"{word[0]}{len(word) - 2}{word[-1]}" # Return the abbreviation
    return word                                      # If the word is not too long, return it as is
for _ in range(n):                                   # Loop through the number of words
    word = input()                                   #Read each word
    print(abbreviate_word(word))                     #Print the result of the abbreviation function for each word
