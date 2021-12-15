#include"fs.h"
int main() {
	FileSystem fs;
	// Câu 1: 
	cout << "Test cau 1: Tao Volume" << endl;
	fs.Init();
	strcpy_s(fs.node[99].name, "Tinh.txt");
	fs.node[99].Block_Position[0] = 14;
	fs.node[99].Block_Position[1] = 17;
	fs.Create_Volume();
	char data[512];
	for (int i = 0; i < 512; i++) {
		data[i] = '1';
	}
	fs.WriteBlock(14, data);
	for (int i = 0; i < 512; i++) {
		data[i] = '2';
	}
	fs.WriteBlock(17, data);
	fs.Read_Volume();
	cout << "Test Cau 2:" << endl;
	fs.Update_Password_Volume(); // username = tinh   old password: 123
	cout << "Test Cau 3:" << endl;
	fs.List_Of_File();
	cout << "Test Cau 4: Voi Inode la 10" << endl;
	fs.Update_Password_Inode(10);
	cout << "Check|||Current Inode 10 pass word is: " << fs.node[10].password << endl;
	cout << "Test Cau 5" << endl;
	cout << "Skipped Em chua implement duoc code chi la psuedocode" << endl;
	cout << "Test Cau 6: Voi Inode 99 lay file tinh.txt ra ngoai" << endl;
	char* m = new char[512*2];
	m[512 * 2] = '\0'; // Dat ky tu cuoi cung \0
	fs.Outport(99, m);
	cout << m << endl;
	cout << "Test Cau 7: Delete File File bi delete se co la file 98 co % dau file" << endl;
	fs.Delete_File_In_Volume(98);
	fs.List_Of_File();
	
}