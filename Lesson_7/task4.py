"""
Створити список із днями тижня.
В один рядок (або як вам зручно) створити словник такого виду: {1: "Monday", 2: "Tuesday", ...}
Також в один рядок (або іншим способом) створити зворотний словник: {"Monday": 1, "Tuesday": 2, ...}"""

week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(week_days)

dct1 = {k: week_days[k-1] for k in range(1, 8)}
print(dct1)

dct2 = {k: week_days.index(k)+1 for k in week_days}
print(dct2)


