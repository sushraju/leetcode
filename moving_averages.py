#!/usr/bin/env python

"""
Moving Averages with a specific window size.
"""


class MovingAverages():
    """
    Moving Averages with a specific window size.
    """

    def __init__(self, window_size):
        """
        Initialize values with window size and set the insert_position to 0
        :param window_size:
        """
        assert (window_size > 0), "Window size should be > 0 !!!"

        self._window_size = window_size
        self._values = [0] * window_size
        self._insert_position = 0

    def add_value(self, value):
        """
        Add the value to the values list and increment the position until the window gets filled
        After that drop the first and append to the end.
        :param value:
        :return:
        """
        if self._insert_position < self._window_size:
            self._values[self._insert_position] = value
            self._insert_position += 1
        else:
            self._values.pop(0)
            self._values.append(value)

    def get_average(self):
        """
        Returns the moving average using the sum and insert position.
        Once the window gets filled, the insert position is always same as the window size
        :return:
        """
        sum_values = 0
        mov_avg = 0.0
        for i in range(self._insert_position):
            sum_values = sum_values + self._values[i]

        if sum_values > 0 and self._insert_position > 0:
            mov_avg = sum_values / self._insert_position

        return mov_avg

    def get_values(self):
        """
        getters, returns the values list
        :return:
        """
        return self._values


def main():
    """
    Driver code
    :return:
    """
    mov_avg = MovingAverages(6)
    value_list = [23, 45, 34, 56, 78, 98, 9, 90, 45, 18, 99, 85, 91, 101, 97, 110, 100, 92, 81, 77, 73, 69, 85]

    for value in value_list:
        mov_avg.add_value(value)
        print(mov_avg.get_values(), "%.2f" % mov_avg.get_average())

    # values and the moving average.
    # [23, 0, 0, 0, 0, 0] 23.00
    # [23, 45, 0, 0, 0, 0] 34.00
    # [23, 45, 34, 0, 0, 0] 34.00
    # [23, 45, 34, 56, 0, 0] 39.50
    # [23, 45, 34, 56, 78, 0] 47.20
    # [23, 45, 34, 56, 78, 98] 55.67
    # [45, 34, 56, 78, 98, 9] 53.33
    # [34, 56, 78, 98, 9, 90] 60.83
    # [56, 78, 98, 9, 90, 45] 62.67
    # [78, 98, 9, 90, 45, 18] 56.33
    # [98, 9, 90, 45, 18, 99] 59.83
    # [9, 90, 45, 18, 99, 85] 57.67
    # [90, 45, 18, 99, 85, 91] 71.33
    # [45, 18, 99, 85, 91, 101] 73.17
    # [18, 99, 85, 91, 101, 97] 81.83
    # [99, 85, 91, 101, 97, 110] 97.17
    # [85, 91, 101, 97, 110, 100] 97.33
    # [91, 101, 97, 110, 100, 92] 98.50
    # [101, 97, 110, 100, 92, 81] 96.83
    # [97, 110, 100, 92, 81, 77] 92.83
    # [110, 100, 92, 81, 77, 73] 88.83
    # [100, 92, 81, 77, 73, 69] 82.00
    # [92, 81, 77, 73, 69, 85] 79.50


if __name__ == "__main__":
    main()
