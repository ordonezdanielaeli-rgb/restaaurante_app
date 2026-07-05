from .producto import Producto
class Platillo(Producto):
     """Clase hija: representa un platillo/comida del restaurante"""
     def __init__(self, nombre: str, precio: float, disponibilidad: bool, tiempo_preparacion: int):
         # Reutilizamos el constructor de la clase padre con super()
         super().__init__(nombre, precio, disponibilidad)
         # Atributo exclusivo de los platillos (minutos)
         self.tiempo_preparacion = tiempo_preparacion
     # Sobreescritura del método: comportamiento distinto para platillos
     def mostrar_informacion(self) -> None:
         estado = "Disponible" if self.disponibilidad else "No disponible"
         print("====================================")
         print("🍽️  TIPO: Platillo")
         print(f"📦 Nombre: {self.nombre}")
         print(f"💵 Precio: ${self.obtener_precio():.2f}")
         print(f"⏱️  Tiempo preparación: {self.tiempo_preparacion} minutos")
         print(f"📌 Estado: {estado}")
         print("====================================")