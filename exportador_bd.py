import pymysql

############### CONFIGURAR ESTO ###################
# Abre conexion con la base de datos
db = pymysql.connect("localhost","bitcoin_addr_finder","BitC01n","digital_address")
##################################################

# prepare a cursor object using cursor() method
cursor = db.cursor()

# ejecuta el SQL query usando el metodo execute().
cursor.execute("SELECT VERSION()")

# procesa una unica linea usando el metodo fetchone().
data = cursor.fetchone()
print ("Database version : {0}".format(data))

# desconecta del servidor
db.close()








