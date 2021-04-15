def most_frequent():
    s = input("Enter the String : ")
    counter = {}
    for char in s:
        if char in counter:
            counter[char] += 1 
        else:
            counter[char] = 1
    print(counter.items())
most_frequent()
