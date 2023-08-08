# Find the Duplicate Number in given list:
# l1 = [1, 3, 5, 7, 1, 3, 2, 9, 8, 1]
# char_count = {}
# # unique_list =[]
# # duplicate_list=[]
# # for i in l1:
# #     if i not in unique_list:
# #         unique_list.append(i)
# #     elif i not in duplicate_list:
# #         duplicate_list.append(i)
# #
# # print(duplicate_list)
# # print(sorted(unique_list))

# WAP how many times given list l1 number repeated:
# for char in l1:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
#
# for char, count in char_count.items():
#     print(f"The Number '{char}' is repeated '{count}' times.")

# Find the emp_name and print the first character of it:
d1 = {"1": {"emp_name": "Naveen"}, "2": {"emp_name": "Deepak"}, "3": {"emp_name": "Saisha"}, "4": {"emp_name": "Rahul"}}
for emp_id, emp_data in d1.items():
    emp_name = emp_data["emp_name"]
    first_letter = emp_name[0]
    print(f"Employee {emp_id}: First letter of name is {first_letter}")
