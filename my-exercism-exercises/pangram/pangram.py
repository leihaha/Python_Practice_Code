def is_pangram(sentence):
    string = "abcdefghijklmnopqrstuvwxyz"
    string_list = list(string)
    if sentence == "":
        return False
    else:
        filter(str.isalpha, sentence)
        
        # to remove the space 
        sentence = sentence.replace(" ", "")
        
        # to create a list
        sen_list = list(sentence)
        
        # to determine the string_list is the subset of the sen_list
        if set(string_list).issubset(set(sen_list)):
            return True
        else:
            return False


"""
def is_pangram(sentence):
    retuen len(set([c for c in sentence.lower() if c.isalpha() ]) == 26
"""