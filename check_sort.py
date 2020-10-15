def main():
    n = input("Введите число: ")
    for i in range (len(n) - 1):
        if n[i] >= n[i+1]:
            print("ERROR: NUMBER ISN'T RIGHT")
            return
    print("EVERYTHING OK")

if __name__ == "__main__":
    main()