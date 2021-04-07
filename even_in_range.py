print("Enter start number")
start = input()
print("Enter end number")
end = input()
for i in range(int(start) , int(end)+1):
    if(i % 2 == 0):
        print(i)