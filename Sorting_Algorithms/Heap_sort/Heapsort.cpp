#include <iostream>

using namespace std;


// MaxHeapify for making Heap in O(n)
void maxHeapify(int arr[], int n, int i){
	
	//init
	int largest = i; 
	int left = 2*i + 1;
	int right = 2*i + 2;
	
	// if left child > root
	if(left < n && arr[left] > arr[largest]){
		largest = left;
	}
	// if right child > root
	if(right < n && arr[right] > arr[largest]){
		largest = right;	
	}
	// if largest is not the root
	if(largest != i){
		swap(arr[i], arr[largest]);
		maxHeapify(arr, n, largest);
	}
		
	
}

// Sorting function
void heapSort(int arr[], int n){
	// Make the heap
	for(int i = n/2; i>=0; i--){
		maxHeapify(arr, n, i);
	}
	// Get elements from the Max heap i.e the largest element
	for(int i = n-1; i>0;i--){
		// Swap the current root to end
		swap(arr[0], arr[i]);
		// Reduce the heap size and call Max Heapify
		maxHeapify(arr,i,0);
	}
}

// Utility Function
void printArray(int arr[], int n) 
{ 
    for (int i=0; i<n; ++i) 
        cout << arr[i] << " "; 
    cout << "\n"; 
} 


// Main Function
int main() 
{ 
    int arr[1000];
	int i, ele;
	cout << "Enter number of elements: \n";
	cin >> ele;
	cout << "Enter Elements of the Array!\n";
	for(i=0; i<ele; i++){
		cin >> arr[i];
	} 
  
    heapSort(arr, ele); 
  
    cout << "Sorted array is \n"; 
    printArray(arr, ele); 
} 


