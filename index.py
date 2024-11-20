def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying the discount.

    :param price: Original price of the item
    :param discount_percent: Discount percentage to apply
    :return: Final price after applying the discount, or the original price if discount < 20%
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the result
    if discount_percentage >= 20:
        print(f"The final price after applying a {discount_percentage}% discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price remains: ${original_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for the price and discount percentage.")
