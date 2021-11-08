"""
You work for a retail store that wants to increase sales on Tuesday and
Wednesday, which are the store's slowest sales days. On Tuesday and
Wednesday, if a customer's subtotal is greater than $50, the store will
discount the customer's purchase by 10%.
"""

from datetime import datetime

DISC_RATE = 0.10
SALES_TAX_RATE = 0.06

text = input("Please enter the subtotal: ")
subtotal = float(text)

current_date_and_time = datetime.now()

weekday = current_date_and_time.weekday()

# if the subtotal is greater than 50 and
# today is Tuesday or Wednesday, compute the discount.
if subtotal >= 50 and (weekday == 1 or weekday == 2):
    discount = round(subtotal * DISC_RATE, 2)
    print(f"Discount amount: {discount}")
    subtotal -= discount

# Compute the sales tax. Notice that we compute the sales tax
# after computing the discount because the customer does not
# pay sales tax on the full price but on the discounted price.
sales_tax = round(subtotal * SALES_TAX_RATE, 2)
print(f"Sales tax amount: {sales_tax}")

# Compute the total by adding the subtotal and the sales tax.
total = subtotal + sales_tax

# Display the total for the user to see.
print(f"Total: {total:.2f}")