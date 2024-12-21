# Python compund interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle amount cannot be -ve or zero")
while rate <= 0:
    rate = float(input("Enter the rate of intrest: "))
    if rate <= 0:
        print("Rate of intrest cannot be -ve or zero")
while time <= 0:
    time = float(input("Enter the time period in years: "))
    if time <= 0:
        print("Time period cannot be 0 or -ve")

final_ammount = principle * (1+rate/100)**time   

print(f"The Final amount : {final_ammount:.2f}")