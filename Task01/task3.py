if __name__ == "__main__":
    # 1. Convert an integer to a floating-point number
    num_int = 10
    converted_float = float(num_int)
    print("1. Integer to float:", converted_float, "| Type:", type(converted_float))

    # 2. Convert a floating-point number to an integer
    num_float = 10.75
    converted_int = int(num_float)
    print("2. Float to integer:", converted_int, "| Type:", type(converted_int))

    # 3. Convert an integer to a string
    num_to_str = 42
    converted_str = str(num_to_str)
    print("3. Integer to string:", converted_str, "| Type:", type(converted_str))

    # 4. Convert a string containing a number to an integer
    str_num = "123"
    converted_from_str = int(str_num)
    print("4. String to integer:", converted_from_str, "| Type:", type(converted_from_str))

    # 5. Convert an integer to a Boolean
    int_bool = 1
    converted_bool = bool(int_bool)
    print("5. Integer to boolean:", converted_bool, "| Type:", type(converted_bool))

    # Factorial calculation
    n = int(input("\nEnter a non-negative integer to calculate its factorial: "))
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"The factorial of {n} is: {factorial}")
