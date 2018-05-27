"""
4 Spiral printing
A function to print a 2-D array (n x m) in spiral order (clockwise).
"""
import os


class SpiralPrinter(object):
    def __init__(self, file_data):
        self.data = []
        for row in file_data:
            self.data.append(row.strip().split(' '))
        self.row_max = len(self.data) - 1
        self.col_max = len(self.data[0]) - 1
        self.row_increment = 1
        self.col_increment = 1
        self.row_start = 0
        self.col_start = 0

    def traverse_matrix_clockwise(self):
        """
        :return: The matrix elements traversed in clockwise as a list
        """
        result_list = list()
        while self.row_start <= self.row_max or self.col_start <= self.col_max:
            if self.row_start <= self.row_max:
                for i in range(self.col_start, self.col_max + 1, self.col_increment):
                    result_list.append(self.data[self.row_start][i])

                self.row_start += 1
                # Reversing the sign to go back in matrix the next time
                self.col_increment = -self.col_increment

            if self.col_start <= self.col_max:
                # Traverse the Last Available Column (Up -> Down)
                for i in range(self.row_start, self.row_max + 1, self.row_increment):
                    result_list.append(self.data[i][self.col_max])

                # This time the last available column was printed, so decrement the value by 1
                self.col_max -= 1
                # Reverse the sign to go up the matrix the next time
                self.row_increment = -self.row_increment

            if self.row_start <= self.row_max:
                # Traverse the Last Available Row (Right -> Left)
                for i in range(self.col_max, self.col_start - 1, self.col_increment):
                    result_list.append(self.data[self.row_max][i])

                # The last available row printed, decrement the value by 1
                self.row_max -= 1
                # Reversing the sign to go front in matrix the next time
                self.col_increment = -self.col_increment

            if self.col_start <= self.col_max:
                # Traverse the First Available Column (Down -> Up)
                for i in range(self.row_max, self.row_start - 1, self.row_increment):
                    result_list.append(self.data[i][self.col_start])

                self.col_start += 1
                self.row_increment = -self.row_increment

        return result_list


if __name__ == '__main__':
    file_path = input('Enter the file path : ')
    if os.path.isfile(file_path):
        with open(file_path) as file:
            data = file.readlines()
            spiral_instance = SpiralPrinter(data)
            spiral_result = spiral_instance.traverse_matrix_clockwise()
            print(" ".join(spiral_result))
