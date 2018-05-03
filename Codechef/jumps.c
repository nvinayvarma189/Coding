/*
This morning Chef wants to jump a little. In a few minutes he will arrive at the point 0. Then he will perform a lot of jumps in such a sequence: 1-jump, 2-jump, 3-jump, 1-jump, 2-jump, 3-jump, 1-jump, and so on.

1-jump means that if Chef is at the point x, he will jump to the point x+1.

2-jump means that if Chef is at the point x, he will jump to the point x+2.

3-jump means that if Chef is at the point x, he will jump to the point x+3.

Before the start Chef asks you: will he arrive at the point a after some number of jumps?
*/
#include<stdio.h>
int main()
{
  int n;
  printf("enter position\n");
  scanf("%d",&n);
  if(n%6==0 ||(n+5)%6 == 0 ||(n+3)%6 == 0 )
  {
    printf("YES\n");
  }
  else
    printf("NO\n");
}
