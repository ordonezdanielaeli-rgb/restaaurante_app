from modelos import Producto
class Restaurante:
     """Clase de servicio: administra la lista de productos del restaurante"""
     def __init__(self, nombre_restaurante: str):
         self.nombre_restaurante = nombre_restaurante
         # Lista para almacenar cualquier tipo de Producto (Platillo o Bebida)
         self.productos_registrados: list[Producto] = []
     def agregar_producto(self, producto: Producto) -> None:
         """Agrega un nuevo producto al listado"""
         self.productos_registrados.append(producto)
         print(f"✅ Producto '{producto.nombre}' agregado correctamente")
     def mostrar_todos_productos(self) -> None:
         """Recorre la lista y usa polimorfismo: ejecuta el método según el tipo de objeto"""
         print(f"\n📋 LISTA DE PRODUCTOS - {self.nombre_restaurante.upper()}")
         print("------------------------------------")
         for producto in self.productos_registrados:
             producto.mostrar_informacion()