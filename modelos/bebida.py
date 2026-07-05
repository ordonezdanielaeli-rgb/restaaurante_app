from .producto import Producto
class Bebida(Producto):
     """Clase hija: representa una bebida del restaurante"""
     def __init__(self, nombre: str, precio: float, disponibilidad: bool, volumen_ml: int):
         # Reutilizamos el constructor de la clase padre
         super().__init__(nombre, precio, disponibilidad)
         # Atributo exclusivo de las bebidas (mililitros)
         self.volumen_ml = volumen_ml
     # Sobreescritura del método: comportamiento distinto para bebidas
     def mostrar_informacion(self) -> None:
         estado = "Disponible" if self.disponibilidad else "No disponible"
         print("====================================")
         print("🥤 TIPO: Bebida")
         print(f"📦 Nombre: {self.nombre}")
         print(f"💵 Precio: ${self.obtener_precio():.2f}")
         print(f"📏 Volumen: {self.volumen_ml} ml")
         print(f"📌 Estado: {estado}")
         print("====================================")