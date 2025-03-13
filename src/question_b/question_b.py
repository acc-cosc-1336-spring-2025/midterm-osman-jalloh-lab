#write functions here, don't add input('') statements here!
def reverse_string(string1):
    string2 = ""
    i=len (string1)-1
    while i >=0:
        string2+= string1[i]
        i-=1
    return string2