import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox


class StudentFrom(QMainWindow):
    def __init__(self):
      super().__init__()
      uic.loadUi("student_from.ui", self)

      self.pushButton.clicked.connect(self.saveData)

    def saveData(self):
      student_id = self.lineEdit.text()
      first_name = self.lineEdit_4.text()
      last_name = self.lineEdit_3.text()
      major = self.lineEdit_2.text()

      QMessageBox.information(
        self,
        "ข้อมูลนักศึกษา",
        f"รหัสนักศึกษา: {student_id}\n"
        f"ชื่อ: {first_name}\n"
        f"นามสกุล: {last_name}\n"
        f"สาขา: {major}\n"
      )
if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  window = StudentFrom()
  window.show()
  sys.exit(app.exec_())