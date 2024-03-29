import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


duplicates = []
# # oof, O(n^2)
# # need to change the below to something more efficient
# # for name_1 in names_1:
# #     for name_2 in names_2:
# #         if name_1 == name_2:
# #             duplicates.append(name_1)

# bst = BinarySearchTree(names_1[0])
# for i in range(1, len(names_1)):
#     bst.insert(names_1[i])
# for i in range(len(names_2)):
#     if bst.contains(names_2[i]):
#         duplicates.append(names_2[i])

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

# O(n)
names_3 = names_1 + names_2
names_3.sort()
for i in range(len(names_1)-1):
    if names_1[i] == names_1[i+1]:
        duplicates.append(names_1[i])