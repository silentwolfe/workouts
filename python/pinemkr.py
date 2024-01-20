# Recieve inputs from the user on the size of tree
tree_height = int(input("How tall is the tree: "))
sec_tree_height = tree_height
# initialize the variables needed for creating the spaces and the hashes
spaces = tree_height - 1
hashes = 1
stump = spaces

# use a loop to iterate through the size inputted by the user
while tree_height != 0:

# print the spaces
    for i in range(spaces):
        print(" ", end="")

# print the hashes
    for j in range(hashes):
        print("#", end="")
    
    print()

    spaces -= 1
    hashes += 2
    tree_height -= 1
    
for i in range(stump):
    print(" ", end="")
print("#")
if sec_tree_height >= 10:
    for i in range(stump):
        print(" ", end="")
    print("#")