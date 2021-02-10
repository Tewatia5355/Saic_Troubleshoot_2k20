import numpy as np
arr = np.zeros((33,33,32))
iss = np.zeros((32,2,16))
def func(selling_team,purchasing_team,gun_code,gun_quantity,gun_price):

  if((selling_team<31 and selling_team>0)and(purchasing_team<31 and purchasing_team>0)and(gun_code>0 and gun_code<16)and(gun_quantity>0)and(gun_price>0)):
    arr[selling_team][31][0] = (gun_quantity*gun_price)
    arr[selling_team][32][0] = arr[selling_team][32][0] + arr[selling_team][31][0]
    arr[31][purchasing_team][0] = (gun_quantity*gun_price)
    arr[32][purchasing_team][0] = arr[32][purchasing_team][0] - arr[31][purchasing_team][0]
    arr[32][selling_team][0] = arr[selling_team][32][0]
    arr[purchasing_team][32][0] = arr[32][purchasing_team][0]
    iss[selling_team][0][gun_code] = iss[selling_team][0][gun_code] - gun_quantity
    iss[purchasing_team][0][gun_code] = iss[purchasing_team][0][gun_code] + gun_quantity
  else:
    print("Error in the given data maybe exceed in matrix limit\n")

print("Update gun matrix!!\n")
for i in range(1,6):
  print("Update team {i} gun_quantity and new balance\n".format(i=i))
  gcc = int(input("Update team net balance : "))
  iss[i][1][0] = gcc
  nog = int(input("Number of guns purchased : "))
  for j in range(1,nog+1):
      gcc = int(input("Gun code for team {i} : ".format(i=i)))
      gqq = int(input("Gun Quantity for gun code {gcc} for team {i} : ".format(gcc=gcc,i=j)))
      iss[i][0][gcc] = gqq
for i in range(1,32):
  arr[32][i][0] = iss[i][1][0]
  arr[i][32][0] = iss[i][1][0]
for i in range(1,32):
  print("{aa}\t{bb}\n".format(aa = arr[i][32][0],bb = arr[32][i][0]))
while(1):
  n = int(input("password/n"))
  if n==53555355 :
      print("Terminating\n")
      print("DATA Output of balance\n")
      for i in range(1,32):
          print("Team {i} Net Selling balance {bb} and Net Purchasing balance {cc} And Guns\n".format(i=i,bb=arr[i][32][0],cc=arr[32][i][0]))
          for j in range(1,16):
            print(" Gun Code {i} : {dd}/n".format(i=i,dd=iss[i][0][j]))
      break
  else:
    print("New update\n")
    s = int(input("Selling_team "))
    p = int(input("Purchasing_team "))
    gc = int(input("Gun_code "))
    gq = int(input("Gun_Quantity "))
    gp = int(input("Gun_Price "))
    func(s,p,gc,gq,gp)
    print("******UPDATED******")
