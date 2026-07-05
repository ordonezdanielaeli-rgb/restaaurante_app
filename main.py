from modelos import Platillo, Bebida
from servicios import Restaurante
if __name__ == "__main__":
     # 1. Crear instancia del servicio Restaurante
     mi_restaurante = Restaurante("Delicias del Sur")
     # 2. Crear objetos de Platillo (mínimo 2)
     plato1 = Platillo(
         nombre="Seco de Pollo",
         precio=5.50,
         disponibilidad=True,
         tiempo_preparacion=30
     )
     plato2 = Platillo(
         nombre="Sancocho",
         precio=4.75,
         disponibilidad=False,
         tiempo_preparacion=20
     )
     # 3. Crear objetos de Bebida (mínimo 2)
     bebida1 = Bebida(
         nombre="Horchata fria/caliente",
         precio=1.50,
         disponibilidad=True,
         volumen_ml=500
     )
     bebida2 = Bebida(
         nombre="Jugo de mora",
         precio=2.25,
         disponibilidad=True,
         volumen_ml=250
     )
     # 4. Prueba de encapsulación y validación de precio
     print("\n🔧 Prueba de modificación de precios:")
     plato1.cambiar_precio(6.50)  # Precio válido
     plato2.cambiar_precio(-0.25)   # Precio inválido (negativo)
     bebida1.cambiar_precio(0)      # Precio inválido (cero)
     # 5. Agregar todos los productos al restaurante
     print("\n➕ Agregando productos al sistema:")
     mi_restaurante.agregar_producto(plato1)
     mi_restaurante.agregar_producto(plato2)
     mi_restaurante.agregar_producto(bebida1)
     mi_restaurante.agregar_producto(bebida2)
     # 6. Mostrar toda la información (demuestra polimorfismo)
     mi_restaurante.mostrar_todos_productos()