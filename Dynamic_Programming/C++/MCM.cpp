#include<iostream> 
using namespace std; 

int MatrixChainOrder(int p[], int n) 
{ 
    int T[n][n]; 
  
    for (int i=1; i<n; i++) 
        T[i][i] = 0; 
  
    for (int L=1; L<n-1; L++)  
    for (int i=1; i<n-L; i++)      
        T[i][i+L] = min(T[i+1][i+L] + p[i-1]*p[i]*p[i+L], 
                    T[i][i+L-1] + p[i-1]*p[i+L-1]*p[i+L]);      
      
    return T[1][n-1]; 
} 
   
int main() 
{ 
    int arr[1000];
	int i, size;
	cout << "Enter number of elements: \n";
	cin >> size;
	cout << "Enter Elements of the Array!\n";
	for(i=0; i<size; i++){
		cin >> arr[i];
	}
  
    printf("Minimum number of multiplications is %d ", 
                    MatrixChainOrder(arr, size)); 
  
    return 0; 
} 
