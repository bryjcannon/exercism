def detect_anagrams(og_word, word_list):
    
    anagrams = []
    
    wd_original = {}
    for letter in og_word.lower():
        if letter in wd_original:
            wd_original[letter] += 1
        else:
            wd_original[letter] = 1
                
    for word in word_list:
        if len(word) == len(og_word):
        
            wd_current = {}
            for letter in word.lower():
                if letter in wd_current:
                    wd_current[letter] += 1
                else:
                    wd_current[letter] = 1
            
            anagram = True        
            for letter in wd_current:
                if letter in wd_original:
                    if wd_current[letter] != wd_original[letter]:
                        anagram = False
                        break
                elif letter not in wd_original:
                    anagram = False
                    break
                
            if anagram == True and word.lower() != og_word.lower():
                anagrams.append(word)
            
    return anagrams
