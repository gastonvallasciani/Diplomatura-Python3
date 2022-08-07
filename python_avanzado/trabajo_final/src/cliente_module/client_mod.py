import socket
import json

HOST, PORT = "localhost", 512
"""
Query
Formato del mensaje 
-------------------
ACCION: ALTA, BAJA, MODIFICACION, CONSULTA, INICIO
NOMBRE
APELLIDO
EDAD
VENCIMIENTO APTO MEDICO
ESTADO APTO MEDICO
"""
"""
Response
Formato del mensaje: 
--------------------
ESTADO:OK, FAIL
DATA_STATUS:NO, YES
DATA:
formato data
NOMBRE
APELLIDO
EDAD
VENCIMIENTO APTO MEDICO
ESTADO APTO MEDICO
NUM_SOCIO
"""       
class SendToServer():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __str__(self,):
        return("Clase SendToServer()")

    def init_remote_database(self,):
        query = {}
        query['ACCION'] = 'INICIO'
        query_to_json = json.dumps(query)
        try:
            self.sock.sendto(query_to_json.encode("UTF-8"), (HOST, PORT))
            response = self.sock.recvfrom(1024)
            print(response)
            response_dict_format = json.loads(response[0])
            print(response_dict_format)
            print(response_dict_format['ESTADO'])
            print(response_dict_format['DATA_STATUS'])
            print(response[1], end="\n")
        except:
            print("Servidor caido")

    def alta_on_remote_database(self, nombre, apellido, edad, venc_apto_medico, estado_apto_medico):
        query = {}
        query['ACCION']='ALTA'
        query['NOMBRE']=nombre
        query['APELLIDO']=apellido
        query['EDAD']=edad
        query['VENC_APTO_MEDICO']=venc_apto_medico
        query['ESTADO_APTO']=estado_apto_medico
        query_to_json = json.dumps(query)
        try:
            self.sock.sendto(query_to_json.encode("UTF-8"), (HOST, PORT))
            response = self.sock.recvfrom(1024)
            print(response)
            response_dict_format = json.loads(response[0])
            print(response_dict_format)
            print(response_dict_format['ESTADO'])
            print(response_dict_format['DATA_STATUS'])
            print(response[1], end="\n")
        except:
            print("Servidor caido")

    def baja_on_remote_database(self, num_socio):
        query = {}
        query['ACCION']='BAJA'
        query['NUM_SOCIO']=num_socio
        query_to_json = json.dumps(query)
        try:
            self.sock.sendto(query_to_json.encode("UTF-8"), (HOST, PORT))
            response = self.sock.recvfrom(1024)
            print(response)
            response_dict_format = json.loads(response[0])
            print(response_dict_format)
            print(response_dict_format['ESTADO'])
            print(response_dict_format['DATA_STATUS'])
            print(response[1], end="\n")
        except:
            print("Servidor caido")

    def modificacion_on_remote_database(self, num_socio, nombre, apellido, edad, venc_apto_medico, estado_apto_medico):
        query = {}
        query['ACCION']='MODIFICACION'
        query['NUM_SOCIO']=num_socio
        query['NOMBRE']=nombre
        query['APELLIDO']=apellido
        query['EDAD']=edad
        query['VENC_APTO_MEDICO']=venc_apto_medico
        query['ESTADO_APTO']=estado_apto_medico
        query_to_json = json.dumps(query)
        try:
            self.sock.sendto(query_to_json.encode("UTF-8"), (HOST, PORT))
            response = self.sock.recvfrom(1024)
            print(response)
            response_dict_format = json.loads(response[0])
            print(response_dict_format)
            print(response_dict_format['ESTADO'])
            print(response_dict_format['DATA_STATUS'])
            print(response[1], end="\n")
        except:
            print("Servidor caido")

    def consulta_on_remote_database(self, num_socio):
        query = {}
        query['ACCION']='CONSULTA'
        query['NUM_SOCIO']=num_socio
        query_to_json = json.dumps(query)
        try:
            self.sock.sendto(query_to_json.encode("UTF-8"), (HOST, PORT))
            response = self.sock.recvfrom(1024)
            print(response)
            response_dict_format = json.loads(response[0])
            print(response_dict_format)
            print(response_dict_format['ESTADO'])
            print(response_dict_format['DATA_STATUS'])
            print(response[1], end="\n")
        except:
            print("Servidor caido")

    def consulta_todos_on_remote_database(self):
        query = {}
        query['ACCION']='CONSULTA_TODOS'
        query_to_json = json.dumps(query)
        try:
            self.sock.sendto(query_to_json.encode("UTF-8"), (HOST, PORT))
            response = self.sock.recvfrom(1024)
            print(response)
            response_dict_format = json.loads(response[0])
            print(response_dict_format)
            print(response_dict_format['ESTADO'])
            print(response_dict_format['DATA_STATUS'])
            print(response[1], end="\n")
            if(response_dict_format['DATA_STATUS'] == 'SI'):
                return response_dict_format['TODOS']
        except:
            print("Servidor caido")

    def cantidad_socios_on_remote_database(self):
        query = {}
        query['ACCION']='CANTIDAD_REGISTROS'
        query_to_json = json.dumps(query)
        try:
            self.sock.sendto(query_to_json.encode("UTF-8"), (HOST, PORT))
            response = self.sock.recvfrom(1024)
            print(response)
            response_dict_format = json.loads(response[0])
            print(response_dict_format)
            print(response_dict_format['ESTADO'])
            print(response_dict_format['DATA_STATUS'])
            print(response[1], end="\n")
            if(response_dict_format['DATA_STATUS'] == 'SI'):
                return response_dict_format['CANTIDAD_REGISTROS']
        except:
            print("Servidor caido")


    

    


