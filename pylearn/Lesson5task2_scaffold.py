def square_list(int_list):
    print('DEBUG: int_list',input_list)
    for i in range(len(int_list)):
        print('DEBUG: i',i)
        int_list[i] = int_list[i] ** 2
        print('DEBUG: int_list[i]', int_list[i])

    return int_list


if __name__ == "__main__":
    input_list = [1, 2, 3]
    assert square_list(input_list) == [1, 4, 9]

    input_list.append(4) # add 4 to end of previous list
    assert square_list(input_list) == [1, 4, 9, 16]