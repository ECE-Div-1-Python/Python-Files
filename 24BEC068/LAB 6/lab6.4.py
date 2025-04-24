def sort_food_prices():
    items = [("Burger", 150), ("Pizza", 300), ("Pasta", 250), ("Sandwich", 100), ("Fries", 80)]
    print("Original List:", items)

    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)

    print("Sorted List (by price descending):")
    for item in sorted_items:
        print(item[0], "\t", item[1])

sort_food_prices()
