# Importa la clase ABC y la función abstractmethod del módulo abc
from abc import ABC, abstractmethod
from error import SubTipoInvalidoError
from anuncio import Anuncio

# Definición de la clase Anuncio como clase abstracta
class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str,
            url_clic: str, sub_tipo: str) -> None:
        # Inicializa los atributos del anuncio
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    # Método de propiedad para acceder al ancho
    @property
    def ancho(self) -> int:
        return self.__ancho

    # Método setter para el ancho
    @ancho.setter
    def ancho(self, nuevo_ancho: int) -> None:
        if nuevo_ancho > 0:
            self.__ancho = nuevo_ancho
        else:
            raise ValueError("El ancho debe ser un valor positivo")

    # Método de propiedad para acceder al alto
    @property
    def alto(self) -> int:
        return self.__alto

    # Método setter para el alto
    @alto.setter
    def alto(self, nuevo_alto: int) -> None:
        if nuevo_alto > 0:
            self.__alto = nuevo_alto
        else:
            raise ValueError("El alto debe ser un valor positivo")

    # Método setter y de propiedad para archivo
    @property
    def archivo(self) -> str:
        """Devuelve la ruta del archivo del anuncio."""
        return self.__archivo

    @archivo.setter
    def archivo(self, ruta_archivo: str) -> None:
        """Establece la ruta del archivo del anuncio."""
        self.__archivo = ruta_archivo

    # Método setter y de propiedad para clic
    #Devuelve el número de clics que ha recibido el anuncio.
    @property
    def clic(self) -> int:        
        return self.__clic

    #Establece el número de clics que ha recibido el anuncio.
    @clic.setter
    def clic(self, nuevo_clic: int) -> None:        
        if nuevo_clic >= 0:
            self.__clic = nuevo_clic
        else:
            raise ValueError("El número de clics no puede ser negativo")


    # Método setter para el subtipo
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo: str) -> None:
        if (isinstance(self, Video) and sub_tipo not in Video.SUB_TIPOS
        or isinstance(self, Display) and sub_tipo not in Display.SUB_TIPOS
        or isinstance(self, Social) and sub_tipo not in Social.SUB_TIPOS):
            raise SubTipoInvalidoError("El sub tipo indicado no está permitido para este formato")
        else:
            self.__sub_tipo = sub_tipo

    # Método estático para mostrar los formatos disponibles
    @staticmethod
    def mostrar_formatos() -> None:  
        print("FORMATO VIDEO:")
        print("==============")
        for v in Video.SUB_TIPOS:
            print(f"- {v}")

        print("FORMATO DISPLAY:")
        print("==============")
        for d in Display.SUB_TIPOS:
            print(f"- {d}")

        print("FORMATO SOCIAL:")
        print("==============")
        for s in Social.SUB_TIPOS:
            print(f"- {s}")

    # Método abstracto para comprimir los anuncios
    @abstractmethod
    def comprimir_anuncios(self) -> None:  
        pass

    # Método abstracto para redimensionar los anuncios
    @abstractmethod
    def redimensionar_anuncio(self) -> None:  
        pass

    #Devuelve una representación textual del anuncio.
    def __str__(self) -> str:        
        return f"Anuncio: {self.tipo} - {self.sub_tipo} ({self.ancho}x{self.alto})"

    #Devuelve la URL del archivo del anuncio.
    def get_url_archivo(self) -> str:        
        return self.__url_archivo

    #Devuelve la URL de clic del anuncio.
    def get_url_clic(self) -> str:        
        return self.__url_clic

#Clase que representa un anuncio de display.
class Display(Anuncio):
    SUB_TIPOS = ("banner", "interstitial")
    #Inicializa un nuevo anuncio de display.
    def __init__(self, ancho: int, alto: int, url_archivo: str,
                  url_clic: str, sub_tipo: str) -> None:        
        super().__init__(ancho=ancho, alto=alto, url_archivo=url_archivo,
                         url_clic=url_clic, sub_tipo=sub_tipo)
    # Muestra un mensaje indicando que la compresión de anuncios display no está implementada aún.
    def comprimir_anuncio(self) -> None:
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")
    #Muestra un mensaje indicando que el redimensionamiento de anuncios display no está implementado aún.
    def redimensionar_anuncio(self) -> None:        
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")


#Clase que representa un anuncio de redes sociales.
class Social(Anuncio): 
    SUB_TIPOS = ("facebook", "instagram")
    def __init__(self, ancho: int, alto: int, url_archivo: str,
                  url_clic: str, sub_tipo: str) -> None:
        super().__init__(ancho=ancho, alto=alto, url_archivo=url_archivo,
                         url_clic=url_clic, sub_tipo=sub_tipo)

#Muestra un mensaje indicando que la compresión de anuncios de redes sociales no está implementada aún.
    def comprimir_anuncio(self) -> None:     
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

#Muestra un mensaje indicando que el redimensionamiento de anuncios de redes sociales no está implementado aún.
    def redimensionar_anuncio(self) -> None:        
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")