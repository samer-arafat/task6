# Q1
lst = [30, 75, 9, 97, 50, -4, 70, 59]
print(lst[3])
print(lst.remove(-4))
print(lst)
lst.sort()
print(lst)
print(lst[3:8])

# Q2
main_lst = [["python", 3], [5, 7.8], ["python", 11], ["python",1]]
print(main_lst.count(['python']))
# print(len(main_lst))

# Q3
my_lst = ["I", "LOvE", "GAZa", "sKy", "GEEks"]
my_n_lst = str(my_lst)
print(my_n_lst.title())

# Q4
my_lst = [12, 3.8, "GSG", ["sKy", "zak"]]
print(my_lst[:])

# Q5
my_lst = ["GSG", "zakaria", 19, 9.8, "Omar"]
n_lst = ["GSG", "zakaria", "Omar", 9.8, 19]
print(n_lst)
# Q6
nums = [33, 5.9, 6, -43, 9, 7, 39, 0, -40]
print(sum(nums))

# Q7
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
n_tuble = tuple1 + (9,)
print(n_tuble)

# Q8
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple2 = ('Java', 'C++', 7.8)

tuble3 = tuple1 + tuple2
print(tuble3)