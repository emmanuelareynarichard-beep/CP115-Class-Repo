# Escape Characters Exercise
# Print the receipt shown in the lab, using \n for new lines and \t for columns.
# Calculate every total, subtotal, and tax in your code. Do not type the money
# amounts in directly. Show every amount with exactly two decimal places.
total_Coffee = 3.50*2
total_Muffin =2.10*3
total_Water = 1.05*4
Subtotal = float(total_Coffee + total_Muffin + total_Water )
Tax = float(Subtotal*0.06)
Total = float(Subtotal + Tax)
print(f"==========Receipt==========\n\nItem\tPrice\tQty\tTotal\nCoffee\t$3.50\t2\t${total_Coffee}\nMuffin\t$2.10\t3\t${round(total_Muffin,2)}\nWater\t$1.05\t4\t{total_Water}\n\n------------------------------\n\nSubtotal\t${Subtotal}\nTax (6%)\t${Tax}\nTotal\t\t${Total}\n==========================")