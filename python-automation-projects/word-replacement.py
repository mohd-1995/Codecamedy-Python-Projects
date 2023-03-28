# this automation takes a string, replaces a word in that string and returns a new string

def replaced_word():
    string = "Hi hi hi hi hi  guys, I am mohammed and interested in breaking into the tech industry"
    word_to_replace = input("Enter the word to be replaced: ")
    word_replacement = input("Enter the word replacement: ")
    print(string.replace(word_to_replace, word_replacement))

replaced_word()


