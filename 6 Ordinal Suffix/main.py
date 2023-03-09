"""    If the last two digits end with 11, 12, or 13 then the suffix is “th.”

·       If the number ends with 1, the suffix is “st.”

·       If the number ends with 2, the suffix is “nd.”

·       If the number ends with 3, the suffix is “rd.”

·       Every other number has a suffix of “th.” """


def ordinalSuffix(number):
    return number , len(str(number))
    
    
    
    
    """ 
    if len(str(number)) > 2:
    
    else:
    
    
    
    if len(str(number)) >= 2:
        if str(number)[-2:] == "11" or str(number)[-2:] == "12" or str(number)[-2:] == "13":
            return str(number) + "th"
        else:
            
    elif str(number)[-1] == "1":
        return str(number) + "st"
    elif str(number)[-1] == "2":
        return str(number) + "nd"
    elif str(number)[-1] == "3":
        return str(number) + "rd"
    else:
        return str(number) + "th"  """      
 
 
 
    
for i in range(102):   
    print(ordinalSuffix(i))
    
assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'