#include<iostream>
using namespace std;
int arr[33][33][32];
int iss[31][16];
void func(int selling_team,int purchasing_team,int gun_code,int gun_quantity,int gun_price)
{
  arr[selling_team][purchasing_team][2*gun_code] = gun_quantity;
  arr[selling_team][purchasing_team][2*gun_code+1] = gun_price;
  arr[selling_team][31][0] = (gun_quantity*gun_price);
  arr[selling_team][32][0] = arr[selling_team][32][0] + arr[selling_team][31][0];
  arr[31][purchasing_team][0] = (gun_quantity*gun_price);
  arr[32][purchasing_team][0] = arr[32][purchasing_team][0] - arr[31][purchasing_team][0];
  arr[32][selling_team][0] = arr[selling_team][32][0];
  arr[purchasing_team][32][0] = arr[32][purchasing_team][0];
  iss[selling_team][gun_code] = iss[selling_team][gun_code] - gun_quantity;
  iss[purchasing_team][gun_code] = iss[purchasing_team][gun_code] + gun_quantity;
}
int main()
{
  for(int i = 0;i<31;i++)
  {
    arr[i][0][0] = i+1;
  //Initial cost to be given
    arr[32][i][0] = 0;
    arr[i][32][0] = 0;
  }
  for(int i = 0;i<31;i++)
  {
    arr[0][i][0] = i+1;
  }
  for(int i = 0;i<=31;i+=2)
  {
    arr[0][0][i] = i+1;
  }
  cout<<"Update gun matrix!!"<<endl;
  for(int i = 1;i<31;i++)
  {
    int gcc;
    cout<<"Update team "<<i<<" gun_quantity"<<endl;
    for(int j = 1;j<16;j++)
    {
      cout<<"Gun Quantity for gun code "<<j<<" is : ";
      cin>>gcc;
    }
  }
  while(1)
  {
    int n,s,p,gc,gq,gp;
    cout<<"password"<<endl;
    cin>>n;
    if(n==53555355)
      {
        cout<<"Terminating"<<endl;
        for(int i = 0;i<3)
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
