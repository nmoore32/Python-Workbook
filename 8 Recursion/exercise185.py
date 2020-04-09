##
# Decompresses a run-length encoded list
#


# Decompresses a run-length encoded list
# @param l the list to be decompressed
# @return a decompressed version of l
def decompress(l):
    # If the list is empty, return the empty list
    if l == []:
        return []

    # If the list has at least 2 entries in it, check to see if the next is an integer
    if len(l) > 1:
        if type(l[1]) == int:
            # If the next entry is an integer, add that many copies the current entry then
            # decompress the remainder of the list after the integer
            return [l[0]] * l[1] + decompress(l[2:])
    else:
        # Return the last item on the list
        return [l[0]]


# Test decompress
def main():
    testlist = ["A", 12, "B", 4, "A", 6, "B", 1]
    print(decompress(testlist))


# Call the main function
main()
