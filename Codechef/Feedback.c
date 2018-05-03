/*
Lots of geeky customers visit our chef's restaurant everyday. So, when asked to fill the feedback form, these customers represent the feedback using a binary string (i.e a string that contains only characters '0' and '1'.

Now since chef is not that great in deciphering binary strings, he has decided the following criteria to classify the feedback as Good or Bad :

If the string contains the substring "010" or "101", then the feedback is Good, else it is Bad. Note that, to be Good it is not necessary to have both of them as substring.

So given some binary strings, you need to output whether according to the chef, the strings are Good or Bad.


*/
#include<stdio.h>
int main()
{
  int t,i,j,f=0;
  char a[100000];
  printf("Enter number of test cases\n");
  scanf("%d",&t);
  for(j=0;j<t;j++)
  {
    f=0;
    scanf("%s",a);
    for(i=0;a[i+2]!='\0';i++)
    {
      if ((a[i] == '0' && a[i+1] == '1' && a[i+2] == '0') || (a[i] == '1' && a[i+1] == '0' && a[i+2] == '1') )
      {
        f=1;
        break;
      }
    }
    if(f==0)
      printf("BAD\n");
    else
      printf("GOOD\n");
  }
}
