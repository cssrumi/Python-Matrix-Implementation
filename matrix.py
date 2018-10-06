class Matrix:
    def __init__(self, *args: list):
        self.matrix = []
        self.columns = args[0].__len__()
        self.rows = 0
        for row in args:
            if row.__len__() == self.columns:
                self.matrix.append(row)
                self.rows += 1
            else:
                raise Exception("All rows should have the same size!")

    def transpose(self):
        new_matrix = []
        new_row = []
        for col_i in range(self.columns):
            for row_i in range(self.rows):
                new_row.append(self.matrix[row_i][col_i])
            new_matrix.append(new_row)
            new_row = []

        new_matrix = Matrix(*new_matrix)
        return new_matrix

    def determinant(self):
        if self.columns == self.rows:
            size = self.rows
            new_matrix = []
            delta = size
            for row in self.matrix:
                new_row = []
                for v in range(2*size - 1):
                    new_row.append(row[v-delta])
                new_matrix.append(new_row)
            new_matrix = Matrix(*new_matrix)
            result = 0
            size = new_matrix.rows
            delta = 0
            for i in range(size):
                temp = 1
                for j in range(size):
                    temp *= new_matrix.matrix[i+j-delta][i+j]
                delta += 1
                result += temp
            delta = 0
            for i in reversed(range(size)):
                temp = 1
                for j in range(size):
                    temp *= new_matrix.matrix[i-j-delta][i-j]
                delta += 1
                result -= temp
            return result
        else:
            raise Exception("To calculate determinant of the matrix "
                            "size of column and row should be the same")

    def __str__(self):
        result = ""
        for row in self.matrix:
            result += row.__str__() + '\n'
        # result = result.strip('\n')

        return result

    def __add__(self, other):
        if other.__class__ == self.__class__:
            if self.columns == other.columns and self.rows == other.rows:
                new_matrix = []
                for row_a, row_b in zip(self.matrix, other.matrix):
                    row = []
                    for a, b in zip(row_a, row_b):
                        row.append(a + b)
                    new_matrix.append(row)

                new_matrix = Matrix(*new_matrix)
                return new_matrix
            else:
                raise ValueError("Both Matrix should have the same size!")
        else:
            raise ValueError('"You can only add Matrix objects."')

    def __mul__(self, other):
        if other.__class__ == self.__class__:
            if self.columns == other.rows and self.rows == other.columns:
                other_t = other.transpose()
                new_matrix = []
                for row_a in self.matrix:
                    row = []
                    for row_b in other_t.matrix:
                        value = 0
                        for a, b in zip(row_a, row_b):
                            value += a * b
                        row.append(value)
                    new_matrix.append(row)

                new_matrix = Matrix(*new_matrix)
                return new_matrix
            else:
                raise ValueError("Wrong sizes of Matrix")
        else:
            raise ValueError('"You can only add Matrix objects."')
