# WRITE YOUR SOLUTION HERE:
class Recording:
    def __init__(self, length: int):
        if length < 0:
            raise ValueError("Length of recording cannot be below 0.")
        self.__length = length

    # A getter method
    @property
    def length(self):
        return self.__length

    # A setter method
    @length.setter
    def length(self, new_length: int):
        if new_length >= 0:
            self.__length = new_length
        else:
            raise ValueError("Length of recording cannot be below 0.")
