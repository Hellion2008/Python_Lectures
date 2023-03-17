"""
Напишите программу для печати всех уникальных значений в словаре. 

Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 

Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""

d = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

all_vals = set()
for i in d:
    val_set = set(i.values())
    all_vals = all_vals.union(val_set)
    # all_vals |= val_set
print(all_vals)

# print(*set([list(d.values())[0] for d in dict]))