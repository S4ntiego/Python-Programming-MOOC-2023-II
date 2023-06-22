# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        current_max = 0
        number_to_return = my_list[0]
        for i in my_list:
            if my_list.count(i) > current_max:
                current_max = my_list.count(i)
                number_to_return = i
        return number_to_return

    @classmethod
    def doubles(cls, my_list: list):
        doubles = []
        for i in my_list:
            if my_list.count(i) > 1 and i not in doubles:
                doubles.append(i)
        return len(doubles)
