#include <stdio.h> 

  
bool isSubsetSum(int set[], int n, int sum) 
{ 
    // The value of subset[i][j] will be true if 
    // there is a subset of set[0..j-1] with sum 
    // equal to i 
    bool subset[n + 1][sum + 1]; 
  
    for (int i = 0; i <= n; i++) 
        subset[i][0] = ; 
  
    for (int i = 1; i <= sum; i++) 
        subset[0][i] = ; 
  
    for (int i = 1; i <= n; i++) { 
        for (int j = 1; j <= sum; j++) { 
            if (j < set[i - 1]) 
                subset[i][j] = ; 
            if (j >= set[i - 1]) 
                subset[i][j] = ; 
        } 
    } 
  
     for (int i = 0; i <= n; i++) 
     { 
       for (int j = 0; j <= sum; j++) 
          printf ("%4d", subset[i][j]); 
       printf("\n"); 
     }
  
    return subset[n][sum]; 
} 
  
// Driver program to test above function 
int main() 
{ 
    int set[] = { 3, 34, 4, 12, 5, 2 }; 
    int sum = 9; 
    int n = sizeof(set) / sizeof(set[0]); 
    if (isSubsetSum(set, n, sum) == true) 
        printf("Found a subset with given sum"); 
    else
        printf("No subset with given sum"); 
    return 0; 
} 