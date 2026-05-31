import asyncio

from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales

from controllers.base_controller import BaseController


class ConfiguracionController(BaseController):

    def datos_empresa(self, rut_emisor: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = Credenciales(rut_emisor=rut_emisor)
                return await client.ConfiguracionService.datos_empresa(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def subir_certificado_digital(self, rut_emisor: str, path_certificado: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                credenciales = Credenciales(rut_emisor=rut_emisor)
                return await client.ConfiguracionService.subir_Certificado_Digital(
                    credenciales, path_certificado
                )
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"
