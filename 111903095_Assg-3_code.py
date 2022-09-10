import pandas as pd
import nltk
from nltk import word_tokenize

def minDistance(word1="", word2=""):
    row = len(word2)+1
    col = len(word1)+1
    matrix=[]
    for i in range(row):
        matrix.append([])
        for j in range(col):
            matrix[i].append(0)
    for  i in range(col):
        matrix[0][i] = i
    for i in range(row):
        matrix[i][0] = i
    #print(matrix)
    for i in range(1, row):
        for j in range(1, col):
            if word2[i-1] == word1[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])+1
    return matrix[row-1][col-1]

input = ""
print("Reading dictionary...")

with open("new_words.txt", "r") as file:
    input = file.read()
input = input.lower()
words_dict = word_tokenize(input)
words_dict = list(set(words_dict))
print("Length of dictionary = ", len(words_dict))
print("Dictionary ready!!!")

def autocorrect(word):
    possible_words = []
    if word in words_dict:
        print("No error!!")
    else:
        for w in words_dict:
            if minDistance(word, w) <= 2:
                possible_words.append(w)
        print("Possible words generated = ", len(possible_words))
    for v in possible_words:
        print(v)

autocorrect("handman")
#autocorrect("moy")