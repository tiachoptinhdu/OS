#include<iostream>
#include<string>
#include<fstream>
#include<sstream>
#include<iomanip>
#include<ctime>
#include<chrono>
#pragma warning(disable : 4996).

using namespace std;
#define _CRT_SECURE_NO_WARMINGS
#define MAX 20

void ReadFile(string fileName) {
	ifstream file;// file để đọc
	string kq;
	file.open(fileName);
	if (file.is_open()) {// khi mở thành công = true
		while (!file.eof()) {// đọc từng dòng 1 cho tới khi gặp null
			getline(file, kq);
			cout << kq << endl;
		}
	}
	file.close();
}

void RemoveTextFile(string fileName) {
	ofstream file;
	file.open(fileName, ofstream::out | ofstream::trunc);
	file.close();
}

void InputTime(int hour_f[MAX], int minute_f[MAX], int hour_t[MAX], int minute_t[MAX], int& n) {
	for (int i = 0; i < n; i++) {
		cout << "Time from: ";
		cin >> hour_f[i];
		if (hour_f[i] > 24) {
			cout << "Error!!" << endl;
		}
		cin >> minute_f[i];
		if (minute_f[i] > 60) {
			cout << "Error!!" << endl;
		}
		cout << "Time to:   ";
		cin >> hour_t[i];
		if (hour_t[i] > 24) {
			cout << "Error!!" << endl;
		}
		cin >> minute_t[i];
		if (minute_t[i] > 60) {
			cout << "Error!!" << endl;
		}
	}
}

void OutputTime(int hour_f[MAX], int minute_f[MAX], int hour_t[MAX], int minute_t[MAX], int& n) {
	for (int i = 0; i < n; i++) {
		cout << "Time from: ";
		cout << setfill('0') << setw(2) << hour_f[i] << ":" << setfill('0') << setw(2) << minute_f[i] << endl;
		cout << "Time to:   ";
		cout << setfill('0') << setw(2) << hour_t[i] << ":" << setfill('0') << setw(2) << minute_t[i] << endl;
	}
}

void Change_Time(string fileName, int hour_f[MAX], int minute_f[MAX], int hour_t[MAX], int minute_t[MAX], int n) {
	RemoveTextFile(fileName);
	fstream file;
	file.open(fileName);
	if (file.is_open()) {// khi mở thành công = true
		for (int i = 0; i < n; i++) {
			if ((hour_f[i] + minute_f[i] * 60) < (hour_t[i] + minute_t[i] * 60)) {
				file << "F" << setfill('0') << setw(2) << hour_f[i] << ":" << setfill('0') << setw(2) << minute_f[i] << " T" << setfill('0') << setw(2) << hour_t[i] << ":" << setfill('0') << setw(2) << minute_t[i] << endl;
			}
		}
	}
	file.close();
}

bool Check_In_Schedule() {
	time_t now = time(0);
	tm* date_time = localtime(&now);
	float currentTime = date_time->tm_hour * 3600 + date_time->tm_min * 60 + date_time->tm_sec;
	int k = int((currentTime - 31) / 60);
	if ((currentTime - 44) / 60 <= k && k < (currentTime - 31) / 60) {
		return true;
	}
	else {
		return false;
	}
}

int main() {
	while (true)
	{
		int selection;
		cout << "================================================================" << endl;
		cout << "_____Chon chuong trinh_____" << endl;
		cout << "1/ Doc file log.txt" << endl;
		cout << "2/ Doc file time.txt" << endl;
		cout << "3/ Chinh sua time" << endl;
		cout << "4/ Thoat chuong trinh" << endl;
		cout << "Your selection: ";
		cin >> selection;

		cout << "Do something with your selection here" << endl;
		cout << "================================================================" << endl;
		// Xem những gì chương trình C làm
		if (selection == 1) {
			ReadFile("C:\\Users\\teoca\\OneDrive - VNU-HCMUS\\ShareFolder\\log.txt");
		}
		else if (selection == 2) {
			ReadFile("C:\\Users\\teoca\\OneDrive - VNU-HCMUS\\ShareFolder\\time.txt");
		}
		else if (selection == 3) {
			// Chỉnh sửa time 
			int hour_f[MAX];
			int hour_t[MAX];
			int minute_f[MAX];
			int minute_t[MAX];
			int n;
			time_t now = time(0);
			tm* date_time = localtime(&now);
			cout << date_time->tm_hour << ":" << date_time->tm_min << ":" << date_time->tm_sec << endl;
			cout << "Nhap n: ";
			cin >> n;
			InputTime(hour_f, minute_f, hour_t, minute_t, n);

			while (true) {
				if (Check_In_Schedule() == true) {
					Change_Time("C:\\Users\\teoca\\OneDrive - VNU-HCMUS\\ShareFolder\\time.txt", hour_f, minute_f, hour_t, minute_t, n);
					ReadFile("C:\\Users\\teoca\\OneDrive - VNU-HCMUS\\ShareFolder\\time.txt");
					break;
				}
			}
		}
		else {
			break;
		}
	}
}
