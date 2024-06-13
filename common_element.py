def find_common_elements(list1, list2):
    common_elements = set(list1) & set(list2)
    if common_elements:
        print("Common elements:", list(common_elements))
    else:
        print("No common elements found.")

# Example usage:
list1 = input("Enter elements of the first list separated by spaces: ").split()
list2 = input("Enter elements of the second list separated by spaces: ").split()

find_common_elements(list1, list2)
