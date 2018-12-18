import operator


class Matrix:
    def __init__(self, elems):
        self.elems = elems
        self.__m = len(self.elems)
        self.__n = len(self.elems[0])
        self._shape = (self.__m, self.__n)
        self._size = self.__m * self.__n
        
    @property
    def size(self):
        return self._size
        
    @property
    def shape(self):
        return self._shape

    def __str__(self):
        cls = self.__class__.__name__
        return f'{cls}({str(self.elems)})'

    __repr__ = __str__
        
    def __getitem__(self, index):
        return self.elems[index]
        
    def __setitem__(self, index, value):
        self.elems[index] = value

    def __contains__(self, item):
        if item in self.elems:
            return True
        return False

    def __iter__(self):
        for elem in self.elems:
            yield elem

    def _fn_base(self, other, op):
        if other.__m == self.__m and other.__n == self.__n:
            result = []
            for i in range(other.__m):
                lst = []
                for j in range(other.__n):
                    lst.append(op(self.elems[i][j], other.elems[i][j]))
                result.append(lst)
            return Matrix(result)

    def __add__(self, other):
        return self._fn_base(other, operator.add)

    def __sub__(self, other):
        return self._fn_base(other, operator.sub)            
    
    def __mul__(self, other):
        result = []
        if type(other) == int:
            for i in range(self.__m):
                line = []
                for j in range(self.__n):
                    line.append(self.elems[i][j] * other)
                result.append(line)
        else:
            if self.__n == other.__m:
                for i in range(self.__m):
                    line = []
                    sum = 0
                    while len(line) < self.__m:
                        for j in range(self.__n):
                            sum += self.elems[i][j] * other.elems[j][i]    
                        line.append(sum)    
                    result.append(line)
            else:
                raise ValueError('Matrices of shape {} and {}'
                    .format(self.shape, other.shape))
        return Matrix(result)
        
    def transpose(self):
        result = []
        for j in range(self.__n):
            line = []                    
            for i in range(self.__m):
                line.append(self.elems[i][j])           
            result.append(line)        
        return Matrix(result)


if __name__ == "__main__":
    matrix = Matrix([[1,2,3], [4,5,6]])
    matrix2 = Matrix([[3,4,6], [8,10,11]])
    matrix3 = Matrix([[5,-4],[6,2],[0,7]])

    print(matrix)
    print(matrix.shape)

    for i in matrix.elems:
        for j in i:
            print(j)
    
    print(5 in matrix)
    print(5 in matrix[1])
    print(matrix2 + matrix)
    print(matrix2 - matrix)
    print(matrix * matrix3)
    print(matrix * 2)
    print(matrix * 'a')
