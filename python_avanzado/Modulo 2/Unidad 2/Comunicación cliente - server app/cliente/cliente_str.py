import socket
import sys
import binascii
import json

HOST, PORT = "localhost", 512
data = " ".join(sys.argv[1:])
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# ################################################333
"""
Formato del mensaje Query

ACCION: ALTA, BAJA, MODIFICACION, CONSULTA, INICIO
NOMBRE
APELLIDO
EDAD
VENCIMIENTO APTO MEDICO
ESTADO APTO MEDICO
"""

mensaje1 = {'ACCION':'INICIO', 'NOMBRE':'PEDRO', 'APELLIDO':'GONZALEZ', 'EDAD':'23' ,'VENC_APTO_MEDICO':'23/02/22', 'ESTADO_APTO':'VENCIDO', 'NUM_SOCIO':'1'} 
mensaje_to_json1 = json.dumps(mensaje1)
mensaje2 = {'ACCION':'ALTA', 'NOMBRE':'PEDRO', 'APELLIDO':'GONZALEZ', 'EDAD':'23' ,'VENC_APTO_MEDICO':'23/02/22', 'ESTADO_APTO':'VENCIDO', 'NUM_SOCIO':'1'}
mensaje_to_json2 = json.dumps(mensaje2)
mensaje3 = {'ACCION':'BAJA', 'NOMBRE':'PEDRO', 'APELLIDO':'GONZALEZ', 'EDAD':'23' ,'VENC_APTO_MEDICO':'23/02/22', 'ESTADO_APTO':'VENCIDO', 'NUM_SOCIO':'3'}
mensaje_to_json3 = json.dumps(mensaje3)
mensaje4 = {'ACCION':'MODIFICACION', 'NOMBRE':'PABLO', 'APELLIDO':'PEREZ', 'EDAD':'15' ,'VENC_APTO_MEDICO':'23/02/22', 'ESTADO_APTO':'VENCIDO', 'NUM_SOCIO':'2'}
mensaje_to_json4 = json.dumps(mensaje4)
mensaje5 = {'ACCION':'CONSULTA', 'NUM_SOCIO':'2'}
mensaje_to_json5 = json.dumps(mensaje5)

print(mensaje_to_json2)

try:
    # ===== ENVIO Y RECEPCIÓN DE MENSAJE 1 =================
    sock.sendto(mensaje_to_json1.encode("UTF-8"), (HOST, PORT))
    received = sock.recvfrom(1024)
    print(received)
    msg_received_dict_format = json.loads(received[0])

    """
        Response
        Formato del mensaje: 

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
    print(msg_received_dict_format)
    print(msg_received_dict_format['ESTADO'])
    print(msg_received_dict_format['DATA_STATUS'])
    print(received[1], end="\n")
    # ===== ENVIO Y RECEPCIÓN DE MENSAJE 2 =================
    sock.sendto(mensaje_to_json2.encode("UTF-8"), (HOST, PORT))
    received = sock.recvfrom(1024)
    print(received)
    msg_received_dict_format = json.loads(received[0])

    """
        Response
        Formato del mensaje: 

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
    print(msg_received_dict_format)
    print(msg_received_dict_format['ESTADO'])
    print(msg_received_dict_format['DATA_STATUS'])
    print(received[1], end="\n")
    # ===== ENVIO Y RECEPCIÓN DE MENSAJE 3 =================
    sock.sendto(mensaje_to_json3.encode("UTF-8"), (HOST, PORT))
    received = sock.recvfrom(1024)
    print(received)
    msg_received_dict_format = json.loads(received[0])

    """
        Response
        Formato del mensaje: 

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
    print(msg_received_dict_format)
    print(msg_received_dict_format['ESTADO'])
    print(msg_received_dict_format['DATA_STATUS'])
    print(received[1], end="\n")
    # ===== ENVIO Y RECEPCIÓN DE MENSAJE 4 =================
    sock.sendto(mensaje_to_json4.encode("UTF-8"), (HOST, PORT))
    received = sock.recvfrom(1024)
    print(received)
    msg_received_dict_format = json.loads(received[0])

    """
        Response
        Formato del mensaje: 

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
    print(msg_received_dict_format)
    print(msg_received_dict_format['ESTADO'])
    print(msg_received_dict_format['DATA_STATUS'])
    print(received[1], end="\n")
     # ===== ENVIO Y RECEPCIÓN DE MENSAJE 5 =================
    sock.sendto(mensaje_to_json5.encode("UTF-8"), (HOST, PORT))
    received = sock.recvfrom(1024)
    print(received)
    msg_received_dict_format = json.loads(received[0])

    """
        Response
        Formato del mensaje: 

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
    print(msg_received_dict_format)
    print(msg_received_dict_format['ESTADO'])
    print(msg_received_dict_format['DATA_STATUS'])
    print(received[1], end="\n")
    # ===== FIN ENVIO Y RECEPCIÓN DE DATOS =================
except:
    print("server caido")