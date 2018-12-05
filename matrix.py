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
        
    def __repr__(self):
        return str(self.elems)
        
    def __getitem__(self, index):
        return self.elems[index]
        
    def __setitem__(self, index, value):
        self.elems[index] = value

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

        try:
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
                    raise ValueError
        
        except AttributeError:
            raise TypeError(f'Unsuported operation with type {}')

        return Matrix(result)
        
    def transpose(self):
        result = []
        
        for j in range(self.__n):
            line = []        
            
            for i in range(self.__m):
                line.append(self.elems[i][j])           
            result.append(line)
        
        return Matrix(result)
