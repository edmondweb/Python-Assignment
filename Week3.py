# Writing a function named calculate_discount that accepts two parameters: price and discount_percent.

def calculate_discount(price, discount_percent):
    """
    Calculate the discounted price based on the original price and discount percentage.

    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to be applied.

    Returns:
    float: The price after applying the discount if the discount percent is 20 or more; 
    otherwise, the original price.
    """

    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

# Prompting the User for inputs

price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calling the calculate_discount function
final_price = calculate_discount(price, discount_percent)

print(f"The final price is: {final_price}")