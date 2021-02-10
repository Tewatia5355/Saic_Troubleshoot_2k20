import numpy as np
import pandas as pd
import xlsxwriter
df = pd.read_excel('trblshoot_R1.xlsx',sheet_name='MAIN')
arr = np.zeros((34,34,32),dtype = 'O')
iss = np.zeros((32,18),dtype = 'O')
iss[1][0] = 'USA'
iss[2][0] = 'UK'
iss[3][0] = 'RUSSIA'
iss[4][0] = 'FRANCE'
iss[5][0] = 'GERMANY'
iss[6][0] = 'CHINA'
iss[7][0] = 'INDIA'
iss[8][0] = 'JAPAN'
iss[9][0] = 'SYRIA'
iss[10][0] = 'ISRAEL'
iss[11][0] = 'PAKISTAN'
iss[12][0] = 'ITALY'
iss[13][0] = 'SOUTH-KOREA'
iss[14][0] = 'IRAQ'
iss[15][0] = 'IRAN'
iss[16][0] = 'JORDAN'
iss[17][0] = 'COLUMBIA'
iss[18][0] = 'ROMANIA'
iss[19][0] = 'VENEZUELA'
iss[20][0] = 'PALESTINE'
iss[21][0] = 'SRI-LANKA'
iss[22][0] = 'CUBA'
iss[23][0] = 'CANADA'
iss[24][0] = 'AUSTRALIA'
iss[25][0] = 'BRAZIL'
iss[26][0] = 'SAUDI-ARABIA'
iss[27][0] = 'AFGHANISTAN'
iss[28][0] = 'MEXICO'
iss[29][0] = 'TURKEY'
iss[30][0] = 'CONGO'
iss[31][0] = 'SAIC'
iss[0][1] =  'UZI'
iss[0][2] =  'AK-47'
iss[0][3] =  'GLOCK'
iss[0][4] =  'AXM-25'
iss[0][5] =  'INSAS'
iss[0][6] =  'COLT1911'
iss[0][7] =  'M4A1'
iss[0][8] =  'BERETTA M461'
iss[0][9] =  'BIZON'
iss[0][10] =  'A550'
iss[0][11] =  'RGD-5'
iss[0][12] =  'RKG3'
iss[0][13] =  'TM-57'
iss[0][14] =  'POM2'
iss[0][15] =  'RPK-74'
iss[0][16] = 'Net Cash Available'
iss[0][17] = 'Net Worth from Weapons'

for i in range(1,32):
    arr[0][i][0] = iss[i][0]
    arr[i][0][0] = iss[i][0]
for i in range(1,16):
    arr[0][0][i*2 - 1] = iss[0][i]

ggpp = (0,475000,300000,125000,1000000,150000,225000,575000,175000,350000,750000,5000,75000,62500,25000,237500)
pp = (237500,150000,62500,500000,75000,112500,287500,87500,175000,375000,2500,37500,31250,12500,118750)
ss = (593750,375000,156250,1250000,187500,281250,718750,218750,437500,937500,6250,93750,78125,31250,296875)
def inp():
    while True:
        try:
          n = int(input())
          break
        except ValueError:
          print("Not a valid integer! Please try again ...")
    return n
dff = pd.read_excel('SHEET.xlsx',sheet_name='Sheet1')
wil = np.zeros((32,16),dtype = 'O')
for i in range(1,30):
  for j in range(1,16):
    wil[i][j] = dff.iloc[i-1][j]

def func(selling_team,purchasing_team,gun_code,gun_quantity,gun_price):
  if((selling_team<32 and selling_team>0)and(purchasing_team<32 and purchasing_team>0)and(gun_code>0 and gun_code<16)and(gun_quantity>0)and(gun_price>0) and (iss[selling_team][gun_code] >= gun_quantity)and(iss[purchasing_team][16]>=(gun_price*gun_quantity))):
    arr[selling_team][purchasing_team][2*gun_code - 1] += gun_quantity
    arr[selling_team][purchasing_team][2*gun_code] = gun_price  
    arr[32][purchasing_team][0] = (gun_quantity*gun_price)
    arr[33][purchasing_team][0] -=  arr[32][purchasing_team][0]
    arr[selling_team][32][0] = (gun_quantity*gun_price)
    arr[selling_team][33][0] +=  arr[selling_team][32][0]
    arr[33][selling_team][0] = arr[selling_team][33][0]
    arr[purchasing_team][33][0] = arr[33][purchasing_team][0]
    iss[selling_team][16] = arr[selling_team][33][0]
    iss[purchasing_team][16] = arr[33][purchasing_team][0]
    iss[selling_team][gun_code] -= gun_quantity
    iss[purchasing_team][gun_code] += gun_quantity
  else:
    print("Error in the given data maybe exceed in matrix limit\n")
print("Updating gun matrix!!\n")
for i in range(1,31):
  iss[i][16] = df.iloc[i][18]
  for j in range(1,16):
      iss[i][j] = df.iloc[i][j]
for i in range(1,32):
  arr[33][i][0] = iss[i][16]
  arr[i][33][0] = iss[i][16]
for i in range(1,32):
  print("Team {i} Net balance : {aa}\n".format(i=i,aa = arr[i][33][0]))
while(1):
  print("Password\n")
  n = inp()
  if n==53555355 :
      writer = pd.ExcelWriter('file.xlsx', engine='xlsxwriter')
      for i in range(0, 32):
          ds = pd.DataFrame(arr[i,:,:])
          ds.to_excel(writer, sheet_name = 'bin%d' % i)
      writer.save()  
      print("Terminating\n")
      print("DATA Output of balance\n")
      for i in range(1,32):
          print("Team {i} \n".format(i=i))
          total = iss[i][16]
             
          for j in range(1,16):
            if (not wil[i][j]) :
              total += (0.75 * iss[i][j] * ggpp[j])
            else:
              total -= (1.5 * iss[i][j] * ggpp[j])
            
            print(" Gun Code {j} : {dd}\n".format(j=j,dd=iss[i][j]))
          print("Net WORTH balance {bb} and Net CASH balance {cc}\n".format(bb=total,cc=arr[i][33][0]))
          iss[i][17] = total
          pd.DataFrame(iss).to_csv("ud.csv")
      break
  elif n==5355 :
        print("Update any changes previous input\n")
        print("Update trade table\n")
        print("Input previous wrong values \n")
        print("Selling_team \n")
        p = inp()
        print("Purchasing_team \n")
        s = inp()
        print("Gun_code \n")
        gc = inp()
        print("Gun_Quantity \n")
        gq = inp()
        print("Gun_Price \n")
        gp = inp()
        func(s,p,gc,gq,gp)
        pd.DataFrame(iss).to_csv("ud.csv")
        print("Changes are reverted \n Enjoy Playing and be Careful\n\n")
  else:
    print("New update\n")
    print("Selling_team \n")
    s = inp()
    print("Purchasing_team \n")
    p = inp()
    print("Gun_code \n")
    gc = inp()
    print("Gun_Quantity \n")
    gq = inp()
    if (p==31):
        gp = pp[gc]
    elif(s==31):
        gp = ss[gc]
    else:
        print("Gun_Price \n")
        gp = inp()
    func(s,p,gc,gq,gp)
    pd.DataFrame(iss).to_csv("ud.csv")
    print("******UPDATED******")
