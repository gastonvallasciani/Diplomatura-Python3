import socketserver
import json
from sqlite3_module.sqlite_mod import DatabaseManager

# global HOST
global PORT


class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.database_object = DatabaseManager()

        data = self.request[0].strip()
        socket = self.request[1]
        rta={}
        """
        Query
        Formato del mensaje: 

        ACCION: ALTA, BAJA, MODIFICACION, CONSULTA, INICIO
        NOMBRE
        APELLIDO
        EDAD
        VENCIMIENTO APTO MEDICO
        ESTADO APTO MEDICO
        NUM_SOCIO

        Ejemplo: {'ACCION':'ALTA', 'NOMBRE':'PEDRO', 'APELLIDO':'GONZALEZ', 'EDAD':'23' ,'VENC_APTO_MEDICO':'23/02/22', 'ESTADO_APTO':'VENCIDO', 'NUM_SOCIO':''}
        """
        msg_received_json_format = data.decode("UTF-8")
        msg_received_dict_format = json.loads(msg_received_json_format)
        
        print(msg_received_dict_format)

        if(msg_received_dict_format['ACCION'] == "INICIO"):
            print("Iniciar base")
            self.database_object.iniciar_base()
            rta['ESTADO']='OK'
            rta['DATA_STATUS']='NO'
        elif(msg_received_dict_format['ACCION'] == "ALTA"):
            print("Registro agregado a la base de datos")
            self.database_object.insertar(msg_received_dict_format['NOMBRE'] 
                , msg_received_dict_format['APELLIDO']
                , msg_received_dict_format['EDAD']
                , msg_received_dict_format['VENC_APTO_MEDICO']
                , msg_received_dict_format['ESTADO_APTO']
                )
            rta['ESTADO']='OK'
            rta['DATA_STATUS']='NO'
        elif(msg_received_dict_format['ACCION'] == "BAJA"):
            print("Registro borrado a la base de datos")
            self.database_object.borrar(msg_received_dict_format['NUM_SOCIO'])
            rta['ESTADO']='OK'
            rta['DATA_STATUS']='NO'
        elif(msg_received_dict_format['ACCION'] == "MODIFICACION"):
            print("Registro modificado en la base de datos")
            self.database_object.actualizar(msg_received_dict_format['NUM_SOCIO'] 
                , msg_received_dict_format['NOMBRE']
                , msg_received_dict_format['APELLIDO']
                , msg_received_dict_format['EDAD']
                , msg_received_dict_format['VENC_APTO_MEDICO']
                , msg_received_dict_format['ESTADO_APTO']
                )
            rta['ESTADO']='OK'
            rta['DATA_STATUS']='NO'
        elif(msg_received_dict_format['ACCION'] == "CONSULTA"):
            print("Registro consultado en la base de datos")
            rta_consulta = list(self.database_object.seleccionar(msg_received_dict_format['NUM_SOCIO']))

            rta['ESTADO']='OK'
            rta['DATA_STATUS']='SI'
            rta['NUM_SOCIO']=rta_consulta[0]
            rta['NOMBRE']=rta_consulta[1]
            rta['APELLIDO']=rta_consulta[2]
            rta['EDAD']=rta_consulta[3]
            rta['VENC_APTO_MEDICO']=rta_consulta[4]
            rta['ESTADO_APTO']=rta_consulta[5]
        else:
            print("comando no soportado")
            rta['ESTADO']='FAIL'

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
        rta_to_json = json.dumps(rta)
        socket.sendto(rta_to_json.encode("UTF-8"), self.client_address)


if __name__ == "__main__":
    HOST, PORT = "localhost", 512
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()