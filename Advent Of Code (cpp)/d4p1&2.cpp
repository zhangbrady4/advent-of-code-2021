#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

vector < vector <int> > v;

vector <int> grid(string line){
    vector <int> b;
    int temp=0;
    for (int i=0; i<line.size(); i++){
        if (isdigit(line[i])){
            if (isdigit(line[i+1])){
                b.push_back(stoi(line.substr(i,2)));
                //cout<<(stoi(line.substr(i,2)));
                i++;
            }else{
                b.push_back(stoi(line.substr(i,1)));;
                //cout<<(stoi(line.substr(i,1)));
            }
        }
    }
    return b;
}

vector <int> callednums (string s){
    vector <int> a;
    int temp=0;
    for (int i=0; i<s.size(); i++){
        if (s[i]==','){
            a.push_back(stoi(s.substr(temp,i-temp)));
            temp=i+1;
        }
        else if(temp==s.size()-1){
            a.push_back(stoi(s.substr(temp,1)));
        }
    }
    return a;
}

int tot(vector <int> h){
    int y=0;
    for (auto x: h){
        y+=x;
    }
    return y;
}

int win(vector <int> h){
    int sum;
    for (int i=0; i<5; i++){
        for (int j=0; j<5; j++){
            if (h[i*5+j]!=0){
                break;
            }
            else{
                if (j==4){
                    sum=tot(h);
                    return sum;
                }
            }
        }
    }

    for (int i=0; i<5; i++){
        for (int j=0; j<5; j++){
            if (h[j*5+i]!=0){
                break;
            }
            else{
                if (j==4){
                    sum=tot(h);
                    return sum;
                }
            }
        }
    }

    return 0;
}

void change(int n){
    for (int i=0; i<v.size(); i++){
        for (int j=0; j<v[i].size(); j++){
            if (v[i][j]==n){
                v[i][j]=0;
                if(win(v[i])!=0){
                    int a=win(v[i]);
                    cout<<n*a<<endl;
                    v[i].clear();
                }
            break;
            }
            
        }
    }
}

int main() {
    vector <string>Data;
    vector <int>num;
    int flag=0;
    int temp=0;
    vector <int> d;
    string line;
    ifstream f("AOC1.txt");

    while ( getline(f, line) ) //space delimited
    {
        if (flag<1){
            flag++;
            num=callednums(line);
        }
        else if(flag==1){
            flag++;
        }
        else if(line!=""){
            vector <int> e;
            e=grid(line);
            d.insert(d.end(),e.begin(),e.end());
        }
        else{
            v.push_back(d);
            d.clear();
        }
    }
    v.push_back(d);

    f.clear();
    f.seekg(0,f.beg);

    f.close();

    for (int i=0; i<num.size(); i++){
        change(num[i]);
    }

    return 0;
}