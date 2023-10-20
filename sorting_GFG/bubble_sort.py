def bubble_sort(seq):
    n = len(seq)
    
    for i in range(n - 1):
        for j in range(n - i -1):
            if seq[j] >  seq[j + 1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
                
    return seq
                
l = [1,23, 3,4]
print(bubble_sort(l))

# we check for the 2 adjacent elements compare them if the prev ele is biggere then we swap the ele

# doing this once we traverse from left to right then after first iteraion we get the last ele place in place

# then we do this again for the second last ele to placed in place

# we do this till n-1 time because once the second ele is placed in place then the first ele is sorted by itself

# so we run the loop n - 1 times

# in the second iteration if we give n - 1 it still gives the ans but we unecessarily check for the last and secon last ele that are allready being sorted and placed in their resp.. locations.

