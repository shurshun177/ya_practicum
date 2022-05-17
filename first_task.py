def del_zero(input_lst: list) -> list:
    result = [elem for elem in input_lst if elem]
    return result


if __name__ == '__main__':
    print(del_zero(input_lst=[0, 1, 0, 0, 4, 5, 7, 0, 0]))