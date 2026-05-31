import asyncio
from datetime import datetime

from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.CesionDteRequest import CesionDteRequest
from SimpleFacturaSDK.models.Cesiones.CesionTrazaRequest import CesionTrazaRequest
from SimpleFacturaSDK.models.Cesiones.ListaCesionRequest import ListaCesionRequest
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum

from controllers.base_controller import BaseController


class CesionController(BaseController):

    def ceder_factura(self, rut_empresa: str, folio: int, rut_cesionario: str,
                      rut_persona_autorizada: str, correo_deudor: str, otras_condiciones: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = CesionDteRequest(
                    CorreoDeudor=correo_deudor,
                    RutCesionario=rut_cesionario,
                    RutPersonaAutorizada=rut_persona_autorizada,
                    OtrasCondiciones=otras_condiciones,
                    Folio=folio,
                    RutEmpresa=rut_empresa
                )
                return await client.CesionService.ceder_Factura(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def obtener_trazas_cesion_emitida(self, rut_emisor: str, folio: int, ambiente: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = CesionTrazaRequest(
                    credenciales=Credenciales(rut_emisor=rut_emisor),
                    folio=folio,
                    ambiente=AmbienteEnum(ambiente)
                )
                return await client.CesionService.obtener_TrazasCesionEmitida(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def listado_cesiones_emitidas(self, rut_emisor: str, ambiente: int, desde: str, hasta: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = ListaCesionRequest(
                    credenciales=Credenciales(rut_emisor=rut_emisor),
                    ambiente=AmbienteEnum(ambiente),
                    desde=datetime.strptime(desde, "%Y-%m-%d"),
                    hasta=datetime.strptime(hasta, "%Y-%m-%d")
                )
                return await client.CesionService.listado_CesionesEmitidas(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"
