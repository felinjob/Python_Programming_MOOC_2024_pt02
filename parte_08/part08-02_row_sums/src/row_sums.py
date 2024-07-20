# Write your solution here
def row_sums(my_matrix: list):
    for row in range(len(my_matrix)):
        my_matrix[row].append(sum(my_matrix[row]))

if __name__ == "__main__":
    row_sums()