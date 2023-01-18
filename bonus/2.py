def binary_search(data, el):
    first = 0
    last = len(data)-1 

    while first <= last:
        mid = (first+last)//2

        if data[mid] == el:
            return mid
        else:
            if el < data[mid]: 
                last = mid-1
            else: 
                first = mid+1
    return -1

test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31]

# print(binary_search(test_list, 11))

def recursive_bsearch(data, el):
    if len(data) == 0:
        return -1

    else: 
        mid = len(data)//2

        if data[mid] == el:
            return mid
        else: 
            if el < data[mid]:
                return recursive_bsearch(data[:mid], el)
            else: 
                return recursive_bsearch(data[mid+1], el)

print(recursive_bsearch(test_list, 12))