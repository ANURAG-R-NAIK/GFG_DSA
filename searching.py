# def search(seq, x):
#     lo, hi = 0, len(seq) - 1
    
#     while lo <= hi:
#         mid = (lo + hi) // 2
        
#         if seq[mid] < x:
#             lo = mid + 1
#         elif seq[mid] > x:
#             hi = mid - 1
#         else:
#             return mid 
#     return -1

# seq =  [1,2,3,4,5,6,7,8,9]
# x = 5
# print(search(seq, x))

###############

# in recursive format

# def rec(seq, x, lo, hi):
    
#     if lo > hi:
#         return -1
    
#     mid = (lo + hi) // 2
    
#     if seq[mid] > x:
#         return rec(seq, x, lo, mid-1)
#     elif seq[mid] < x:
#         return rec(seq, x, mid+1, hi)
    
#     else:
#         return mid
    
# seq =  [1,2,3,4,5,6,7,8,9]
# x = 5
# lo = 0
# hi = len(seq) - 1
# print(rec(seq, x, lo, hi))

#################333

# SORTED ARRAY RETURNS THE FIRST OCCURANCE OF ELEMENT

# def search(seq, x):
#     lo, hi = 0, len(seq) - 1
#     # index = -1
    
#     while lo <= hi:
#         mid = (lo + hi) // 2
        
#         if seq[mid] < x:
#             lo = mid + 1
            
#         elif seq[mid] > x:
#             hi = mid - 1
        
#         else:
#             if mid == 0 or seq[mid - 1] != seq[mid]:
#                 return mid
#             else:
#                 hi = mid - 1
#     return -1

# seq = [1,2,2,2,2,3,3,3,3,4,4,4]
# x = 2
# print(search(seq, x))


##############################

# SORTED ARRAY RETURNS THE LAST OCCURANCE OF ELEMENT

# def search(seq, x):
#     lo, hi = 0, len(seq) - 1
    
#     while lo <= hi:
        
#         mid = (lo + hi) // 2
        
#         if seq[mid] < x:
#             lo = mid + 1
#         elif seq[mid] > x:
#             hi = mid - 1
            
#         else:
#             if mid == len(seq) - 1 or seq[mid] != seq[mid+1]:
#                 return mid
#             else:
#                 lo = mid + 1
                
# seq = [1,2,2,2,2,3,3,3,3,4,4,4]
# x = 2
# print(search(seq, x))


    
    