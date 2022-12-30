#Question: Write a function that asks a user for the number of days temperature reading was taken and the temperature on those days

days = int(input("How many day's temperature: "))
tempList = []
aboveAverage = 0
for i in range(days):
    temp = int(input("Day " + str(i+1) +"'s temperature: "))
    tempList.append(temp)

average = sum(tempList)/len(tempList)

for i in tempList:
    if i > average:
        aboveAverage += 1

print(f"\nAverage = {average}")
print(f"{aboveAverage} day(s) above average")
