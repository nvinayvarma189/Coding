/*Question:
Arijit is a brilliant boy. He likes memory games. He likes to participate alone but this time he has to have a partner. So he chooses you.

In this Game , your team will be shown N numbers for few minutes . You will have to memorize these numbers.

Now, the questioner will ask you Q queries, in each query He will give you a number , and you have to tell him the total number of occurrences of that number in the array of numbers shown to your team . If the number is not present , then you will have to say “NOT PRESENT” (without quotes).

INPUT And OUTPUT

The first line of input will contain N, an integer, which is the total number of numbers shown to your team.

The second line of input contains N space separated integers .

The third line of input contains an integer Q , denoting the total number of integers.

The Next Q lines will contain an integer denoting an integer, Bi , for which you have to print the number of occurrences of that number (Bi) in those N numbers on a new line.

If the number Bi isn’t present then Print “NOT PRESENT” (without quotes) on a new line.*/
#include <stdio.h>
int main()
{
  int n,a[100],q,x,c,f;
  scanf("%d",&n);
  for (int i=0;i<n;i++)
  {
    scanf("%d",&a[i]);
  }
    scanf("%d",&q);
    for(int i=0;i<q;i++)
    {
      c=0;
      f=0;
      scanf("%d",&x);
      for(int i=0;i<n;i++)
      {

        if(a[i]==x)
        {
          c++;
          f=1;
        }
      }
      if(f==1)
      {
        printf("%d me\n",c);
      }
        else
        {
          printf("NOT PRESENT\n");
        }
    }
}
