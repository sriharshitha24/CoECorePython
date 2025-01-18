project=int(input("Enter project score:"))
inte=int(input("Enter internal score:"))
ext=int(input("Enter external score:"))
if((project and inte and ext)>=50):
    total = 0.7 * project + 0.1 * inte + 0.2 * ext
    print("Total Marks obtained are ", total)
    if (total > 90):
        print("grade A")
    elif (total > 80):
        print("Grade B")
    else:
        print("Grade C")
else:
    if(ext<50):
        print("Failed in external")
    if(inte<50):
        print("Failed in internal")
    if(project<50):
        print("Failed in project")

