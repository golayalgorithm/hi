#include <iostream>
#include <fstream> // for ifstream
#include <string>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
    
    ifstream inFile;
    vector<int> numbers;
    inFile.open("input_data.txt");
    
    if (inFile.is_open()) {
        // ok, it's open, time to read the data
        string line;
        int number;
        while (getline(inFile,line)) {
            string::size_type sz;
            number = stoi(line,&sz);
            numbers.push_back(number);
        }
        inFile.close();
    }
    
    // printing out the array of numbers
    for (unsigned int i=0; i<numbers.size(); i++) {
        cout << numbers[i] << " ";
    }
    
    // writing to file
    ofstream outFile;
    outFile.open("output_data.txt");
    for (unsigned int i=0; i<numbers.size(); i++) {
        outFile << i << ": " << numbers[i] << endl;
    }
    outFile.close();
    cout << endl;
    return 0;
}
