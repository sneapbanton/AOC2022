
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char* argv[]) {
    string line;
    ifstream myfile;
    vector<vector<int>> values;
    myfile.open("data.txt", ios::in);
    if (myfile.is_open()){
        vector<int> current_elf = {};
        while(getline(myfile,line)){
            if(line != ""){
                current_elf.push_back(stoi(line));
            }
            else{
                values.push_back(current_elf);
                current_elf.clear();
            }
        }
        values.push_back(current_elf);
    }
    int biggest_sum = 0;
    for (auto v: values){
        int local_sum = 0;
        for (auto calorie:v){
            local_sum += calorie;
        }
        if (local_sum > biggest_sum){
            biggest_sum = local_sum;
        }
    }
    cout<<biggest_sum<<endl;
    return 0;
}