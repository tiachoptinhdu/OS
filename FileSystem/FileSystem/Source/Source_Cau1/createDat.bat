:: câu lệnh này giúp tắt các lệnh gọi ra terminal
@echo off

:: với set /P sẽ yêu cầu người dùng nhập giá trị
set /P n=Please, enter the number of files: 

:: vòng lặp for /L là vòng lặp cơ bản với 3 tham số (bắt đầu, bước tăng, kết thúc)
:: call :Label1 %%X là 1 cách gọi function với tham số truyền vào là %%X 
FOR /L %%X IN (1,1,%n%) DO call :Label1 %%X
:: Sau khi xong vòng lặp, tránh thực thi 1 lần nữa function thì phải jump đến label End 
goto End

:: function sẽ được gọi và đối số để nhận tham số vào sẽ thể hiện ở %1
:Label1
	:: với set /A là lệnh tạo biến kiểu số
	set /A i=%1-1
	:: echo [data] >> file là sẽ ghi data vào file và dấu >> thể hiện sẽ ghi tiếp mà không ghi đè (ghi đè: >)
	echo %i% >> G:\F%i%.dat
	echo %i% >> G:\F%i%.dat
	echo %i% >> G:\F%i%.dat
	echo %i% >> G:\F%i%.dat
	echo %i% >> G:\F%i%.dat
	echo %i% >> G:\F%i%.dat
	echo %i% >> G:\F%i%.dat
	
	set /A isEven=%i% %% 2
	
	if %isEven%==0 (
		:: Câu lệnh fsutil file seteof sẽ đặt kết thúc của file tại vị trí mong muốn 
		:: ở đây là 2048 sẽ tương đương kết thúc file sẽ ở vị trí 2048
		:: Điều này cũng đồng nghĩa với set cứng dung lượng cho file là 2048 byte tương ứng 2 cluster
		fsutil file seteof G:\F%i%.dat 2048
	) else (
		fsutil file seteof G:\F%i%.dat 1024
	)
	goto :eof

:End 

pause