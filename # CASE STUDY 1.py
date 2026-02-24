# CASE STUDY 1
""" 
Problem Statement:
A grocery store wants to calculate the total cost of items purchased by a customer.
Calculate the total cost of 5 different items & each items can be taken in multiple numbers.
Add a 10% discount if the total exceeds Rs. 100.
Display the final payable amount.
"""

""" 
Program Requirements:
””Accept price input for 5 items.
Accept number of units for each items.
- Calculate total cost.
- Apply 10% discount if total > Rs. 100.
- Display Original Total, Discount (if applicable), and Final Amount.
- Use proper indentation and comments.
"""

#declaring variable
items = 5
total_cost = 0

w
print("Enter details for 5 items:")
for i in range(items):
    price = float(input(f"Enter price of item {i+1}: "))
    quantity = int(input(f"Enter quantity of item {i+1}: "))
    total_cost += price * quantity

#printing the original total 
print(f"\nOriginal Total: Rs. {total_cost:.2f}")

# applying discount
discount = 0
if total_cost > 100:
    discount = total_cost * (0.10)
    final_amount = total_cost - discount
    print(f"Discount (10%): Rs. {discount:.2f}")
else:
    final_amount = total_cost
    print("No discount applicable")



print(f"Final  Amount: Rs. {final_amount:.2f}")
