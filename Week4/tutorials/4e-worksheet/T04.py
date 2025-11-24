def bill(cost):
    final_cost = (cost * 1.10) * 1.08
    return final_cost

meal_cost = 10.80
final_bill = bill(meal_cost)
final_bill = round(final_bill, 2)
print(f"Final bill: ${final_bill}")
