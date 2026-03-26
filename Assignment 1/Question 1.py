# def computepay(hours_worked, hourly_rate, bonus, tax_rate):
#     if hours_worked > 40:
#         total_pay = (hours_worked - 40) * 1.5 * hourly_rate + 40 * hourly_rate + bonus
#     else:
#         total_pay = hours_worked * hourly_rate + bonus
#     net_pay = total_pay * (1 - tax_rate / 100)
#     return net_pay
#
# try:
#     hours_worked = float(input("Enter your hours: "))
#     hourly_rate = float(input("Enter your rate: "))
#     bonus = float(input("Enter your bonus: "))
#     tax_rate = float(input("Enter your tax rate (percent): "))
#
#     print("Pay:", computepay(hours_worked, hourly_rate, bonus, tax_rate))
# except:
#     print("Error, please enter numeric input.")
#
#
#
#
#

age = int(input("Enter age: "))
if 15 <= age < 18:
    weight = float(input("Enter weight (kg): "))
if (age >=18 or age>=15 and weight >=55):
    print("The medicine can be used.")
else:
    print("The medicine cannot be used.")
