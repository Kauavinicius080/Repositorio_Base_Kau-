import sqlite3

banco = sqlite3.connect('Consultas.db')
cursor = banco.cursor()
#cursor.execute("CREATE TABLE Consultas (Paciente Text,Dia Data,idade INTEREGER,Medico Text)")
cursor.execute("INSERT INTO Consultas VALUES ('Kauã','20/11/25',15,'KID bengala')")   
#cursor.execute("INSERT INTO blibioteca VALUES ('José','jose_meupalnoseupé','25/06/2027','ezequiel')")   
#cursor.execute("INSERT INTO blibioteca VALUES ('carioca','play_boy','22/07/2027','pedro')")   
#cursor.execute("INSERT INTO blibioteca VALUES ('carioca','play_boy','15/06/2027','Ricardo')")   
#cursor.execute("INSERT INTO blibioteca VALUES ('carioca','play_boy','12/06/2027','Juan')")  
#cursor.execute("INSERT INTO blibioteca VALUES ('carioca','play_boy','12/06/2027','Jose')")  
banco.commit()
