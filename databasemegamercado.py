import pyodbc
from PyQt5 import QtWidgets

def conexion():
    server = 'LAPTOP-HT380DU1\SQLEXPRESS01'
    user = 'manuel'
    password = '00100267590'
    database = 'MegaMercado'
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+user+';PWD='+ password)
    return(conn)    


def mensaje(status,mensaje):
	msg= QtWidgets.QMessageBox()
	msg.setText(mensaje)
	msg.setWindowTitle(status)
	return msg
	error = True

def  mensaje1(modo, mensaje):
	msg= QtWidgets.QMessageBox()
	msg.setText(mensaje)
	msg.setWindowTitle(modo)
	return msg
	error = True
 
