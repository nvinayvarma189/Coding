/*
The greatest common divisor (GCD) of a sequence is the greatest positive integer
which divides each element of this sequence.

You are given a sequence AA of positive integers with size NN.
You are allowed to delete up to N−1N−1 elements from this sequence.
 (I.e., you may delete any number of elements, including zero, as long as the
 resulting sequence is non-empty.)

Please find the minimum number of elements which have to be deleted so that the
GCD of the resulting sequence would be equal to 11, or determine that it is impossible.

Input
The first line of the input contains a single integer TT
denoting the number of test cases. The description of TT test cases follows.
The first line of each test case contains a single integer NN.
The second line contains NN space-separated integers A1,A2,…,ANA1,A2,…,AN.
Output
For each test case, print a single line containing one integer —
the minimum number of elements to delete, or −1−1 if it is impossible to make the GCD equal to 11.
*/

#include <stdio.h>
int gcd(int a, int b)
{
	int i,g;
  for(i=1; i<=a && i<= b; i++)
  {
    if(a%i==0 && b%i==0)
    {
      g=i;
    }
  }
  return g;
}
int main()
{
	int n,result,a[1000],t;
  scanf("%d", &t);
	for (int i = 0; i < t; i++) {
    scanf("%d",&n);
    for (int i = 0; i < n; i++) {
      scanf("%d",&a[i]);
    }
    result =a[0];
    for (int i = 1; i < n; i++) {
      result = gcd(result, a[i]);
    }
    if(result == 1)
    {
      printf("%d\n",0);
    }
    else
    {
      printf("%d\n",-1);
    }
  }
	return 0;
}
