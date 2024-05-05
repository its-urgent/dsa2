size = int(input("Enter size of Hash Table : "))
array1 = [None] * size
array2 = [None] * size

def insert_linear_probing():
    data = int(input("Enter Telephone Number : "))
    count = 1
    index = data % size
    while array1[index] is not None:
        index = (index + 1) % size
        count += 1
    array1[index] = data
    print("Record inserted successfully.")

def insert_quadratic_probing():
    data = int(input("Enter Telephone Number : "))
    count = 1
    index = data % size
    while array2[index] is not None:
        index = (index + count**2) % size
        count += 1
        if count > size:
            print("Opps, Index Not Found....")
            return
    array2[index] = data
    print("Record inserted successfully.")

def display_linear_probing():
    print("Linear Probing: ")
    print(array1)

def display_quadratic_probing():
    print("Quadratic Probing: ")
    print(array2)

def search_linear_probing():
    data = int(input("Enter Telephone Number : "))
    count = 1
    index = data % size
    while array1[index] is not None:
        if array1[index] == data:
            print("Telephone Number Found ")
            print("Number of Comparisons in Linear Probing are : ", count)
            return
        index = (index + 1) % size
        count += 1
        if count > size:
            break
    print("Opps, Element Not Present")
    print("Number of Comparisons : ", count)

def search_quadratic_probing():
    data = int(input("Enter Telephone Number : "))
    count = 1
    index = data % size
    while array2[index] is not None:
        if array2[index] == data:
            print("Telephone number found ")
            print("Number of comparisons in Quadratic Probing are : ", count)
            return
        index = (index + count**2) % size
        count += 1
        if count > size:
            break
    print("No such Element Found")
    print("Number of comparisons : ", count)

while True:
    print("1. Linear Probing    2. Quadratic Probing    3. Exit")
    choice = int(input("Enter Choice : "))
    if choice == 1:
        while True:
            print("1. Insert    2. Search    3. Display    4. Back")
            linear_choice = int(input("Enter Choice : "))
            if linear_choice == 1:
                insert_linear_probing()
            elif linear_choice == 2:
                search_linear_probing()
            elif linear_choice == 3:
                display_linear_probing()
            elif linear_choice == 4:
                break
            else:
                print("Invalid Choice!")
    elif choice == 2:
        while True:
            print("1. Insert    2. Search    3. Display    4. Back")
            quadratic_choice = int(input("Enter Choice : "))
            if quadratic_choice == 1:
                insert_quadratic_probing()
            elif quadratic_choice == 2:
                search_quadratic_probing()
            elif quadratic_choice == 3:
                display_quadratic_probing()
            elif quadratic_choice == 4:
                break
            else:
                print("Invalid Choice!")
    elif choice == 3:
        break
    else:
        print("Invalid Choice!")
