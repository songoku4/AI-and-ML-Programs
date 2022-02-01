#include<bits/stdc++.h> 
using namespace std; 

int cost = INT_MAX; 
int Matrix[5][5] = { 
        {0, 15, 10, 5, 15}, 
        {15, 0, 30, 20, 15}, 
        {15, 30, 0, 30, 15}, 
        {5, 20, 10, 0, 50}, 
        {5, 20, 10, 10, 0} 
}; 

void swap(int *x, int *y) { 
    int flag; 
    flag = *x; 
    *x = *y; 
    *y = flag; 
} 

void arrayFn(int *arr, int flag){ 
    int sum = 0; 
    for(int i = 0; i <= flag; i++) { 
        sum += Matrix[arr[i % 4]][arr[(i + 1) % 4]]; 
    } 
    if (cost > sum) { 
        cost = sum; 
    } 
} 

void TP(int *arr, int src, int end) { 
    if (src == end) { 
        arrayFn(arr, end); 
    } 
    else { 
        for (int j = src; j <= end; j++) { 
            swap((arr + src), (arr + j)); 
            TP(arr, src + 1, end); 
            swap((arr + src), (arr + j)); 
        } 
    } 
} 

int main() { 
   int arr[] = {0, 1, 2, 3, 4}; 
   TP(arr, 0, 4); 
   cout<<"Minimum Cost: "<< cost; 
   return 0; 
} 
