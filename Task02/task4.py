if __name__ == "__main__":
    colors = ["Red", "Blue", "Black", "White", "Pink"]

    # Convert each string into a list of its individual characters
    result = list(map(list, colors))

    print("Original list of strings:")
    print(colors)
    print("\nConverted list of lists:")
    print(result)
