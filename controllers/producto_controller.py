import asyncio

from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.Productos.NuevoProductoExternoRequest import NuevoProductoExternoRequest

from controllers.base_controller import BaseController


class ProductoController(BaseController):

    def crear_producto(self, rut_emisor: str, nombre: str, codigo_barra: str,
                       unidad_medida: str, precio: float, exento: bool) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                nuevo = NuevoProductoExternoRequest(
                    nombre=nombre,
                    codigoBarra=codigo_barra,
                    unidadMedida=unidad_medida,
                    precio=precio,
                    exento=exento,
                    tieneImpuestos=False,
                    impuestos=[]
                )
                solicitud = {
                    "credenciales": Credenciales(rut_emisor=rut_emisor).to_dict(),
                    "producto": nuevo.to_dict()
                }
                return await client.Productos.CrearProducto(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def listar_productos(self, rut_emisor: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = Credenciales(rut_emisor=rut_emisor)
                return await client.Productos.listarProductos(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"
