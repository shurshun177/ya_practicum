def get_specific_elements(lst_1: list, lst_2: list) -> list:
    result = [i for i in lst_1 if i not in lst_2]
    return result


if __name__ == '__main__':
    print(
        get_specific_elements(
            lst_1=[0, 1, 0, 0, 4, 5, 7, 0, 0],
            lst_2=[0, 5]
        )
    )