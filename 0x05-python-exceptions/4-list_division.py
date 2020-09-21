#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(list_length):
        try:
            r = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            r = 0
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
            r = 0
        except IndexError:
            print("out of range")
            r = 0
        finally:
            new.append(r)
    return new
