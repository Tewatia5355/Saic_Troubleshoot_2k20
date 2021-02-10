#include<iostream>
#include<fstream>
using namespace std;
int arr[33][33][32];
int iss[31][2][16];
void func(int selling_team,int purchasing_team,int gun_code,int gun_quantity,int gun_price)
{
  if((selling_team<31 && selling_team>0)&&(purchasing_team<31 && purchasing_team>0)&&(gun_code>0 && gun_code<16)&&(gun_quantity>0)&&(gun_price>0))
  {
	//arr[selling_team][purchasing_team][2*gun_code] = gun_quantity;
    //arr[selling_team][purchasing_team][2*gun_code+1] = gun_price;
    arr[selling_team][31][0] = (gun_quantity*gun_price);
    arr[selling_team][32][0] = arr[selling_team][32][0] + arr[selling_team][31][0];
    arr[31][purchasing_team][0] = (gun_quantity*gun_price);
    arr[32][purchasing_team][0] = arr[32][purchasing_team][0] - arr[31][purchasing_team][0];
    arr[32][selling_team][0] = arr[selling_team][32][0];
    arr[purchasing_team][32][0] = arr[32][purchasing_team][0];
    iss[selling_team][0][gun_code] = iss[selling_team][0][gun_code] - gun_quantity;
    iss[purchasing_team][0][gun_code] = iss[purchasing_team][0][gun_code] + gun_quantity;
  }
  else
  {
      cout<<"Error in the given data maybe exceed in matrix limit"<<endl;
  }
}
int main()
{
  /*for(int i = 0;i<31;i++)
  {
    arr[i][0][0] = i+1;
  //Initial cost to be given
    arr[32][i][0] = 100000;
    arr[i][32][0] = 100000;
  }
  for(int i = 0;i<31;i++)
  {
    arr[0][i][0] = i+1;
  }
  for(int i = 0;i<=31;i+=2)
  {
    arr[0][0][i] = i+1;
  }*/
  cout<<"Update gun matrix!!"<<endl;
  for(int i = 1;i<=5;i++)
  {
    int gcc,gqq,nog;
    cout<<"Update team "<<i<<" gun_quantity and new balance"<<endl;
    cout<<"Update team net balance :"<<endl;
    cin>>gcc;
    iss[i][1][0] = gcc;
    cout<<"Number of guns purchased"<<endl;
    cin>>nog;
    for(int j = 1;j<=nog;j++)
    {
        cout<<"Gun code for team "<<i<<" : ";
        cin>>gcc;
        cout<<"Gun Quantity for gun code "<<gcc<<" for team "<<i<<" : ";
        cin>>gqq;
        iss[i][0][gcc] = gqq;
    }
  }
  for(int i = 1;i<=31;i++)
  {
      arr[32][i][0] = iss[i][1][0];
      arr[i][32][0] = iss[i][1][0];
  }
  for (int i=1;i<=31;i++)
        {
            cout<<arr[i][32][0]<<"\t"<<arr[32][i][0]<<endl;
        }
  while(1)
  {
    int n,s,p,gc,gq,gp;
    cout<<"password"<<endl;
    cin>>n;
    if(n==53555355)
      {
        cout<<"Terminating"<<endl;
        cout<<"DATA Output of balance"<<endl;
        for (int i=1;i<=31;i++)
        {
            cout<<"Team "<<i<<" Net Selling balance "<<arr[i][32][0]<<" and Net Purchasing balance "<<arr[32][i][0]<<" And Guns\n";
            for(int j = 1;j<=15;j++)
            {
                cout<<" Gun Code "<<i<<" : "<<iss[i][0][j]<<endl;
            }
        }
        ofstream outdata;
        outdata.open('outfile.csv',ios::app);
        outdata<<arr[1][32][0]<<endl;
        system("pause");
        break;
      }
    else
    {
      cout<<"New update "<<endl;
      cout<<"Selling_team"<<endl;
      cin>>s;
      cout<<"purchasing_team"<<endl;
      cin>>p;
      cout<<"Gun_code"<<endl;
      cin>>gc;
      cout<<"Gun_quantity"<<endl;
      cin>>gq;
      cout<<"Gun_price"<<endl;
      cin>>gp;
      func(s,p,gc,gq,gp);
      cout<<"******UPDATED******\n\n";
    }
  }
  return 0;
}
