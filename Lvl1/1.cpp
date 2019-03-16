#include<iostream>
#include<limits>
using namespace std;
double division(int a, int b) {
   if( b == 0 ) {
      throw "Division by zero condition!";
   }
   return (a/b);
}

int main(){
float num1,num2,z;
int n;
cout << "Welcome to The Simple Calculator \n";
cout << "PLease enter the two numbers to perform operations \n";
cin >> num1;
cin >> num2;
if(!std::isdigit(num1) || !isdigit(num2)){
cout << "Enter valid floats";
exit(0);
}
cout << "Enter the number of the operation  to be performed \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n";
cin >> n;
switch (n)
{
    case 1: cout << "sum=" <<num1+num2;
        break;
    case 2:cout << "difference=" <<num1-num2;
        break;
    case 3:cout << "product=" <<num1*num2;
	break;
    case 4:
      try {
      z = division(num1, num2);
      cout << z << endl;
   } catch (const char* msg) {
     cerr << msg << endl;
   }
	break;
	default:
	cout << "Please choose another value";
	break;
}
}
