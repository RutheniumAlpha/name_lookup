from algs import Binary_Search, Quick_Sort

output = []
show_only_existing_people = False

# 1. Take the names to be searched from the file
search = []
with open("search.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        val = line.replace("\n", "")
        search.append(val)

# 2. Take the data from the file
unsorted_names = []
with open("data/name_data.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        val = line.replace("\n", "")
        unsorted_names.append(val)

# 3. Sort it in ascending order (A-Z)
sorted_names = Quick_Sort.sort(unsorted_names)

# 4. Search for the values
for name in search:
    i = Binary_Search.search(sorted_names, 0, len(sorted_names) - 1, name)
    output.append(i != -1)

# 5. Print the output
print(
    f"                    ------- Output -------"
)
for i in range(len(output)):
    if show_only_existing_people:
        if output[i]:
            print(
                f"%30s: {output[i]}" % search[i]
            )
    else:
        print(
            f"%30s: {output[i]}" % search[i]
        )
