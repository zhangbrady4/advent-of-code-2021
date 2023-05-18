#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

/*import re
import math

f = open('input.txt', 'r')
g = re.split(",",f.read())

#print (g)

for x in range(len(g)):
    g[x]=int(g[x])

for x in range(1,256):
    for y in range(len(g)):
        if (g[y]==0):
            g[y]=6
            g.append(8)
        else:
            g[y]=(g[y]-1)

print (len(g))

f.close()*/


int main() {
    vector <string>Data;
    char c;
    vector <int> a;
    string line;
    ifstream f("input2.txt");

    while ( f.get(c) ) //space delimited
    {
        if (c!=','){
            a.push_back(c);
        }
    }

    f.clear();
    f.seekg(0,f.beg);

    f.close();

    for (int i=0; i<80; i++){
        for (int j=0; j<a.size(); j++){
            cout<<a[j]<<endl;
            if (a[j]==0){
                a[j]=6;
                a.push_back(8);
            }
            else{
                a[j]--;
            }
        }
    }

    cout<<a.size();

    return 0;
} 