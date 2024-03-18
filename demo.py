from campania import Campania
from datetime import date
from error import LargoExcedidoError, SubTipoInvalidoError

# Creación de una instancia de Campania y definición de sus atributos
c = Campania("Campania Demo", date.today(), date.today(), [
    {"tipo": "video", "url_clic": "sin-url", "url_archivo": "sin-url",
     "sub_tipo": "instream", "duracion": 30}
])

try:
    # Solicita al usuario ingresar un nuevo nombre para la campaña
    nombre = input("Ingrese nuevo nombre de la campania:\n")

    # Validación del nombre de la campaña
    if len(nombre) > 250:
        raise LargoExcedidoError("El nombre de la campaña no puede superar los 250 caracteres.")

    # Solicita al usuario ingresar un nuevo subtipo para el anuncio
    sub_tipo = input("Ingrese nuevo sub tipo del anuncio:\n")

    # Validación del subtipo del anuncio
    if sub_tipo not in c.anuncios[0].SUB_TIPOS:
        raise SubTipoInvalidoError(f"Subtipo inválido para el anuncio: {sub_tipo}")

    # Actualiza el nombre de la campaña
    c.nombre = nombre

    # Actualiza el subtipo del primer anuncio en la lista de anuncios
    c.anuncios[0].sub_tipo = sub_tipo

except Exception as e:
    # Manejo de excepciones: si ocurre algún error, se registra en el archivo error.log
    with open("error.log", "a+") as log:
        log.write(f"{e}\n")

