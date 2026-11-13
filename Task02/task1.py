if __name__ == "__main__":
    sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

    sorted_list = sorted(sample_list, key=lambda x: x[-1])

    print("Original List:", sample_list)
    print("Sorted List:", sorted_list)
