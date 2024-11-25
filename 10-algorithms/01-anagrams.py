

def are_anagrams(str1: str | None = '', 
                str2: str | None = '') -> bool:
    
    '''
    comprobar en cada palabras si es igual
    '''
    x = [str1[i] for i in range(0, len(str1))]
    y = [str2[i] for i in range(0, len(str2))]
    x.sort() # sort
    y.sort()
    if x == y:
        return True
    else:
        return False


x = are_anagrams("listen", "silent") # true
y = are_anagrams("hello", "world") # false

print(x, y)
