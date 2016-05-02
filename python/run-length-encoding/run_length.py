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
                print "Errorz"
                
        except:
            if code[position] == code[position-1]:
                result.append((count, letter))
            else:
                result.append(('', letter))
            
    result2 = ''.join([str(num)+str(letter) for num, letter in result])
    #print result, count, letter
    return result2
            
                                      

#def decode():
