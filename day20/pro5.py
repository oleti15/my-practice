def slug_generator(s):
    s=s.lower()
    # slug=s.replace(" ","-")  # if there is no special characters
    # return slug
    result=""
    for i in range(0,len(s)):
        if s[i].isalnum():
            result+=s[i]
        elif s[i]==" ":
            result+="-"
        else:
            continue
    return result
title=input()
result=slug_generator(title)
print(result)