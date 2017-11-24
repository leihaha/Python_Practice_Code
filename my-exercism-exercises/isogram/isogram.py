def is_isogram(string):
    # find the string only have letters 
    filter(str.isalpha, string)
    
    #the string only in lower 
    string = string.lower()
    
    # for the string "", return True
    if string == "":
        return True
    else:
        for item in string:
            ind = string.index(item)
            if item in string[ind+1:]:
                return False
            else:
                return True
