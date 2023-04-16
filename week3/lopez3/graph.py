class Graph:
    def __init__(self, n):
        self.adj_matrix = [[0 for x in range(n)] for x in range(n)]

    def add_edge(self, i, j, weight):
        self.adj_matrix[i][j] = weight
        self.adj_matrix[j][i] = weight

    def __str__(self):
        output = []
        for row in self.adj_matrix:
            output.append(' '.join([str(val) for val in row]))
            output.append('\n')
        return ''.join(output)
