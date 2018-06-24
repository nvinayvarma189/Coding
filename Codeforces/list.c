#include<stdio.h>
int main(){
    int t, k, a[10000],c=0;
    scanf("%d", &t);
    scanf("%d", &k);
    for (int i = 0; i < t; i++) {
        scanf("%d", &a[i]);
    }
    int s,l;
    s=0;
    l=t-1;
    while(1 && s!=l+1 )
    {
        if(k >= a[s]  && k >= a[l])
        {
            c++;
            s++;

        }
        else if(k >= a[s])
        {
            c++;
            s++;
        }
        else if(k >= a[l])
        {
            c++;
            l--;
        }
        else
            break;
    }
    printf("%d\n", c);
}
