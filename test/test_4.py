#def get_slice_index(number, slice_sizes, start_index=0):
#    total = 0
#    for i, size in enumerate(slice_sizes):
#        if start_index > i:
#            total += size
#        elif number <= size - total:
#            return i, total + number
#        else:
#            total += size
#    return len(slice_sizes) - 1, slice_sizes[-1] - 1

def get_slice_index(number, slice_sizes):
    # i is just from 0 to large number but size is the number i on the slice_sizes
    for i, size in enumerate(slice_sizes):
        if number <= size:
            return i , number
        number -= size
    
        
        
        


slice_sizes = [2, 2, 2, 2, 2]
number = 10
start_index = 0

slice_index, index_within_slice = get_slice_index(number, slice_sizes)
print(f"Slice index: {slice_index}, Index within slice: {index_within_slice}")
