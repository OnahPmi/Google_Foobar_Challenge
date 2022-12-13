#!/usr/bin/env python
# coding: utf-8

# # Link to Challenge
# https://foobar.withgoogle.com

# # Requirements
# ## Java
# Your code will be compiled using standard Java 8. All tests will be run by calling the solution() method inside the Solution class
# 
# Execution time is limited.
# 
# Wildcard imports and some specific classes are restricted (e.g. java.lang.ClassLoader). You will receive an error when you verify your solution if you have used a blacklisted class.
# 
# Third-party libraries, input/output operations, spawning threads or processes and changes to the execution environment are not allowed.
# 
# Your solution must be under 32000 characters in length including new lines and and other non-printing characters.
# ***
# ## Python
# Your code will run inside a Python 2.7.13 sandbox. All tests will be run by calling the solution() function.
# 
# Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.
# 
# Input/output operations are not allowed.
# 
# Your solution must be under 32000 characters in length including new lines and and other non-printing characters.
# ***

# Level one: I Love Lance & Janice
# ===========================
# 
# # Challenge
# 
# You've caught two of your fellow minions passing coded notes back and forth -- while they're on duty, no less! Worse, you're pretty sure 
# it's not job-related -- they're both huge fans of the space soap opera ""Lance & Janice"". You know how much Commander 
# Lambda hates waste, so if you can prove that these minions are wasting time passing non-job-related notes, it'll put you that much closer to a 
# promotion. 
# 
# Fortunately for you, the minions aren't exactly advanced cryptographers. In their code, every lowercase letter [a..z] is replaced with the 
# corresponding one in [z..a], while every other character (including uppercase letters and punctuation) is left untouched.  That is, 'a' becomes 
# 'z', 'b' becomes 'y', 'c' becomes 'x', etc.  For instance, the word ""vmxibkgrlm"", when 
# decoded, would become ""encryption"".
# 
# Write a function called solution(s) which takes in a string and returns the deciphered string so you can show the commander proof that these minions 
# are talking about ""Lance & Janice"" instead of doing their jobs.
# 
# ## Languages
# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java
# 
# ## Test cases
# 
# Inputs:  
# (string) s = “wrw blf hvv ozhg mrtsg’h vkrhlwv?”  
# Output:  
# (string) “did you see last night’s episode?”  
# 
# Inputs:  
# (string) s = “Yvzs! I xzm’g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!”  
# Output:    
# (string) “Yeah! I can’t believe Lance lost his job at the colony!!”    
# 
# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

# In[1]:


def test_cases():

    test_datasets = ["Lzmxv & Jzmrxv", "wrw blf hvv ozhg mrtsg'h vkrhlwv?", 
                     "Yvzs! I xzm’g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"]
    
    answers =["Lance & Janice", "did you see last night's episode?", 
              "Yeah! I can’t believe Lance lost his job at the colony!!"]
    
    counts = range(1, len(answers)+1, 1)
    for test_dataset, answer, count in zip(test_datasets, answers, counts):
        if solution(test_dataset) == answer:
            print(f"Test {count} passed!")
        else:
            print(f"Test {count} failed!")


# Solutuion
# ========

# In[2]:


# This is the solution that was submitted

def solution(s):
    import string
    
    letters = string.ascii_letters
    letter_list = [letter for letter in letters]
    upper_letters = letter_list[26:]
    
    my_list = []
    for char in s:
        if char == "a": my_list.append("z")
        elif char == "b": my_list.append("y")
        elif char == "c": my_list.append("x")
        elif char == "d": my_list.append("w")
        elif char == "e": my_list.append("v")
        elif char == "f": my_list.append("u")
        elif char == "g": my_list.append("t")
        elif char == "h": my_list.append("s")
        elif char == "i": my_list.append("r")
        elif char == "j": my_list.append("q")
        elif char == "k": my_list.append("p")
        elif char == "l": my_list.append("o")
        elif char == "m": my_list.append("n")
        elif char == "n": my_list.append("m")
        elif char == "o": my_list.append("l")
        elif char == "p": my_list.append("k")
        elif char == "q": my_list.append("j")
        elif char == "r": my_list.append("i")
        elif char == "s": my_list.append("h")
        elif char == "t": my_list.append("g")
        elif char == "u": my_list.append("f")
        elif char == "v": my_list.append("e")
        elif char == "w": my_list.append("d")
        elif char == "x": my_list.append("c")
        elif char == "y": my_list.append("b")
        elif char == "z": my_list.append("a")
        # Checks for Punctuation mark and append it to the list
        elif char not in letter_list: my_list.append(char)
        # Checks for capital letter and append it to the list unchanged
        elif char in upper_letters: my_list.append(char)
        elif char == " ": my_list.append(" ")
            
    deciphered_string = "".join(my_list) 
    return deciphered_string

test_cases()


# In[3]:


# Method 2
def solution(s):
    import string
    
    cipher = dict()
    # cipher = {}
    answer = ""

    for no, val in enumerate(string.ascii_lowercase):
        cipher[val] = string.ascii_lowercase[25 - no]

    for char in s:
        if char.islower():
            answer += cipher[char]
        else:
            answer += char

    return answer

test_cases()

