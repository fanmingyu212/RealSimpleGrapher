import numpy as np


class Data(object):
    """ Saves data in a list of numpy.ndarray to save overhead time with appending to the data """
    def __init__(self, size=1000):
        self._data = []
        self._size = size
        self._index = 0

    def add_data(self, new_data):
        new_data_len = len(new_data)
        new_data = np.asarray(new_data)
        current_len = 0

        if len(self._data) > 0:
            if new_data_len - current_len <= self._size - self._index:
                data = new_data[current_len:]
                self._data[-1] = np.append(self._data[-1], data, axis=0)
                self._index += new_data_len - current_len
                current_len = new_data_len
            else:
                data = new_data[current_len:current_len+self._size-self._index]
                self._data[-1] = np.append(self._data[-1], data, axis=0)
                current_len += self._size - self._index
                self._index = self._size

        while current_len < new_data_len:
            if new_data_len - current_len <= self._size:
                data = new_data[current_len:]
                self._data.append(data)
                current_len = new_data_len
                self._index = new_data_len - current_len
            else:
                data = new_data[current_len:current_len+self._size]
                self._data.append(data)
                current_len += self._size
                self._index = self._size

    def row(self, row_num):
        value = np.array([])
        for kk in self._data:
            value = np.append(value, kk[:,row_num])
        return value

    def num_of_rows(self):
        if len(self._data) > 0:
            return len(self._data[0][0])
        else:
            return None