# Sal's Shipping
# Diego Salcedo

weight = 41.5

# Ground Shipping
Flat_charge = 20.00
if weight <= 2.00:
  price_per_pound = 1.50
elif weight <= 6.00:
  price_per_pound = 3.00
elif weight <= 10.00:
  price_per_pound = 4.00
else:
  price_per_pound = 4.75

cost_ground = Flat_charge + price_per_pound * weight
cost_ground = f"{cost_ground:.2f}"
print(f"The cost of your shipment (Ground Shipping) is: ${cost_ground}\n")

# Ground Shipping Premium
cost_ground_premium = 125.00
cost_ground_premium = f"{cost_ground_premium:.2f}"
print(f"The cost of your shipment (Ground Shipping Premium) is: ${cost_ground_premium}\n")

# Drone Shipping
Flat_charge = 0.00
if weight <= 2.00:
  price_per_pound = 4.50
elif weight <= 6.00:
  price_per_pound = 9.00
elif weight <= 10.00:
  price_per_pound = 12.00
else:
  price_per_pound = 14.25

cost_drone = Flat_charge + price_per_pound * weight
cost_drone = f"{cost_drone:.2f}"
print(f"The cost of your shipment (Drone Shipping) is: ${cost_drone}\n")
