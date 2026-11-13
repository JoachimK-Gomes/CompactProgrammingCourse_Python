if __name__ == "__main__":
    models = [
        {"make": " Google ", "model": 216, "color": "Black"},
        {"make": "Mi Max", "model": "2", "color": "Gold"},
        {"make": "Samsung", "model": 7, "color": "Blue"},
    ]

    # Sort alphabetically by 'color' (Black -> Blue -> Gold)
    sorted_models = sorted(models, key=lambda x: x["color"])

    print("Original list of dictionaries:")
    print(models)
    print("\nSorted list of dictionaries:")
    print(sorted_models)
