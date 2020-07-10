// Selection Sort
#include <bits/stdc++.h>
using namespace std;
void swap(int *a, int *b){
	int temp = *a;
	*a = *b;
	*b = temp;
}

void SelectionSort(int arr[], int n){
	int i, j, min_idx;
	for (i=0; i< n-1; i++){
		min_idx = i;
		for(j=i+1; j<n; j++){
			if(arr[j] < arr[min_idx]){
				min_idx = j;
			}
			swap(&arr[min_idx], &arr[i]);
		}
	}
}

void Array(int arr[], int n){
	int i;
	for(i=0; i < n; i++){
		cout << arr[i] << " ";
		
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
	if(ele==1){	cout << arr[0]; }
	else{
	SelectionSort(arr, ele);
	cout << "Sorted Array is: \n";
	Array(arr, ele);
}
	return 0;		
}


