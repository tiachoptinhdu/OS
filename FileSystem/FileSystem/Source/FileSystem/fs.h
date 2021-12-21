#pragma once
#include<cstdlib>
#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

#define _CRT_SECURE_NO_WARNINGS
#define min_size 100
#define max_size 4000
#define max_wrong 4

class FileSystem {
public:
    int fileSize;
    struct SuperBlock {	     // Chứa các thông tin về volume 
        char username[20];
        char password[20];
        int num_inodes;
        int num_blocks;
        int size_blocks;
    };

    struct Block
    {
        bool state;     // nếu state = 1 thì dùng được  state: 0 không dùng được
        char data[512];
    };

    struct Inode {      // Lưu trữ các thông tin cơ bản về thư mục hoặc file 
        char name[10];
        char type[10];
        char password[10];
        bool state;
        int Block_Position[8];
    };

    SuperBlock inf;
    Inode* node;
    Block* block;

    FileSystem();
    int Input_Filesize();                       // nhập kích thước file
    void Input_Account();                       // nhập tài khoản
    bool CheckPass(char* user, char* pass);
    bool ChangePassword();
    void Init();                                // hàm init

    // Câu 1: tạo volume
    void Create_Volume();
    void Read_Volume();                         // Đọc volume
    void ReadBlock(int pos, char*& data);
    void WriteBlock(int pos, char* data);

    // Câu 2: Tạo, đổi mật khẩu của volume 
    void Update_Password_Volume();

    // Câu 3: Liệt kê tất cả thông tin inode có nghĩa là tất cả các file
    void List_Of_File();

    //Cãu 4: Đặt đổi khẩu khẩu cho tập tin Inode trong volume
    void Update_Password_Inode(int pos);

    //Câu 5: Chép Import một tập tin từ bên ngoài vào
    void Import(char* data, int size, int inode);

    //Câu 6: Chép outport 1 tập tin bên trong MyFS ra ngoài
    void Outport(int inode_num, char*& data);

    //Câu 7: Xóa 1 tập tin trong MyFS bằng cách qui định tên file bắt đầu bằng %
    void Delete_File_In_Volume(int pos);
    ~FileSystem();
};