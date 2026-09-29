# Anagram

def isAnagram(s1,s2):
    # logic #1 using existing finction SORTED()
    if len(s1) != len(s2):
        return False
    s1= sorted(s1)
    s2 = sorted(s2)
    if s1 == s2:
        return True
    else:
        return False
    
    
   # Logic 2 using seen list 
seen = {}
for ch in s1:
   seen[char] = seen.get(char,0)+1
for ch2 in s2:
    if ch2 in seen:
        seen[ch2]-=1
    else:
       return False
if (value ==0 for value in seen.values()):
    return True
else:
    return False
 
print(isAnagram("listen","slient"))
    

