#include<stdio.h>
float probability(float x, float arr [], float n)
{
  float c=0;
  for (int i = 0; i < n; i++) {
    if(arr[i]==x)
    {
      c++;
    }
  }
  return (c/n);
}
int main()
{
  float t,a,n,b,arr[10000],pa,pb;
  scanf("%f", &t);
  for (int i = 0; i < t; i++) {
    scanf("%f",&n);
    scanf("%f",&a);
    scanf("%f",&b);
    for (int j = 0; j < n; j++) {
      scanf("%f", &arr[j]);
    }
    pa=probability(a,arr,n);
    pb=probability(b,arr,n);
    printf("%f\n", pa*pb);
  }
}
