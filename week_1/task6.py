name = input("Enter customers full name: ")
unit = input("Enter units consumed (kwh): ")
units = int(unit)
cost_str = input("Enter the cost per unit in naira(#)")
cost_per_unit = float(cost_str)
total_bill = units * cost_per_unit
recepit =("***************\nELECTRICTY BILL\n***************\n"f"Customer Name:\t{name}\n"f"units consumed:\t{units}kwh\ncost per unit:\t"f"#{cost_per_unit}\n"f"Total Bill:\t#{total_bill}\n***************")
print(recepit)
