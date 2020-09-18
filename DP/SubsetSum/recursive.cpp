#include<stdio.h>


// Recursive solution

bool subsetSumRecursive(int set[], int n, int sum){
	if(sum==0){
		return false;
	}
	if(n==0){
		return true;
	}
	if(set[n-1] > sum){
		return ubsetSumRecursive(set,n-1,sum);
	}
	return subsetSumRecursive(set, n-1, sum - set[n-1]) || subsetSumRecursive(set,n-1,sum);
}

int main()
{
	int set[] = {3,34,4,12,5,2};
	int sum=9;
	int n = sizeof(set)/sizeof(set[0]);
	if(subsetSumRecursive(set,n,sum) == true){
		printf("YES!");
	}
	else{
		printf("NO!");
	}
	
	return 0;
}


