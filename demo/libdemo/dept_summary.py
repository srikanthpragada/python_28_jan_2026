
with open("employees.txt", "rt") as f:
    for line in f.readlines():
        parts = line.strip().split(",")
        dept_name = parts[0]

        # take names
        employees = ",".join(parts[1::2])

        # take salaries
        total_salary = sum(map(int, parts[2::2]))
        print(f"{dept_name:10} {total_salary:8}  {employees}")

