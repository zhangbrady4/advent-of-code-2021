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

    return 0;
} 