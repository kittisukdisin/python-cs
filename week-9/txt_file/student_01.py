import os
from pathlib import Path
class TXT :
    def __int__(self):
        dir = Path ("student.txt")
        self.dir = dir
    def Creted():
        text_data = """  Hello ! E YUY  """
        with open("student.txt", "w", encoding="utf-8") as file:
            try:
                file.write(text_data)
                print("บันทึกไฟล์เรียบร้อยเเล้ว")
            except:
                print("บันทึกไม่ได้")

    def Reader():
        with open("student.txt", "r", encoding="utf-8") as file:
            try:
                print(file.read())
            except:
                print("อ่านไฟล์ไม่ได้")
    def Update(data_update):
        with open("student.txt", "a", encoding="utf-8") as file:
            try:
                file.write(data_update)
                print("อัพเดทข้อมูลเรียบร้อยเเล้ว")
            except:
                print("ไม่สามารถอัพเดทข้อมูลไม่ได้")

    def Del(fileName):
        file = fileName
        if (os.path.exists(file)):
            os.remove(file)
            print("ลบไฟล์เรียบร้อยเเล้ว")
        else:
            print("ไม่พบไฟล์", file)
#-------------------------------
txt = TXT()
while True:
    print("------------------menu-----------------")
    print("Q = Quit, C = Create, R = Read, U = Update, D = Delete ")
    print("------------------menu--------------------")
    status = input("ต้องการ : ")
    if(status.lower() == "q"):
        break
    elif(status.lower() == "c"):
        txt.Creted()
    elif(status.lower() == "r"):
        txt.Reader()
    elif(status.lower() == "u"):
        inp = input("data update : ")
        txt.Update()
    elif(status.lower() == "d"):
        txt.Del("student.txt")