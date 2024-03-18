# Importar las clases necesarias
from error import LargoExcedidoError, SubTipoInvalidoError
from anuncio import Video, Social, Display
from datetime import date

# Definir la clase Campania
class Campania():
    def __init__(self, nombre: str, fecha_inicio: date,
            fecha_termino: date, anuncios: list) -> None:
# Inicializa la campania con nombre, fechas de inicio y termino, y una lista de anuncios
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = anuncios
    # Método para obtener la instancia del tipo correcto de anuncio
    def __obtener_instancia_anuncio(self, anuncio: dict):
        tipo_anuncio = anuncio.get("tipo", "").lower()
        ancho = anuncio.get("ancho", 0)
        alto = anuncio.get("alto", 0)
        url_archivo = anuncio.get("url_archivo", "")
        url_clic = anuncio.get("url_clic", "")
        sub_tipo = anuncio.get("sub_tipo", "")
        duracion = anuncio.get("duracion", 0)

        if tipo_anuncio == "video":
            return Video(url_archivo, url_clic, sub_tipo, duracion)
        elif tipo_anuncio == "social":
            return Social(ancho, alto, url_clic, url_clic, sub_tipo)
        else:
            return Display(ancho, alto, url_clic, url_clic, sub_tipo)

    # Método de propiedad para acceder al nombre de la campania
    @property
    def nombre(self) -> str:
        return self.__nombre

    # Método setter para el nombre de la campania
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        # Verifica que el nombre no supere los 250 caracteres
        if len(nombre) > 250:
            raise LargoExcedidoError("El nombre de la campaña no puede superar los 250 caracteres.")
        self.__nombre = nombre
    # Método de propiedad para acceder a la fecha de inicio
    @property
    def fecha_inicio(self) -> date:
        return self.__fecha_inicio

    # Método setter para la fecha de inicio
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio: date) -> None:
        self.__fecha_inicio = fecha_inicio

    # Método de propiedad para acceder a la fecha de término
    @property
    def fecha_termino(self) -> date:
        return self.__fecha_termino

    # Método setter para la fecha de término
    @fecha_termino.setter
    def fecha_termino(self, fecha_termino: date) -> None:
        self.__fecha_termino = fecha_termino

    # Método de propiedad para acceder a la lista de anuncios
    @property
    def anuncios(self) -> list:
        return self.__anuncios

    # Método para obtener una representación en cadena de la campania
    def __str__(self):
        cant_video = len(list(filter(
            lambda x: isinstance(x, Video), self.anuncios
        )))
        cant_display = len(list(filter(
            lambda x: isinstance(x, Display), self.anuncios
        )))
        cant_social = len(list(filter(
            lambda x: isinstance(x, Social), self.anuncios
        )))

        return (f"Nombre de la Campania: {self.__nombre}\n"
                f"Anuncios: {cant_video} Video, "
                f"{cant_display} Display, "
                f"{cant_social} Social")

# Clase Display que hereda de Anuncio
class Display(Anuncio):
# Constante de subtipos para anuncios Display
    SUB_TIPOS = ("banner", "interstitial")
# Constructor de la clase Display
    def __init__(self, ancho: int, alto: int, url_archivo: str,
                  url_clic: str, sub_tipo: str) -> None:
        super().__init__(ancho=ancho, alto=alto, url_archivo=url_archivo,
                         url_clic=url_clic, sub_tipo=sub_tipo)
# Método para comprimir anuncios de Display
    def comprimir_anuncio(self) -> None:
        raise NotImplementedError("Compresión de anuncios display no implementada aún")
# Método para redimensionar anuncios de Display
    def redimensionar_anuncio(self) -> None:
        raise NotImplementedError("Redimensionamiento de anuncios display no implementada aún")
# Clase Social que hereda de Anuncio
class Social(Anuncio):
# Constante de subtipos para anuncios en redes sociales
    SUB_TIPOS = ("facebook", "instagram")
# Constructor de la clase Social
    def __init__(self, ancho: int, alto: int, url_archivo: str,
                  url_clic: str, sub_tipo: str) -> None:
        super().__init__(ancho=ancho, alto=alto, url_archivo=url_archivo,
                         url_clic=url_clic, sub_tipo=sub_tipo)
# Método para comprimir anuncios en redes sociales
    def comprimir_anuncio(self) -> None:
        raise NotImplementedError("Compresión de anuncios de redes sociales no implementada aún")
# Método para redimensionar anuncios en redes sociales
    def redimensionar_anuncio(self) -> None:
        raise NotImplementedError("Redimensionamiento de anuncios de redes sociales no implementada aún")
# Método para obtener la plataforma de un anuncio en redes sociales
    def obtener_plataforma(self) -> str:
        if self.sub_tipo == "facebook":
            return "Facebook"
        elif self.sub_tipo == "instagram":
            return "Instagram"
        else:
            raise SubTipoInvalidoError(f"Subtipo inválido para anuncio social: {self.sub_tipo}")
