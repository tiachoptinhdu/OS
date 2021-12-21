#include"fs.h"
#include"account.h"
using namespace std;

FileSystem::FileSystem() {

}

int FileSystem::Input_Filesize() {
	cout << "Nhap kich thuoc file( don vi MB): ";
	cin >> this->fileSize;
	while (this->fileSize < min_size || this->fileSize > max_size) {// kích thước tổi thiểu là 100MB, tối đa là 4GB
		if (this->fileSize > min_size && this->fileSize < max_size) {
			return this->fileSize;
		}
		else {
			cout << "Khong hop le!!!" << endl;
			cout << "Vui long nhap lai: " << endl;
			cin >> this->fileSize;
		}
	}
}

void FileSystem::Input_Account() {
	SuperBlock inf;
	account admin;
	int So_Lan_Sai = 0;
	do {
		cout << "Nhap Username: ";
		cin >> inf.username;
		cout << "Nhap Password: ";
		cin >> inf.password;
		if (inf.username != admin.Username || inf.password != admin.Password) {
			So_Lan_Sai++;
		}
	} while (So_Lan_Sai < max_wrong);
}

// Hàm CheckPass
bool FileSystem::CheckPass(char* user, char* pass) {
	if (strcmp(inf.username, user) == 0 && strcmp(inf.password, pass) == 0)
		return 1;
	else return 0;
}

// Hàm đổi mật khẩu( không phải đổi trên volume) 
bool FileSystem::ChangePassword() {
	if (strcmp(inf.username, "") == 0) {
		cout << "Khoi tao password:" << endl;
		cout << "Nhap username" << endl;
		cin.get(inf.username, 20, '\n');
		cin.ignore();
		cout << "Nhap password" << endl;
		cin.get(inf.password, 20, '\n');
		cin.ignore();
		return 1;
	}
	else {
		cout << "Nhap password cu" << endl;
		char pass[20];
		cin.get(pass, 20, '\n');
		cin.ignore();

		if (CheckPass(inf.username, pass) == 1) {
			cout << "Nhap password moi" << endl;
			cin.get(inf.password, 20, '\n');
			cin.ignore();

			return 1;
		}
		else {
			cout << "Password Sai" << endl;
			return 0;
		}
	}
	return 0;
}


void FileSystem::Init() {
	// Init the SuperBlock info
	strcpy_s(inf.username, "");
	strcpy_s(inf.password, "");
	inf.num_blocks = 1000;
	inf.num_inodes = 100;
	inf.size_blocks = sizeof(Block);
	ChangePassword();
	// Init node and block
	node = new Inode[inf.num_inodes];
	block = new Block[inf.num_blocks];
	for (int i = 0; i < inf.num_inodes; i++) {
		strcpy_s(node[i].name, "Default");
		strcpy_s(node[i].type, "Null");
		strcpy_s(node[i].password, "");
		node[i].state = 1;
		for (int j = 0; j < 8; j++)
			node[i].Block_Position[j] = -1;
		node[i].state = 1;
	}
	for (int i = 0; i < inf.num_blocks; i++) {
		block[i].state = 0;
	}
}


// Câu 1: tạo volume
void FileSystem::Create_Volume() {
	FILE* file;
	fopen_s(&file, "MyFS.Dat", "w+");
	if (file != NULL) {
		fwrite(&inf, sizeof(struct SuperBlock), 1, file);
		fwrite(node, sizeof(struct Inode), inf.num_inodes, file);
		fwrite(block, sizeof(struct Block), inf.num_blocks, file);
		fclose(file);
	}
}


//Đọc hết volume
void FileSystem::Read_Volume() {
	FILE* file;
	fopen_s(&file, "MyFS.Dat", "r");
	if (file != NULL) {
		fread(&inf, sizeof(struct SuperBlock), 1, file);
		node = new Inode[inf.num_inodes];
		block = new Block[inf.num_blocks];
		fread(node, sizeof(struct Inode), inf.num_inodes, file);
		fread(block, sizeof(struct Block), inf.num_blocks, file);
		fclose(file);
	}
}

void FileSystem::ReadBlock(int pos, char*& data) {
	data = new char[512];
	memcpy(data, block[pos].data, 512);
}

