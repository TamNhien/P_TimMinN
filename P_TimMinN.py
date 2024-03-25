A = float(input("Nhập vào giá trị A : "))

n, sum_terms = 1, 0
while (sum_terms := sum_terms + 1/n) <= A:
    n += 1

print("Giá trị của n nhỏ nhất sao cho tổng 1 + 1/2 + 1/3 + ... + 1/n lớn hơn", A, "là : ", n - 1)

