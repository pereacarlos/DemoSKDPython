import asyncio

from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.Clientes.NuevoReceptorExternoRequest import (
    NuevoReceptorExternoRequest,
    ReceptorExternoEnt,
)

from controllers.base_controller import BaseController


class ClientesController(BaseController):

    def crear_cliente(self, rut_emisor: str, rut: str, razon_social: str, giro: str,
                      dir_part: str, dir_fact: str, correo_par: str, correo_fact: str,
                      ciudad: str, comuna: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                nuevo = NuevoReceptorExternoRequest(
                    Rut=rut,
                    RazonSocial=razon_social,
                    Giro=giro,
                    DirPart=dir_part,
                    DirFact=dir_fact,
                    CorreoPar=correo_par,
                    CorreoFact=correo_fact,
                    Ciudad=ciudad,
                    Comuna=comuna
                )
                solicitud = {
                    "credenciales": Credenciales(rut_emisor=rut_emisor).to_dict(),
                    "clientes": [nuevo.to_dict()]
                }
                return await client.Clientes.CrearClientes(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def listar_clientes(self, rut_emisor: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = Credenciales(rut_emisor=rut_emisor)
                return await client.Clientes.ListarClientes(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def obtener_datos_cliente(self, rut_emisor: str, rut_cliente: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = Credenciales(rut_emisor=rut_emisor)
                return await client.Clientes.ObtenerDatosCliente(solicitud, rut_cliente)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def actualizar_cliente(self, rut_emisor: str, rut: str, razon_social: str, giro: str,
                           dir_part: str, dir_fact: str, correo_par: str, correo_fact: str,
                           ciudad: str, comuna: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                cliente = ReceptorExternoEnt(
                    rut=int(rut.split("-")[0]) if "-" in rut else int(rut),
                    dv=rut.split("-")[1] if "-" in rut else "",
                    rutFormateado=rut,
                    razonSocial=razon_social,
                    giro=giro,
                    dirPart=dir_part,
                    dirFact=dir_fact,
                    correoPar=correo_par,
                    correoFact=correo_fact,
                    ciudad=ciudad,
                    comuna=comuna,
                    activo=True
                )
                solicitud = {
                    "credenciales": Credenciales(rut_emisor=rut_emisor).to_dict(),
                    "clientes": [cliente.to_dict()]
                }
                return await client.Clientes.Actualizar_Clientes(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"
