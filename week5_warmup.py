# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
magic = 'abracadabra'
# # a. Retrieve the 5th character.
print(magic [4])
# # b. Retrieve the second to last character.
print(magic [9]) 
# # c. Find the first occurrence of the letter 'c'.
print(magic[5])
# Advanced Slicing:
alphebet = "abcdefghijklmnopqrstuvwxyz"
# # a. Extract the letters 'hij'.
print(alphebet.find('hij'))
print(alphebet[7:10])
# # b. Extract every second letter starting from 'a' to 'm'.
print(alphebet [0:12:2])
# # c. Reverse the entire string using slicing.
print(alphebet [::-1])
# Problem Set 2: Extracting Information
# From Descriptions:
quote= "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(quote.find('John F. Kennedy'))
print(quote [83:])
# Manipulating Words:
info = "Python is fun. Fun is good. Good is subjective.",
# # a. Extract the word 'subjective' without knowing its exact position.
info.find('subective')


# b. Extract every third word.
# c. Reverse the positions of the words, but keep the characters in each word in the same order.

# Problem Set 3: String Methods
# Upper & Lower:
# force="MAY THE FORCE BE WITH YOU."
# result=force.lower()
# print(result)
# String Joining and Splitting:
# Given the list 
# motto = ["Make", "haste", "slowly."]
# result= " ".join(motto)

# # # a. Convert the list into a single string.
# # # b. Now, split the string at every occurrence of the letter 'a'.
# res_2=result.split('a')
# print(res_2)
# Replacing Words:
# Modify the sentence: 
# life="Life is what happens when you are busy making other plans."
# # a. Replace "busy" with "distracted".
# result=life.replace("busy", "dsitracted")
# print(result)
# b. Replace "plans" with "mistakes".

life="Life is what happens when you are busy making other plans."
result=life.replace("plans " , "mistakes ")
print(result)

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
# x = "Iteration "
# # print(x*7)

# # Word Search:
# # Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
# moonlight="With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
# result=moonlight
# print(result.find('moonlight'))
# # Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
word="Supercalifragilisticexpialidocious"
print(len(word))
# b. Count the number of times the letter 'i' appears in the same word/phrase.
print(word.count('i'))