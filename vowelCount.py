def vowelCount(sentence):
    vowelCounter = 0
    for word in sentence.split():
        for letter in word:
            if letter in "aeiou":
                vowelCounter += 1
    return vowelCounter

sentence = input("Enter word/sentence, and we'll count the vowels! ")

print(vowelCount(sentence))
