all_students = []
winter_15 = []
spring_15 = []
summer_15 = []
tas = []

cohort_data = open("cohort_data.txt")

for line in cohort_data:
    line.rstrip()
    tokens = line.split("|")
    cohort = tokens[4].strip()
    name = tokens[0].strip() + " " + tokens[1].strip()
    print cohort, name

    if cohort == "TA":
        tas.append(name)
    elif cohort == "Winter 2015":
        winter_15.append(name)
    elif cohort == "Spring 2015":
        spring_15.append(name)
    elif cohort == "Summer 2015":
        summer_15.append(name)

print winter_15

winter_15.sort()
print winter_15

spring_15.sort()
summer_15.sort()
tas.sort()
all_students = [winter_15, spring_15, summer_15, tas]
cohort_data.close()        

print all_students