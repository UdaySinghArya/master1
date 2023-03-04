// Project of  Hotel Management.

#include<iostream>
using namespace std;
int main()
{
    int quant,choice,m;
    int Qrooms=0,Qpasta=0,Qburger=0,Qnoodles=0,Qshake=0,Qchicken=0;//Quantity
    int Srooms=0,Spasta=0,Sburger=0,Snoodles=0,Sshake=0,Schicken=0;//Sold
    int Total_rooms=0,Total_pasta=0,Total_burger=0,Total_noodles=0,Total_shake=0,Total_chicken=0;

    cout<<"Quantity of Item we have::";
    cout<<"\n Rooms are available: ";
    cin>>Qrooms;
    cout<<"\n Pastas are available: ";
    cin>>Qpasta;
    cout<<"\n Burgers are available: ";
    cin>>Qburger;
    cout<<"\n Noodles are available: ";
    cin>>Qnoodles;
    cout<<"\n Shakes are available: ";
    cin>>Qshake;
    cout<<"\n Chikens are available: ";
    cin>>Qchicken;

    m:
    cout<<"\n\t\t\t Plese select from the menu option  ";
    cout<<"\n\n1) Rooms";
    cout<<"\n\n2) Pasta";
    cout<<"\n\n3) Burger";
    cout<<"\n\n4) Noodles";
    cout<<"\n\n5) Shake";
    cout<<"\n\n6) Chicken";
    cout<<"\n\n7) Information regarding sales and collection";
    cout<<"\n\n8) Exit";
    n:
    cout<<"\n\n Please Enter Your Choice:: ";
    cin>>choice;
    switch(choice)
    {
        case 1:
        cout<<"Enter the number of rooms you want::";
        cin>>quant;
        if(Qrooms-Srooms>=quant)
        {
            Srooms=Srooms+quant;
            Total_rooms=Total_rooms+quant*1200;
            cout<<"\n\n"<<quant<<" "<<"Rooms have been alloted to you!"<<"\n";
        }
        else
        {
            cout<<"\n\tonly"<<Qrooms-Srooms<<"Rooms remaining in hotel";
            break;
        }
        goto n;
        case 2:
        cout<<"Enter the number of pasta you want::";
        cin>>quant;
        if(Qpasta-Spasta>=quant)
        {
            Spasta=Spasta+quant;
            Total_pasta=Total_pasta+quant*150;
            cout<<"\n\n"<<quant<<" "<<"pasta have been alloted to you!"<<"\n";
        }
        else
        {
            cout<<"\n\tonly"<<Qpasta-Spasta<<"pasta remaining in hotel";
            break;
        }
        goto n;
        
        
        case 3:
        cout<<"Enter the number of burger you want::";
        cin>>quant;
        if(Qburger-Sburger>=quant)
        {
            Sburger=Sburger+quant;
            Total_burger=Total_burger+quant*200;
            cout<<"\n\n"<<quant<<" "<<"burger have been alloted to you!"<<"\n";
        }
        else
        {
            cout<<"\n\tonly"<<Qburger-Sburger<<"burger remaining in hotel";
            break;
        }
        goto n;

        case 4:
        cout<<"Enter the number of noodles you want::";
        cin>>quant;
        if(Qnoodles-Snoodles>=quant)
        {
            Snoodles=Snoodles+quant;
            Total_noodles=Total_noodles+quant*100;
            cout<<"\n\n"<<quant<<" "<<"noodles have been alloted to you!"<<"\n";
        }
        else
        {
            cout<<"\n\tonly"<<Qnoodles-Snoodles<<"noodles remaining in hotel";
            break;
        }
        goto n;


        case 5:
        cout<<"Enter the number of shake you want::";
        cin>>quant;
        if(Qshake-Sshake>=quant)
        {
            Sshake=Sshake+quant;
            Total_shake=Total_shake+quant*50;
            cout<<"\n\n"<<quant<<" "<<"shake have been alloted to you!"<<"\n";
        }
        else
        {
            cout<<"\n\tonly"<<Qshake-Sshake<<"shake remaining in hotel";
            break;
        }
        goto n;

        case 6:
        cout<<"Enter the number of chicken you want::";
        cin>>quant;
        if(Qchicken-Schicken>=quant)
        {
            Snoodles=Snoodles+quant;
            Total_chicken=Total_chicken+quant*250;
            cout<<"\n\n"<<quant<<" "<<"chicken have been alloted to you!"<<"\n";
        }
        else
        {
            cout<<"\n\tonly"<<Qchicken-Schicken<<"chicken remaining in hotel";
            break;
        
        }
        goto n;


        case 7:
        cout<<"\n\t\t\t\t\t\t DETAILS OF SALES AND CONDITION";
        cout<<"\n\n Number of rooms we had : "<<Qrooms;
        cout<<"\n\n remaining rooms : "<<Qrooms-Srooms;
        cout<<"\n\n Total rooms collection for the day: "<<Total_rooms;
        
        
        cout<<"\n\nNumber of pasta we had: "<<Qpasta;
        cout<<"\n\n Number of pasta we sold : "<<Spasta;
        cout<<"\n\n remaining pasta : "<<Qpasta-Spasta;
        cout<<"\n\n Total pasta collection for the day: "<<Total_pasta;

        
        cout<<"\n\nNumber of burger we had: "<<Qburger;
        cout<<"\n\n Number of burger we sold : "<<Sburger;
        cout<<"\n\n remaining burger : "<<Qburger-Sburger;
        cout<<"\n\n Total burger collection for the day: "<<Total_burger;

        

        cout<<"\n\nNumber of Noodles we had: "<<Qnoodles;
        cout<<"\n\n Number of noodles we sold : "<<Qnoodles;
        cout<<"\n\n remaining noodles : "<<Qnoodles-Snoodles;
        cout<<"\n\n Total noodles collection for the day: "<<Total_noodles;

        cout<<"\n\n Number of shake we had: "<<Qshake;
        cout<<"\n\n Number of shake we sold : "<<Qshake;
        cout<<"\n\n remaining shake : "<<Qshake-Sshake;
        cout<<"\n\n Total shake collection for the day: "<<Total_shake;

        cout<<"\n\n Number of chicken we had: "<<Qchicken;
        cout<<"\n\n Number of shake we sold : "<<Qchicken;
        cout<<"\n\n remaining chicken : "<<Qchicken-Schicken;
        cout<<"\n\n Total chicken collection for the day: "<<Total_chicken;
        
        cout<<"\n\n\n TOTAL COLLECTION FOR THE DAY: "<<Total_rooms+Total_pasta+Total_burger+Total_noodles+Total_shake+Total_chicken;
        goto n;

        case 8:
            exit(0);
            
            default:
                cout<<"\n Please select the number mentioned above! ";
    }
    goto m;
    return 0;
}