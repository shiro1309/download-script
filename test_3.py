values = [1, 2, 3, 4, 5, 6, 7]
slice_sizes = [3, 2, 2]  # slice sizes for each group

for i, size in enumerate(slice_sizes):
    start = sum(slice_sizes[:i])  # calculate starting index for this group
    end = start + size  # calculate ending index for this group
    total = sum(values[start:end])  # calculate sum for this group
    print(f"Sum of group {i+1}: {total}")
    
temp_data = []     
for i, size in enumerate(seasons):
    start = sum(seasons[:i]) 
    end = start + size
    temp_data.append(sum(episodes[start:end]))
print(temp_data)

season_num = 1
        #for i in range(len(episodes)):
        #    if count > episodes[i]:
        #        count -= episodes[i]
        #        season_num += 1
        #    else:
        #        break