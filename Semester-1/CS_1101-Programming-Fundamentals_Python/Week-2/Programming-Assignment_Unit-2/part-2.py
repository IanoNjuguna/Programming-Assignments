#!/bin/python3

def catalogue(item1, item2, item3):
# Define the prices for individual items
    item1_price = 200.0
    item2_price = 400.0
    item3_price = 600.0

    # Calculate the total cost without any discounts
    total_cost = item1 * item1_price + item2 * item2_price + item3 * item3_price

    # Check if the customer is purchasing a combo pack with two unique items
    if item1 > 0 and item2 > 0 and item3 == 0:
        # Apply a 10% discount for the combo pack
        total_cost *= 0.9
        #combo_2 = (total_cost * 0.9)

    # Check if the customer is purchasing a gift pack
    if item1 > 0 and item2 > 0 and item3 > 0:
        # Apply a 25% discount for the gift pack
        total_cost *= 0.75

    print("Online Store")
    print("------------------------------")
    print("Product(S)\t\tPrice")
    print(f"Item 1\t\t\t{item1_price}")
    print(f"Item 2\t\t\t{item2_price}")
    print(f"Item 3\t\t\t{item3_price}")
    print(f"Combo 1(Item 1 + 2)\t540.0")
    print(f"Combo 2(Item 2 + 3)\t900.0")
    print(f"Combo 3(Item 1 + 3)\t720.0")
    print(f"Combo 4(Item 1 + 2 + 3)\t900.0")
    print("------------------------------")
    print("For delivery Contact:98764678899")

catalogue(1,2,3)
