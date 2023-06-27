def binary_search(bogstaver, low, high, i):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If index is equal to the mid
        if mid == i:
            return bogstaver[mid]

        # If index is greater, ignore left half
        elif mid < i:
            return binary_search(bogstaver, mid + 1, high, i)

        # If index is smaller, ignore right half
        else:
            return binary_search(bogstaver, low, mid - 1, i)

    else:
        # Element is not present in the array
        return -1


bogstaver = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "æ", "ø", "å"]

# Test array
index = int(input("Det danske alfabet består af 29 bogstaver, skriv et tal mellem 1 og 29 og find det bogstav der er på den plads: "))

result = binary_search(bogstaver, 0, len(bogstaver)-1, index-1)

if result != -1:
    print("Bogstavet på den plads du tastede er:", result)
else:
    print("Du ramte ved siden af.... nu skal du dø!")

