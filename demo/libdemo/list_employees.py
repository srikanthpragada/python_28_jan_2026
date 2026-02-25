import json

employees = json.load(open("employees.json", "rt"))

for emp in employees:
    print(f"{emp["empname"]:20}  {emp["salary"]:6}")

