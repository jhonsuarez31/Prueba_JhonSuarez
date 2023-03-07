# Prueba_JhonSuarez

Crear ambiente virtual de python
 python -m virtualenv venv  
 
 Instalación de flask: 
 pip install flask
 
 Instalación de SQLALCHEMY
  pip install SQLAlchemy
 
  Instalación de mysqlclient
  pip install mysqlclient
 
 Instalación de openpyxl 
 
 pip install openpyxl

Requerimients 


pip install : 

autopep8==2.0.2
click==8.1.3
colorama==0.4.6
et-xmlfile==1.1.0
Flask==2.2.3
Flask-SQLAlchemy==3.0.3
greenlet==2.0.2
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.2
mysqlclient==2.1.1
numpy==1.24.2
openpyxl==3.1.1
pandas==1.5.3
pycodestyle==2.10.0
python-dateutil==2.8.2
pytz==2022.7.1
six==1.16.0
SQLAlchemy==2.0.5.post1
tomli==2.0.1
typing_extensions==4.5.0
Werkzeug==2.2.3


Base de datos:
MySQL:
Las credenciales para la conexión a la base de datos 
mysql://root:3138533232@localhost/falabella 

CREATE TABLE type_document (
id INTEGER NOT NULL,
type_document VARCHAR(200),
PRIMARY KEY (id)
);

CREATE TABLE user (
id INTEGER NOT NULL,
number_ID VARCHAR(200),
name VARCHAR(200),
last_name VARCHAR(200),
email VARCHAR(200),
phone VARCHAR(200),
type_id INTEGER,
PRIMARY KEY (id),
FOREIGN KEY(type_id) REFERENCES type_document(id)
);





