// https://www.codechef.com/LTIME61B/problems/NUM239
#include<stdio.h>
int main()
{
    int t,l,r,c;
    scanf("%d", &t);
    for (int i=0; i<t; i++)
    {
        c=0;
        scanf("%d", &l);
        scanf("%d", &r);
        for (int j=l ; j<=r; j++)
        {
            if(j % 10 == 2 || j % 10 == 3 || j % 10 == 9 )
            {
                c++;
            }
        }
printf("%d\n", c);
    }
}
