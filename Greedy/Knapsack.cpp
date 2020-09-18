#include <bits/stdc++.h> 
  
using namespace std; 
  
struct Item 
{ 
    int val, wt; 
  
    // Constructor 
    Item(int val, int wt) : val(val), wt(wt) 
    {} 
};

 
bool cmp(struct Item a, struct Item b) 
{ 
    double r1 = (double)a.val / a.wt; 
    double r2 = (double)b.val / b.wt; 
    return r1 > r2; 
} 


double fractionalKnapsack(int W, struct Item arr[], int n) 
{ 
    //    sorting Item on basis of ratio 
    sort(arr, arr + n, cmp); 
  
  
    int curWeight = 0;  
    double finalvalue = 0.0; 
   
    for (int i = 0; i < n; i++) 
    { 
        if (curWeight + arr[i].wt <= W) 
        { 
            curWeight += arr[i].wt; 
            finalvalue += arr[i].val; 
        } 
  
        else
        { 
            int remain = W - curWeight; 
            finalvalue += arr[i].val * ((double) remain / arr[i].wt); 
            break; 
        } 
    } 
   
    return finalvalue; 
} 
  
int main() 
{ 
    int W = 50; 
    Item arr[] = {{60, 10}, {100, 20}, {120, 30}}; 
  
    int n = sizeof(arr) / sizeof(arr[0]); 
    cout << "Maximum val we can obtain = "
         << fractionalKnapsack(W, arr, n); 
    return 0; 
} 
