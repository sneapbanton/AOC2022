
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
    vector<int> biggest_sum = {0,0,0};
    for (auto v: values){
        int local_sum = 0;
        for (auto calorie:v){
            local_sum += calorie;
        }
        for (int i = 0; i < 3; ++i){
            if (local_sum > biggest_sum.at(i)){
                biggest_sum.insert(biggest_sum.begin()+i, local_sum);
                break;
            }
        }
    }
    for (int i = 0; i<3; ++i){
        cout<<biggest_sum.at(i)<<endl;
    }
    cout<<biggest_sum.at(0)+biggest_sum.at(1)+biggest_sum.at(2)<<endl;
    return 0;
}