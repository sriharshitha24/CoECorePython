basic=int(input('Basic Salary:'))
if(basic<10000):
    hra=0.67*basic
    da=0.73*basic
elif(basic>10000 & basic<20000):
    hra = 0.69 * basic
    da = 0.76 * basic
else:
    hra = 0.73 * basic
    da = 0.89 * basic
gs=hra+da+basic
print("Gross Salary:",gs)