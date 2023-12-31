def fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")


def main():
    fahrenheit()


if __name__ == "__main__":
    main()
