import csv

with open("payroll.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Name", "Basic", "HRA", "Total"])

    n = int(input("Enter number of employees: "))

    for i in range(n):
        name = input("Enter employee name: ")
        basic = int(input("Enter basic salary: "))

        hra = basic * 0.20
        total = basic + hra

        w.writerow([name, basic, hra, total])

with open("payroll.csv", "r") as f:
    r = csv.reader(f)

    print("\nPayroll Details:")
    for row in r:
        print(row)