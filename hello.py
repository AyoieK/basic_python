while True:
    try:
        print("0) Exit")
        print("1) Hello, Student")
        print("2) Sum of Two Numbers")
        print("3) Rectangle Area")
        print("4) Average of 3 Scores")
        print("5) Temperature Convert (C → F)")
        print("6) Even or Odd")
        print("7) Positive / Negative / Zero")
        print("8) Max of Three")
        print("9) Simple Discount")
        print("10) BMI")

        choice = int(input())

        if choice == 0:
            break

        elif choice == 1:
            print("Hello, Student!")

        elif choice == 2:
            a, b = map(int, input().split())
            print(a + b)

        elif choice == 3:
            w, h = map(int, input().split())
            print(w * h)

        elif choice == 4:
            a, b, c = map(float, input().split())
            print(f"{(a + b + c) / 3:.2f}")

        elif choice == 5:
            c = float(input())
            print(c * 9 / 5 + 32)

        elif choice == 6:
            n = int(input())
            print("EVEN" if n % 2 == 0 else "ODD")

        elif choice == 7:
            n = int(input())
            if n > 0:
                print("POSITIVE")
            elif n < 0:
                print("NEGATIVE")
            else:
                print("ZERO")

        elif choice == 8:
            a, b, c = map(int, input().split())
            print(max(a, b, c))

        elif choice == 9:
            p = float(input())
            if p >= 1000:
                p *= 0.9
            print(f"{p:.2f}")

        elif choice == 10:
            w, h = map(float, input().split())
            print(f"{w / (h ** 2):.2f}")

        print()

    except:
        print()
        continue
