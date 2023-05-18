#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

int main() {
    vector <string>Data;
    vector <string>temp;
    string line;
    ifstream f("AOC1.txt");

    while ( getline(f, line) ) //space delimited
    {
        temp.push_back(line);
        Data.push_back(line);
    }

    f.clear();
    f.seekg(0,f.beg);

    f.close();

    int hori;

    vector <vector <int> > v;

    for (int i=0; i<Data.size(); i++){
        vector <int> a;
        for (int j=0; j<Data[i].size(); j++){
            a.push_back(stoi(Data[i].substr(j,1)));
        }
        v.push_back(a);
    }

    for (int k=0; k<v[0].size(); k++){
        if (v.size()!=1){
            int count=0;
            for (int i=0; i<v.size(); i++){
                if (v[i][k]>0){
                    count++;
                }
                else{
                    count--;
                }
            }

            if (count>=0){
                count=1;
            }
            else{
                count=0;
            }

            cout<<count<<endl<<endl<<endl;

            for (int i=v.size()-1; i>=0; i--){
                cout<<i<<endl;
                cout<<k<<endl;
                
                if ((v[i][k])!=count){
                    v.erase(v.begin()+i);
                    
                }
                cout<<v.size()<<endl;
            }
        }
    }

    for (int i=0; i<v[0].size(); i++){
        cout<<v[0][i];
    }

    for (int i=0; i<v[0].size(); i++){
        if (v[0][i]==1){
            hori+= pow(2,v[0].size()-1-i);
        }
    }

    cout<<endl<<hori;

    return 0;
} 