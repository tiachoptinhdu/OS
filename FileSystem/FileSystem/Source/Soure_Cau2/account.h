#pragma once
#include"fs.h"

// tạo file account nhằm bảo mật tài khoản trong trường hợp file fs bị lộ


struct account {
	string Username = "tinh";    // người dùng
	string Password = "123";    // mật khẩu
};