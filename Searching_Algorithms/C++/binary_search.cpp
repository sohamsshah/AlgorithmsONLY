#include <bits/stdc++.h>
using namespace std;

int binarySearch(int arr[], int l, int r, int key){

	if(r>=l){
		int mid = l + (r-1)/2;
		if(arr[mid] == key){
			return mid;
		}
		if(arr[mid]> key){
			return binarySearch(arr, l, mid-1,key);
		}
		return binarySearch(arr, mid+1, r,key);
	}
	return -1;
}


int main(){
	int arr[1000];
	int i, ele, key, ans;
	cout << "Enter number of elements: \n";
	cin >> ele;
	cout << "Enter Elements of the Array!\n";
	for(i=0; i<ele; i++){
		cin >> arr[i];
	}
	cout << "Enter element to be searched: \n";
	cin >> key;
	ans = binarySearch(arr, arr[0], arr[ele-1], key);
	if(ans != -1){
		cout << "The element is at index: ";
		cout << ans;
	}
	else{
		cout << "\nElement not present!\n";
	}
	
	return 0;		
}


