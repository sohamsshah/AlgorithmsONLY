// Insertion Sort


#include <bits/stdc++.h>
using namespace std;


void Array(int arr[], int n){
	int i;
	for(i=0; i < n; i++){
		cout << arr[i] << " ";
		
	}
}


void InsertionSort(int arr[], int n)  
{  
    int i, key, j;  
    for (i = 1; i < n; i++) 
    {  
        key = arr[i];  
        j = i - 1;  
  
        while (j >= 0 && arr[j] > key) 
        {  
            arr[j + 1] = arr[j];  
            j = j - 1;
			 
        }  
        arr[j + 1] = key; 
		Array(arr,n); 
		cout << "\n";
        
    }  
}  


int main(){
	int arr[1000];
	int i, ele;
	cout << "Enter number of elements: \n";
	cin >> ele;
	cout << "Enter Elements of the Array!\n";
	for(i=0; i<ele; i++){
		cin >> arr[i];
	}
	InsertionSort(arr, ele);
	cout << "Sorted Array is: \n";
	Array(arr, ele);
	return 0;	
	
}


