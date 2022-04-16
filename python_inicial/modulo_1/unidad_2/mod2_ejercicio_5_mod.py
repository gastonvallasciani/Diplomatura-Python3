def calculo_perimetro_circunferencia_en_funcion_del_radio(radio_local):
    pi = 3.1416
    perimetro = 2 * float(radio_local) * pi
    return(perimetro)

def calculo_area_circunferencia_en_funcion_del_radio(radio_local):
    radio_local = float(radio_local)
    pi = 3.1416
    area = pi * (radio_local ** 2)
    return(area)

def incrementar_valor_enetero_en_10_porciento(valor_entero_local):
    valor_incrementado_local = float(valor_entero_local) * 1.1
    return(valor_incrementado_local)