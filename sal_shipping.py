#Ground Shipping
##
#Weight of Package	Price per Pound	Flat Charge
#2 lb or less	$1.50	$20.00
#Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
#Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
#Over 10 lb	$4.75	$20.00

#Ground Shipping Premium

#Flat charge: $125.00

#Drone Shipping

#Weight of Package	Price per Pound	Flat Charge
#2 lb or less	$4.50	$0.00
#Over 2 lb but less than or equal to 6 lb	$9.00	$0.00
#Over 6 lb but less than or equal to 10 lb	$12.00	$0.00
#Over 10 lb	$14.25	$0.00

weight = 8.40

if weight <= 2:
  cost_ground = weight * 1.50 + 20.00
elif weight <= 6:
  cost_ground = weight * 3.00 + 20.00
elif weight <= 10:
  cost_ground = weight * 4.00 + 20.00
else:
  cost_ground = weight * 4.75 + 20.00

print("ground shipping: " + str(cost_ground))

if weight <= 2:
  prem_cost = weight * 4.50 + 125.00
elif weight <= 6:
  prem_cost = weight * 9.00 + 125.00
elif weight <= 10:
  prem_cost = weight * 12 + 125.00
else:
  prem_cost = weight * 14.25 + 125.00

print("Drone Shipping: " + str(prem_cost))