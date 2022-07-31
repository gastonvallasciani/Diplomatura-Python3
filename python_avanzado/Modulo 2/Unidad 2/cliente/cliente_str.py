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

ACCION: ALTA, BAJA, MODIFICACION, CONSULTA
NOMBRE
APELLIDO
EDAD
VENCIMIENTO APTO MEDICO
ESTADO APTO MEDICO
"""

mensaje = {'ACCION':'ALTA', 'NOMBRE':'PEDRO', 'APELLIDO':'GONZALEZ', 'EDAD':'23' ,'VENC_APTO_MEDICO':'23/02/22', 'ESTADO_APTO':'VENCIDO'}
mensaje_to_json = json.dumps(mensaje)

print(mensaje_to_json)

try:
    # ===== ENVIO Y RECEPCIÓN DE DATOS =================
    sock.sendto(mensaje_to_json.encode("UTF-8"), (HOST, PORT))
    received = sock.recvfrom(1024)
    print(received)
    msg_received_dict_format = json.loads(received[0])

    """
    Formato del mensaje Response

    ESTADO:OK, FAIL
    """
    print(msg_received_dict_format)
    print(msg_received_dict_format['ESTADO'])
    print(received[1], end="\n")
    # ===== FIN ENVIO Y RECEPCIÓN DE DATOS =================
except:
    print("server caido")