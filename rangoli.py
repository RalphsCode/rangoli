"""
Code to draw an alphabet Rangoli.
(Rangoli is a form of Indian folk art based on creation of patterns.)
"""

# Choose a size from 1 to 26
size = 5
#############
str_length = ((((size*2)-1)*2)-1)
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
out_string = ''
temp_str = ''
cycle = 0
letters_to_use = alphabet[0:size+1]

while cycle < size:
    if cycle == 0:
        out_string =(letters_to_use[0])
        print(out_string.center(str_length, '-'))
        cycle += 1
    else:
        temp = out_string
        out_string = letters_to_use[cycle] + '-' + temp + '-' + letters_to_use[cycle]
        print(out_string.center(str_length, '-'))
        cycle += 1

cycle -= 1

while cycle > 0:
    temp = out_string
    out_string = out_string[2:]
    out_string = out_string[:-2]
    print(out_string.center(str_length, '-'))
    cycle -= 1
