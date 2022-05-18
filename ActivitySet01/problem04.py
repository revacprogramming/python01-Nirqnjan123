# Conditional Execution

hrs = float(input("Enter Hours:"))
rate=float(input("Enter rate:"))
pay=hrs*rate;
if hrs>40:
    grasspay=pay+(hrs-40)*(rate*0.5);
else:
    grasspay=pay;
print(grasspay);

