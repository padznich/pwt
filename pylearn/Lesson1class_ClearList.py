list_to_clear = ["-", "1", "-", "2", "-", "3", "4", "5", "-", "6"]
#list_to_clear = []

def clear(list_to_clear):

# METHOD 1 "At Lesson1"
    dict1 = {}
    for w in list_to_clear:
        dict1[w] = None

    output_list1 = []
    for w in dict1:
        output_list1.append(w)
    print(list_to_clear)
    print(output_list1)

# METHOD 2 "Unique iteration"
    output_list2 = []
    for x in set(list_to_clear):
        output_list2.append(x)
    print(output_list2)

clear(list_to_clear)