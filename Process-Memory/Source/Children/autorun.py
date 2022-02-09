import os
import getpass

USER_NAME = getpass.getuser()

#Add too startup  
# Reference: https://stackoverflow.com/questions/4438020/how-to-start-a-python-file-while-windows-starts
def startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = f'C:/Users/{USER_NAME}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'
    print(bat_path)
    with open(bat_path + '/' + "open.bat", "w+") as bat_file:
        bat_file.write(f'start "" {file_path}/C.py')
    print(f'start "" {file_path}/C.py')
startup()