"""
Justifying text
Given string and width, justify the string to fit the width.
"""
import os


class JustifyString(object):
    def __init__(self, file_data):
        self.column_width = int(file_data[0])
        self.data = file_data[1].split(' ')
        self.result_string = []
        self.current_line_words = []
        self.current_line_end_index = 0

    def create_string(self):
        self.current_line_end_index -= 1  # Remove the last space.
        extra_space_needed = self.column_width - self.current_line_end_index
        space_multiplier = 1 + extra_space_needed // (len(self.current_line_words)-1)
        remaining_space = extra_space_needed % (len(self.current_line_words)-1)
        space_word = ' ' * space_multiplier
        last_space = space_word + ' ' * remaining_space
        initial_string = space_word.join(self.current_line_words[:-1])
        final_string = initial_string + last_space + self.current_line_words[-1]
        return final_string

    def justify(self):
        for word in self.data:
            if self.current_line_end_index + len(word) < self.column_width:
                self.current_line_words.append(word)
                self.current_line_end_index += len(word) + 1    # Extra 1 added for space
            else:
                final_string = self.create_string()
                self.result_string.append(final_string)
                self.current_line_end_index = len(word) + 1
                self.current_line_words = [word]
        else:
            if len(self.current_line_words) == 1:
                space_to_add = ' '*(self.column_width - len(self.current_line_words[0]))
                text_to_add = self.current_line_words[0] + space_to_add
                self.result_string.append(text_to_add)
            else:
                self.result_string.append(self.create_string())

        return self.result_string


if __name__ == '__main__':
    file_path = input('Enter the file path : ')
    if os.path.isfile(file_path):
        with open(file_path) as file:
            data = file.readlines()
            result = JustifyString(data).justify()
            for text in result:
                print(text)
