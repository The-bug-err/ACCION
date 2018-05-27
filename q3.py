"""
String Manipulation
1. strip whitespace from the string.
2. remove duplicate characters if they are next to each other
"""
import os


class StringManipulator(object):
    def __init__(self, input_string):
        self.inStr = input_string

    def reformat_string(self):
        """
        Removes spaces and duplicate characters
        :return: The reformatted string
        """
        input_list = list(self.inStr)
        result_list = list()
        for char in input_list:
            if (result_list and char == result_list[-1]) or char == ' ':
                continue
            else:
                result_list.append(char)
        return ''.join(result_list)


if __name__ == '__main__':
    file_path = input('Enter the file path : ')
    if os.path.isfile(file_path):
        with open(file_path) as file:
            data = file.readlines()[0]
            op_data = StringManipulator(data).reformat_string()
            print(op_data)
