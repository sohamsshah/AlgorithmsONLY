// Quick Sort

#include <iostream>
using namespace std;

void swap(int *a, int *b) {
  int t = *a;
  *a = *b;
  *b = t;
}

void Array(int arr[], int n){
	int i;
	for(i=0; i < n; i++){
		cout << arr[i] << " ";
		
	}
}

int partition(int arr[], int l, int h) {
  
  int pivot_element = arr[h];
  int i = l - 1;

  for (int j = l; j < h; j++) {
    if (arr[j] <= pivot_element) {
      i++;
      swap(&arr[i], &arr[j]);
    }
  }
  swap(&arr[i + 1], &arr[h]);
  return (i + 1);
}

void quickSort(int arr[], int l, int h) {
  if (l < h) {

    int pivot = partition(arr, l, h);

    
    quickSort(arr, l, pivot - 1);

    quickSort(arr, pivot + 1, h);
  }
}

int main() {
  int n;
   cout << "Enter size of array: ";
   cin >> n;
   int arr[n];     
   cout << "Enter elements:" << endl;
   for(int i = 0; i<n; i++) {
      cin >> arr[i];
   }
   cout << "Array before Sorting: ";
   Array(arr, n);
   quickSort(arr, 0, n - 1);
  cout << "Array after Sorting: \n";
   Array(arr, n);
}
