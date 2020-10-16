using namespace std;
#include <bits/stdc++.h> 
// Number of vertices in the graph globally defined
#define V 5 

// To find the vertex with the minimum key value  
int minKey(int key[], bool mstSet[]) 
{ 
    // Initialize min value with Int Max 
    int min = INT_MAX, min_index; 

    for (int v = 0; v < V; v++) 
        if (mstSet[v] == false && key[v] < min) 
            min = key[v], min_index = v; 
 
    return min_index; 
} 
 
// A utility function to print the 
// constructed MST stored in parent[] 
void printMST(int parent[], int graph[V][V]) 
{ 	
	cout<<"The minimum Spanning Tree is: \n";
    cout<<"Edge \tWeight\n"; 
    for (int i = 1; i < V; i++) 
        cout<<parent[i]<<" - "<<i<<" \t"<<graph[i][parent[i]]<<" \n"; 
} 
 
// To construct MST and graph using Adjacency Matrix Representation
void primMST(int graph[V][V]) 
{ 
    int parent[V]; // To store MST
     
    int key[V]; // key array to pick minimum weight edge
     
    bool mstSet[V]; // To represent set of vertices included in MST 
 
    // Initializing all keys as INFINITE 
    for (int i = 0; i < V; i++) 
        key[i] = INT_MAX, mstSet[i] = false; 

    key[0] = 0; 
    parent[0] = -1; // First node is always root of MST 
 
    for (int count = 0; count < V - 1; count++)
    { 
        int u = minKey(key, mstSet); // choose minimum key vertex from set of vertex not included in MST
 
        
        mstSet[u] = true; // adding the chosen vertex to MST set
 
        // Update key value and parent index of the adjacent vertices of the picked vertex. 
        
        for (int v = 0; v < V; v++) 
        	// Consider only those vertices which are not yet included in MST 
            if (graph[u][v] && mstSet[v] == false && graph[u][v] < key[v]) 
                parent[v] = u, key[v] = graph[u][v]; 
    } 
    // printing the constructed MST 
    printMST(parent, graph); 
} 
 
// Driver code
int main() 
{ 
    int graph[V][V] = { { 0, 2, 0, 6, 0 }, 
                        { 2, 0, 3, 8, 5 }, 
                        { 0, 3, 0, 0, 7 }, 
                        { 6, 8, 0, 0, 9 }, 
                        { 0, 5, 7, 9, 0 } }; 
 
    // Print the solution 
    primMST(graph); 
 
    return 0; 
} 
