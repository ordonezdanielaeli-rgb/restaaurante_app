class Producto:
    """Clase padre que representa un producto general del restaurante"""
    def __init__(self, nombre: str, precio: float, disponibilidad: bool):
        # Atributos comunes a todos los productos
        self.nombre = nombre
        # Encapsulamiento: atributo privado con doble guion bajo
        self.__precio = precio
        self.disponibilidad = disponibilidad 
    # Metodo de acceso para atributo privado
    def obtener_precio(self) -> float:
        return self.__precio
    # Metodo de modificacion con validacion
    def cambiar_precio(self, nuevo_precio: float) -> None:
        """Valida que el precio sea mayor a 0 antes de actualizarlo"""
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
            print(f"✅ Precio de '{self.nombre}' actualizado correctamente")
        else:
            print(f"❌ Error: El precio debe ser mayor a 0")
    # Metodo base a sobrescribir para demostrar polimorfismo
    def mostrar_informacion(self) -> None:
        estado = "Disponible" if self.disponibilidad else "No disponible"
        print(f"📦 Producto: {self.nombre}")
        print(f"💵 Precio: ${self.obtener_precio():.2f}")
        print(f"📌 Estado: {estado}")