void FileSystem::WriteBlock(int pos, char* data) {
	memcpy(block[pos].data, data, 512);

	// Dong bo hoa xuong file MyFS.Dat
	FILE* file;
	fopen_s(&file, "MyFS.Dat", "w+");
	if (file != NULL) {
		fwrite(&inf, sizeof(struct SuperBlock), 1, file);
		fwrite(node, sizeof(struct Inode), inf.num_inodes, file);
		fwrite(block, sizeof(struct Block), inf.num_blocks, file);
		fclose(file);
	}

}

// Câu 2: Tạo, đổi mật khẩu của volume 
void FileSystem::Update_Password_Volume() {
	ChangePassword();
	FILE* file;
	fopen_s(&file, "MyFS.Dat", "w+");
	if (file != NULL) {
		fwrite(&inf, sizeof(struct SuperBlock), 1, file);
		fwrite(node, sizeof(struct Inode), inf.num_inodes, file);
		fclose(file);
	}
}

// Câu 3: Liệt kê tất cả thông tin inode có nghĩa là tất cả các file
void FileSystem::List_Of_File() {
	for (int i = 0; i < inf.num_inodes; i++)
		cout << "inode " << i << "\t name" ":" << node[i].name << "\t" << "type:" << node[i].type << endl;
}

//Cãu 4: Đặt đổi khẩu khẩu cho tập tin Inode trong volume
void FileSystem::Update_Password_Inode(int pos) {
	if (strcmp(node[pos].password, "") == 0) {
		cout << "Create new password for file" << endl;
		cin.get(node[pos].password, 20, '\n');
		cin.ignore();

		// Ghi password mới xuống file
		FILE* file;
		fopen_s(&file, "MyFS.Dat", "w+");
		if (file != NULL)
		{
			fwrite(&inf, sizeof(struct SuperBlock), 1, file);
			fwrite(node, sizeof(struct Inode), inf.num_inodes, file);

			fclose(file);
		}
	}
	else {
		cout << "Input your old password" << endl;
		char pass[20];
		cin.get(pass, 20, '\n');
		cin.ignore();
		if (strcmp(pass, node[pos].password) == 0) {
			cout << "Create new password for file" << endl;
			cin.get(node[pos].password, 20, '\n');
			cin.ignore();

			// Ghi password xuong file
			FILE* file;
			fopen_s(&file, "MyFS.Dat", "w+");
			if (file != NULL) {
				fwrite(&inf, sizeof(struct SuperBlock), 1, file);
				fwrite(node, sizeof(struct Inode), inf.num_inodes, file);
				fclose(file);
			}
		}
		else {
			cout << "Wrong Password" << endl;
		}
	}
}

//Câu 5: Chép Import một tập tin từ bên ngoài vào
// Này chỉ code ý tưởng, Psuedocode, chưa implement được
void FileSystem::Import(char* data, int size, int inode) {

	// chia cum data thanh cac cum 512 byte
	//Truyen data vao block theo cum 512 byte
	//Tim block_position la block free
	//WriteBlock(block_position, data)

}

//Câu 6: Chép outport 1 tập tin bên trong MyFS ra ngoài
// Này chỉ là code ý tưởng, Psuedocode,  chưa implement được
void FileSystem::Outport(int inode_num, char*& data) {
	for (int i = 0; i < 8; i++) {
		int pos = node[inode_num].Block_Position[i];
		if (pos < 0)
			break;
		char* m;
		ReadBlock(pos, m);
		for (int j = 0; j < 512; j++)
			data[i * 512 + j] = m[j];
	}
}

//Câu 7: Xóa 1 tập tin trong MyFS bằng cách qui định tên file bắt đầu bằng %
void FileSystem::Delete_File_In_Volume(int pos) {
	// Thay đổi tên file đầu tiên bằng %
	node[pos].name[0] = '%';
	FILE* file;
	fopen_s(&file, "MyFS.Dat", "w+");
	if (file != NULL) {
		fwrite(&inf, sizeof(struct SuperBlock), 1, file);
		fwrite(node, sizeof(struct Inode), inf.num_inodes, file);

		fclose(file);
	}
}

FileSystem::~FileSystem() {

}