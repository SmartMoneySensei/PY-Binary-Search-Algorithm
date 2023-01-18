# code your recursive algorithm below here

def recursive_bsearch(data, el):
    if len(data) == 0:
        return False

    else: 
        mid = len(data)//2

        if data[mid] == el:
            return True
        else: 
            if el < data[mid]:
                return recursive_bsearch(data[:mid], el)
            else: 
                return recursive_bsearch(data[mid+1], el)


test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31]
print(recursive_bsearch(test_list, 1))