// Bubble Sort
#include <bits/stdc++.h>
using namespace std;

void Array(int arr[], int n){
	int i;
	for(i=0; i < n; i++){
		cout << arr[i] << " ";
		
	}
}

void swap(int *a, int *b){
	int temp = *a;
	*a = *b;
	*b = temp;
}

void BubbleSort(int arr[],int n){
	int i,j, swapped;
	for(i=0;i<n-1;i++){
	
		for(j=0; j<n-i-1; j++){
			if(arr[j] > arr[j+1]){
				swap(&arr[j], &arr[j+1]);
				swapped=1;
			}
			
		}
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
	BubbleSort(arr, ele);
	cout << "Sorted Array is: \n";
	Array(arr, ele);
	return 0;		
}


