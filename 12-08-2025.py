#1. unique in list
# input=[1,2,2,3,4,2,5,2]
# output=[1,2,3,4]
def unique_elements(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
#input
print(unique_elements([1, 2, 2, 3, 4, 1, 5]))


#2.rotates the elements of a list
#input=([1,2,3,4,5],2)
# output=[4,5,1,2,3]
def rotate_list(lst, k):
    k = k % len(lst)  
    return lst[-k:] + lst[:-k]
# input
print(rotate_list([1, 2, 3, 4, 5], 2)) 


#3.find the lomgest word
# input:"python is an amazing programming language"
# output:programming

def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
#input
print(longest_word("Python is an amazing programming language"))


#4.sum of digits function
#input:12345
# output:15
def sum_of_digits(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    return total
#input
print(sum_of_digits(12345)) 


#5.character frequency counter
# inout:"hello"
# output:{'h:1,'e':1,'l':2,'o':1}
def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq
# input
print(char_frequency("hello"))


#6.numbers which is divisble by 3 or 5 but not both
# input:numbers from 1 to 15
# output: 3 5 9 10 12 15

def numbers_divide():
    result=[]
    for i in range(1, 16):
       if (i % 3 == 0 or i % 5 == 0):
           result.append(i)
    return result
print("numbers divide by 3 or 5 but not both",numbers_divide())


#7.reverse words in a sentence
# input: "python is fun"
# output: "fun is python"

def reverse_words(sentence):
    word = ""
    words = []
    
    for ch in sentence:
        if ch == " ":
            words.append(word)
            word = ""
        else:
            word += ch
    words.append(word)  
    reverse = ""
    for i in range(len(words) - 1, -1, -1):
        reverse += words[i]
        if i != 0:
            reverse += " "

    return reverse

# Input
print("reverse word in sentence is:", reverse_words("python is fun"))


#8.star diamond pattern
#   *
#  * *
# * * *
n = 5
for i in range(1, n + 1, 2):  # 1, 3, 5
    print(" " * ((n - i) // 2) + "*" * i)


#9.count consonants in a string
 #input:"hello world"
#ouput:7

def count_consonants(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch.isalpha() and ch not in vowels:
            count += 1
    return count
#input
print(count_consonants("hello world")) 


#10.number guessing game
# Guess the number: 5   
# Wrong, try again.   
# Guess the number: 8   
# Correct! You guessed it

secret_number =9
while True:
    guess = int(input("Guess the number: "))
    if guess == secret_number:
        print("Correct! You guessed it.")
        break
    else:
        print("Wrong, try again.")


