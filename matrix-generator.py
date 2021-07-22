def generate_vector_c(c,n):
    vector = []
    for k in range(2*n+1):
        kth_value = min(k, 2*n-k, c)
        result = format(kth_value, "02d")
        print(result, end = " ")
        vector.append(kth_value)
    return vector
def generate_matrix_n(n):
    matrix = []
    for i in range(n+1):
        vector = generate_vector_c(i, n)
        print("\n")
        matrix.append(vector)
    return matrix
def main():
    value = int(input("Insert an integer value between 0 and 99: "))
    if value < 0 or value > 99:
        print("The input number is invalid")
        return 0
    generate_matrix_n(value)
main()
