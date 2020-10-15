import random

def main():
    arr = []
    n = int(input("Введите число: "))
    for i in range (n):
        arr.append(random.randint(-10, 10))
    print(arr)
    for i in range (len(arr) - 2):
        print(arr[i], end=" 10")

if __name__ == "__main__":
    main()