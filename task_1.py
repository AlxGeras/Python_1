class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix(self.my_list)


m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [11, 12, 13]])
m_2 = Matrix([[5, 4, 3], [1, 2, 3], [7, 5, 3], [8, 5, 2]])
m_new = m + m_2
print(m_new)
