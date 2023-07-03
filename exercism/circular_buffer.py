''' exercise circular buffer '''

class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.lst = [None for _ in range(capacity)]
        self.capacity = capacity
        self.oldest = 0
        self.newest = 0

    def read(self):
        if self.lst[self.oldest] is None:
            raise BufferEmptyException('Circular buffer is empty')
        value = self.lst[self.oldest]
        self.lst[self.oldest] = None
        self.oldest = self.add_one(self.oldest)
        return value

    def write(self, data):
        if self.oldest == self.newest and self.lst[self.newest] is not None:
            raise BufferFullException("Circular buffer is full")
        self.lst[self.newest] = data
        self.newest = self.add_one(self.newest)
        return data

    def overwrite(self, data):
        if self.lst[self.oldest] is None:
            raise BufferEmptyException('Circular buffer is empty')
        if self.oldest != self.newest:
            return self.write(data)
        self.read()
        return self.write(data)

    def clear(self):
        self.lst = [None for _ in range(self.capacity)]
        self.oldest = 0
        self.newest = 0

    def add_one(self, parameter):
        parameter += 1
        if parameter == self.capacity:
            parameter = 0
        return parameter

    def __repr__(self):
        repr = []
        for value in self.lst:
            if value is None:
                repr += '[ ]'
            else:
                repr += '[' + str(value) + ']'
        return repr  
    
