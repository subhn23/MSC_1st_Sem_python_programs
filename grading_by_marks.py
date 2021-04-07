print("Enter marks scored in maths")
maths = input()
print("Enter marks scored in science")
science = input()
print("Enter marks scored in Social science")
ssc = input()
print("Enter marks scored in English")
english = input()
total = int(maths)+int(science)+int(ssc)+int(english)
print("Total Marks: " + str(total))
percent = total/400*100
print("Percent secured : " + str(percent) + "%")
print("Grade: ")
if(percent >= 80.0):
    print("A")
elif(percent<80.0 and percent >= 60.0):
    print("B")
elif(percent<60.0 and percent >= 50.0):
    print("C")
elif(percent<50.0 and percent >= 40.0):
    print("D")
elif(percent<40.0 and percent >= 33.0):
    print("E")
elif(percent<33.0):
    print("F")
else:
    print("Invalid mark")