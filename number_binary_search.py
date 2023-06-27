try_counter = 0

def binary_search(tal_array, target):
    global try_counter
    low = 0
    high = len(tal_array) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = tal_array[mid]
       

        if guess == target:
            return mid
        if guess > target:
            try_counter += 1
            high = mid - 1
        else:
            try_counter += 1
            low = mid + 1
    return -1

# Testing the function
tal_array = []

for i in range(1,10001):
    tal_array.append(i)

target = int(input("Skriv et tal som du ønsker at algoritmen skal finde i en liste med tallene fra 1 til 10.000: "))

result = binary_search(tal_array, target)

if result != -1:
    print("der blev brugt", try_counter , " forsøg på at finde dit tal")
    print("tallet som du vil finde ligger på index(plasering):", result, "på listen.")
else:
    print("Du ramte ved siden af.... nu skal du dø!")