import math

# asks for the input the number of ppl attending and the num of hot dogs each person will be given
num_people = int(input("Enter the number of people attending the cookout: "))
num_hotdogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))

# Calculate the total number of hot dogs needed
num_hotdogs = num_people * num_hotdogs_per_person

# Calculate the number of packages of hot dogs needed
num_hotdog_packages = math.ceil(num_hotdogs / 10)

# Calculate the number of packages of hot dog buns needed
num_bun_packages = math.ceil(num_hotdogs / 8)

# Calculate the number of hot dogs left over
num_hotdogs_leftover = num_hotdog_packages * 10 - num_hotdogs

# Calculate the number of hot dog buns left over
num_buns_leftover = num_bun_packages * 8 - num_hotdogs

# Output the results
print("Minimum number of packages of hot dogs required:", num_hotdog_packages)
print("Minimum number of packages of hot dog buns required:", num_bun_packages)
print("Number of hot dogs left over:", num_hotdogs_leftover)
print("Number of hot dog buns left over:", num_buns_leftover)
