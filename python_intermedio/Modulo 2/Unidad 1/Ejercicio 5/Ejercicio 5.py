"""

Ejercicio 5
Para este ejercicio se partirá de la app adjunta en “Downloads.7z” 
Se pide modificar la estructura del modelo, de forma tal que en lugar de una clase “Abmc” que cree la base de datos y su estructura para solo usar “sqlite3” y   
permita realizar el CRUD, exista una clase Abmc que realice el crud, pero la decisión de cual base de datos utilizar sea tomada en una clase padre llamada “Database”. 
Es decir que el programa debe poder seleccionar el tipo de base a utilizar y el nombre de la misma antes de poder ser utilizado.

Nota: Para simplificar el problema no se utilizará una ventana emergente para la carga del nombre de la base y del tipo de base, solo se agregarán un par de campos 
y un botón en la parte superior de la app. 

"""