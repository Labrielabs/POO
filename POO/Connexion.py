import mysql.connector as mysql


db = mysql.connect(
    user = "root",
    password = "MariaDB",
    host = "localhost",
    database = "ecole"
)
requete = db.cursor()
requete.execute("SELECT * FROM ETUDIANTS")
etudiant = requete.fetchall()
print(etudiant)