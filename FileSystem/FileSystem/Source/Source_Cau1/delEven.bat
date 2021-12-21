:: câu lệnh này giúp tắt các lệnh gọi ra terminal
@echo off

:: với set /A là lệnh tạo biến kiểu số
set /A index=0

:: vòng lặp for /R là vòng lặp sẽ duyệt qua tất cả các file ở path truyền vào với tham số là tên file mong muốn
:: ở đây tên file mong muốn chỉ cần bắt đầu là F và kết thúc là .dat nên sẽ truyền vào F*.dat với * là bất kỳ
:: call :Label1 %%X là 1 cách gọi function với tham số truyền vào là %%f 
FOR /R "G:" %%f IN (F*.dat) DO call :Label1 %%f
:: Sau khi xong vòng lặp, tránh thực thi 1 lần nữa function thì phải jump đến label End 
goto End 

:Label1
	set file=%1
	::echo index=[%index%] : %file% 
	set /A checkEven=%index% %% 2
	if %checkEven%==0 (
		:: Hiển thị cho người dùng biết các file đã được delete
		echo file: %file% is deleted
		del %file%
	)
	set /A index+=1
	goto :eof

:End 
pause
