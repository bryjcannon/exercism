from string import ascii_lowercase

def is_pangram(sentence):
    if not sentence:
        return False
    sen_list = []
    for letter in sentence.lower().replace(" ",""):
        sen_list.append(letter)
    for letter in ascii_lowercase:
        count = 0
        for item in sen_list:
            if letter != item:
                count += 1
            if count == len(sen_list):
                return False
    return True
