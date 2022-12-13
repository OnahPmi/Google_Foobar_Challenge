# Method 1

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

# Some Test Cases

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
