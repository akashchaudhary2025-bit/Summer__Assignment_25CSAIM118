# WAP to count words in a sentence

sentence = input("Enter a sentence: ")

count = 0
in_word = False

for char in sentence:
    if char != " " and not in_word:
        count += 1
        in_word = True
    elif char == " ":
        in_word = False

print("Number of words in the sentence:", count)
