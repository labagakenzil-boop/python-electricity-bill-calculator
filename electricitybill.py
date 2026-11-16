
# ELECTRICITY BILL CALCULATOR

print("")
print("       ELECTRICITY BILL SYSTEM")
print("")

# Get customer information
customer_name = input("Enter customer name: ")
meter_number = input("Enter meter number: ")

# Get electricity consumption
units = float(input("Enter units consumed (kWh): "))

# Cost per unit
rate = float(input("Enter cost per unit (Naira): "))

# Additional charges
service_charge = 500
vat_rate = 0.075

# Calculate electricity cost
electricity_cost = units * rate

# Calculate VAT
vat = electricity_cost * vat_rate

# Calculate total bill
total_bill = electricity_cost + vat + service_charge

# Display receipt
print("\n")
print("          ELECTRICITY RECEIPT")
print("")

print("Customer Name:", customer_name)
print("Meter Number:", meter_number)
print("Units Consumed:", units, "kWh")
print("Rate Per Unit: ₦", rate)

print("------------------------------------")
print("Electricity Cost: ₦", round(electricity_cost, 2))
print("Service Charge: ₦", service_charge)
print("VAT (7.5%): ₦", round(vat, 2))

print("------------------------------------")
print("TOTAL BILL: ₦", round(total_bill, 2))

print("Thank you for using our service!")
