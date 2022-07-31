import socket
import threading
import socketserver
from pathlib import Path
import os
import sys
import binascii
from datetime import datetime
import netifaces
import json

# global HOST
global PORT


class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        
        # ####################################################
        #   String
        # ####################################################
        """
        Formato del mensaje Query

        ACCION: ALTA, BAJA, MODIFICACION, CONSULTA
        NOMBRE
        APELLIDO
        EDAD
        VENCIMIENTO APTO MEDICO
        ESTADO APTO MEDICO

        Ejemplo: {'ACCION':'ALTA', 'NOMBRE':'PEDRO', 'APELLIDO':'GONZALEZ', 'EDAD':'23' ,'VENC_APTO_MEDICO':'23/02/22', 'ESTADO_APTO':'VENCIDO'}
        """
        print("Data received")

        msg_received_json_format = data.decode("UTF-8")
        msg_received_dict_format = json.loads(msg_received_json_format)
        
        print(data)
        print(msg_received_json_format)
        print(msg_received_dict_format)
        print(msg_received_dict_format['ACCION'])
        print(msg_received_dict_format['NOMBRE'])
        print(msg_received_dict_format['APELLIDO'])
        print(msg_received_dict_format['EDAD'])
        print(msg_received_dict_format['VENC_APTO_MEDICO'])
        print(msg_received_dict_format['ESTADO_APTO'])

        """
        Formato del mensaje Response

        ESTADO:OK, FAIL
        """
        rta = {'ESTADO':'OK'}        
        rta_to_json = json.dumps(rta)
        socket.sendto(rta_to_json.encode("UTF-8"), self.client_address)


if __name__ == "__main__":
    HOST, PORT = "localhost", 512
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()