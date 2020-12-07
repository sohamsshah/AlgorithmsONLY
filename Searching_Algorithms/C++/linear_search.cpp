#include <bits/stdc++.h>
using namespace std;


int linear_search(int arr[], int n, int key){
	for(int i=0; i<n; i++){
		if(arr[i] == key){
			return i;
		}
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
	ans = linear_search(arr, ele, key);
	if(ans != -1){
		cout << "The element is at index: ";
		cout << ans;
	}
	else{
		cout << "\nElement not present!\n";
	}
	
	return 0;		
}
