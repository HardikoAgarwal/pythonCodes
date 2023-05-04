import sys
n=len(sys.argv) # total number of arguement
print("\ntotal arguement passed:",n) #arguement passed
print("\nname of the python script :",sys.argv[0])
print("\narguemnt passed:",end=" ")
for i in range(1,n):
    print(sys.argv[i],end=" ")

sum=0
for i in range(1,n):
    sum+=int(sys.argv[i])

print("\n\nresult:",sum)
print("\n\n\n\n")