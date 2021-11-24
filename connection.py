from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def conn(request):
    db = QSqlDatabase.addDatabase("QPSQL")

    db.setHostName("localhost")
    db.setPort(5432)
    db.setDatabaseName("PyQT")
    db.setUserName("postgres")
    db.setPassword("1190")
    if db.open():
        print("Connection Success")
        query = QSqlQuery()
        query.exec_(request)
    else:
        print(db.lastError().text())

    db.close()