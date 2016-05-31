def encode(code):
    
    result = []
      
    count = 1
    letter = None
    for position in xrange(len(code)): 
           
        try:
            current = code[position]
            next = code[position+1]            
            if current == next:
                count += 1
                letter = current                
            elif current != next and count == 1:
                result.append(('', current))
                count = 1
                letter = next                
            elif current != next and count != 1:
                result.append((count, current))
                count = 1
                letter = next                
            else:
                print "Errorz1"
                
        except:
            if code[position] == code[position-1]:
                result.append((count, letter))
            else:
                result.append(('', letter))
            
    result2 = ''.join([str(num)+str(letter) for num, letter in result])
    #print result, count, letter
    return result2
            
                                      
#try to clean this up at some point...
def decode(code):
    
    result = []
    
      
    count = '1'
    item = None
    
    if code[0].isdigit():
        count = code[0]
    elif code[0].isalpha():
        item = code[0]
        result.append((count, item))
    
    for position in xrange(1, len(code)): 
           

        previous = code[position-1]
        current = code[position]
                
        if previous.isdigit() and current.isdigit():
            count += current
        elif previous.isdigit() and current.isalpha():
            item = current
            result.append((count, item))
        elif previous.isalpha() and current.isalpha():
            count = '1'
            item = current
            result.append((count, item))
        elif previous.isalpha() and current.isdigit():
            count = current
        elif previous.isdigit() and current.isspace():
            result.append((count, ' '))
        elif previous.isalpha() and current.isspace():
            count = '1'
            item = current
            result.append((count, item))
        elif previous.isspace() and current.isalpha():
            count = '1'
            result.append((count, current))
        elif previous.isspace() and current.isdigit():
            count = current
        else:
            result.append(('1', 'ER'))
                            
    result2 = ''.join([int(num) * letter for num, letter in result])
    return result2    
