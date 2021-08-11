# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginmegamercado.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc
import databasemegamercado
from databasemegamercado import mensaje
from databasemegamercado import  mensaje1

class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
    
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color:rgb(255, 255, 255)")


        #Espacio para poner el titulo de "Megamercado"

        self.foto = QtWidgets.QLabel(self.centralwidget)
        self.foto.setGeometry(QtCore.QRect(50, 30, 131, 111))
        self.foto.setText("")
        self.foto.setTextFormat(QtCore.Qt.RichText)
        self.foto.setPixmap(QtGui.QPixmap("../Users/Sonia Iturbides/Downloads/Logo con Casa Estilo de Vida Cooper (3).png"))
        self.foto.setScaledContents(True)
        self.foto.setObjectName("foto")


        self.usuario = QtWidgets.QLabel(self.centralwidget)
        self.usuario.setGeometry(QtCore.QRect(200, 40, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.usuario.setFont(font)
        self.usuario.setScaledContents(False)
        self.usuario.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono ")
        font.setPointSize(13)
        self.usuario.setFont(font)
        self.usuario.setObjectName("usuario")

        self.contrasena = QtWidgets.QLabel(self.centralwidget)
        self.contrasena.setGeometry(QtCore.QRect(220, 80, 91, 21))
        self.contrasena.setFont(font)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono ")
        font.setPointSize(13)
        self.contrasena.setFont(font)
        self.contrasena.setObjectName("contrasena")

        self.leusuario = QtWidgets.QLineEdit(self.centralwidget)
        self.leusuario.setGeometry(QtCore.QRect(320, 40, 113, 20))
        self.leusuario.setObjectName("leusuario")

        self.lecontrasena = QtWidgets.QLineEdit(self.centralwidget)
        self.lecontrasena.setGeometry(QtCore.QRect(320, 80, 113, 20))
        self.lecontrasena.setObjectName("lecontrasena")

        self.Registrarse = QtWidgets.QPushButton(self.centralwidget)
        self.Registrarse.setGeometry(QtCore.QRect(220, 160, 105, 31))
        self.Registrarse.setObjectName("Registrarse")
        self.Registrarse.setStyleSheet("""
        QPushButton{       
        color:rgb(255, 255, 255);
        background-color: rgb(225, 25, 25);
        font: 13 13pt \"Roboto Mono\";
        font-weight: bold;}
        """)
     
        self.Aceptar = QtWidgets.QPushButton(self.centralwidget)
        self.Aceptar.setGeometry(QtCore.QRect(335, 160, 100, 31))
        self.Aceptar.setObjectName("Aceptar")
        self.Aceptar.setStyleSheet("color:rgb(255, 255, 255);\n"
        "background-color: rgb(33, 167, 218);\n"
        "font: 13 13pt \"Roboto Mono\";\n"
        "font-weight: bold;\n"
        "") 
        self.Aceptar.clicked.connect(self.validarusuario)      

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.usuario.setText(_translate("MainWindow", "Usuario"))
        self.contrasena.setText(_translate("MainWindow", "Contraseña"))
        self.Registrarse.setText(_translate("MainWindow", "Registrarse"))
        self.Aceptar.setText(_translate("MainWindow", "Aceptar"))

   
    def validarusuario(self):
        error = False

        if error == False:
           if not self.leusuario.text():
              conectar = databasemegamercado.conexion()
              mycursor = conectar.cursor()
              sql = "select * from login"
              mycursor.execute(sql)
              misdatos = mycursor.fetchall()

            
              msg= mensaje("OK", "El usuario no puede estar en blanco")
              msg.exec()
              error = True
              self.leusuario.setFocus() 

        if error == False:
            if not self.lecontrasena.text():
                conectar = databasemegamercado.conexion()
                mycursor = conectar.cursor()
                sql = "select * from login"
                mycursor.execute(sql)
                misdatos = mycursor.fetchall()

                msg = mensaje("OK", "La contrasena no puede estar en blanco")
                msg.exec()
                error = True
                self.lecontrasena.setFocus()

        if error == False:
            conectar = databasemegamercado.conexion()
            mycursor = conectar.cursor()
            sql = "SELECT * FROM login WHERE log_Usuario ="+"'"+ self.leusuario.text()+"'"
            mycursor.execute(sql)

            misdatos = mycursor.fetchall()

            if mycursor.rowcount == 0:
                msg= mensaje1 ("Error", "El usuario es invalido")
                msg.exec()
                error = True
                self.leusuario.setFocus()

            else: 
                conectar = databasemegamercado.conexion()
                mycursor = conectar.cursor()
                sql = "SELECT * FROM login WHERE Log_Contrasena = "+"'"+ self.lecontrasena.text()+"'"
                mycursor.execute(sql)

                misdatos = mycursor.fetchall()

                if mycursor.rowcount == 0:
                    conectar = databasemegamercado.conexion()
                    mycursor = conectar.cursor()
                    sql = "SELECT * FROM login WHERE log_Usuario = "+"'"+ self.leusuario.text()+"'"
                    mycursor.execute(sql)

                    misdatos = mycursor.fetchall()

                    if misdatos [0][0] == None or misdatos [0][0] == 0:
                     wregistro = 0
                    else:
                     wregistro = misdatos [0][0]
                      

                    conectar = databasemegamercado.conexion()
                    mycursor = conectar.cursor()
                    sql="UPDATE login SET Log_Ingreso = "+str(wregistro+1)+" WHERE log_Usuario ="+"'"+self.leusuario.text()+"'"
                    mycursor.execute(sql)
                    conectarsql.commit() 

                    if wregistro >= 3:
                     msg= mensaje1 ("Error", "Su usuario ha excedido el numero de intentos")
                     msg.exec()

                else: 
                    conectar =  databasemegamercado.conexion()
                    mycursor = conectar.cursor()
                    sql="UPDATE login SET Log_Ingreso  = 0 WHERE log_Usuario="+"'"+ self.leusuario.text()+"'"
                    mycursor.execute(sql)
                    conectarsql.commit()
                    

                 


if __name__ == "__main__":
   import sys
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow()
   ui = Ui_MainWindow()
   ui.setupUi(MainWindow)
   MainWindow.show()
   sys.exit(app.exec_())
