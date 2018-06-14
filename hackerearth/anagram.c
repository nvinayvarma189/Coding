#include <stdio.h>
#include <string.h>

int main()
{
    int t,m;
    scanf("%d",&t);
    for(m=0;m<t;m++)
    {
      char a[10000],b[10000];
      scanf("%s",a);
      scanf("%s",b);
      int l1,l2,i,j;
      l1 = strlen(a); l2 = strlen(b);
      for(i=0;i<l1;i++)
      {
        for(j=0;j<l2;j++)
        {
          if(a[i]==b[j])
          {
            for(int k=i;k<l1;k++)
            {
              a[k] = a[k+1];
            }
            l1--;
            for(int k=j;k<l2;k++)
            {
              b[k] = b[k+1];
            }
            l2--;
            i--;
          }
        }
      }
      printf("%d\n",l1+l2);
    }
    return 0;
}
