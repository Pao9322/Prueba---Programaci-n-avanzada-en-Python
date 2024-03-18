from anuncio import Anuncio
from error import LargoExcedidoError

class Video(Anuncio): 
    SUB_TIPOS = ("instream", "outstream")
    def __init__(self, duracion: int, url_archivo: str,
                  url_clic: str, sub_tipo: str) -> None:      
        super().__init__(ancho=1, alto=1, url_archivo=url_archivo,
                         url_clic=url_clic, sub_tipo=sub_tipo)
        self.__duracion = duracion if duracion > 0 else 5

    # **Método de propiedad y setter la duración**
    #Devuelve la duración del video en segundos.
    @property
    def duracion(self) -> int:        
        return self.__duracion

    #Establece la duración del video en segundos.
    @duracion.setter
    def duracion(self, nueva_duracion: int) -> None:
        if nueva_duracion > 0:
            self.__duracion = nueva_duracion
        else:
            raise LargoExcedidoError("La duración del video no puede ser negativa")

    # **Métodos para comprimir y redimensionar anuncios**
    #Muestra un mensaje indicando que la compresión de video no está implementada aún.
    def comprimir_anuncio(self) -> None:
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    # Muestra un mensaje indicando que el recorte de video no está implementado aún.
    def redimensionar_anuncio(self) -> None:
        print("RECORTE DE VIDEO NO IMPLEMENTADA AÚN")