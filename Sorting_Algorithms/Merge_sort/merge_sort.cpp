// Merge Sort


#include <bits/stdc++.h>
using namespace std;

void Array(int arr[], int n){
	int i;
	for(i=0; i < n; i++){
		cout << arr[i] << " ";
		
	}
}

void merge(int *array, int l, int m, int r) {
   int i, j, k, n_l, n_r;
   
   n_l = m-l+1; 
   n_r = r-m;
   int larr[n_l]; 
   int rarr[n_r];
  
   for(i = 0; i<n_l; i++)
      larr[i] = array[l+i];
   for(j = 0; j<n_r; j++)
      rarr[j] = array[m+1+j];
   i = 0; j = 0; k = l;
   
   while(i < n_l && j<n_r) {
      if(larr[i] <= rarr[j]) {
         array[k] = larr[i];
         i++;
      }else{
         array[k] = rarr[j];
         j++;
      }
      k++;
   }
   while(i<n_l) {       
      array[k] = larr[i];
      i++; k++;
   }
   while(j<n_r) {     
      array[k] = rarr[j];
      j++; k++;
   }
}


void mergeSort(int *array, int l, int r) {
   int m;
   if(l < r) {
      int m = l+(r-l)/2;
      mergeSort(array, l, m);
      mergeSort(array, m+1, r);
      merge(array, l, m, r);
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
   mergeSort(arr, 0, n-1);    
   cout << "Array after Sorting: \n";
   Array(arr, n);
}
