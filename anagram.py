def isAnagram(a,b):
        d1 = {}
        d2 = {}
        
        for i in a:
            d1[i] = d1.get(i, 0) + 1
        for i in b:
            d2[i] = d2.get(i, 0) + 1
        if d1 == d2:
            return 'YES'
        else:
            return 'NO'
        
a = "b"
b = "d"
print(isAnagram(a, b))