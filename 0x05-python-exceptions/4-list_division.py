#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    result = None
    for element in range(list_length):
        try:
            result = my_list_1[element] / my_list_2[element]
        except ZeroDivisionError:
            print("division by 0")
            my_list.append(0)
        except (ValueError, TypeError):
            print("wrong type")
            my_list.append(0)
        except IndexError:
            print("out of range")
            my_list.append(0)
        finally:
            my_list.append(result)
    return (my_list)
