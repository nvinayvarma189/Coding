/*Question:
Given an array 'a' having 'n' elements.

Now, given 'q' queries , each query has an integer 'x' , you have to find out the index of last occurrence of the 'x' if it is present in the array else print '-1'.

Input :

test cases,t
no. of elements in array , a
a[i]
no. of queries, q
element x
Output:

Desired O/p
*/
#include <stdio.h>

int main()
{
    int t,q,p,f,b=-1;
    long int x,n,a[100000];
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        scanf("%ld",&n);
        for(int j=0;j<n;j++)
        {
            scanf("%ld",&a[j]);
        }
        scanf("%d",&q);
        for(int k=0;k<q;k++)
        {
            f=0;
            scanf("%ld",&x);
            for(int l=n-1;l >= 0;l--)
            {
                if(a[l]==x)
                {
                    printf("%d yolo",l+1);
                    f=1;
                    break;
                }
            }
            if(f==0)
            {
               printf("%d",b);
            }
        }
    }
}
