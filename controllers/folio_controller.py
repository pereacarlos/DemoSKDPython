import asyncio

from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.Folios.SolicitudFolios import SolicitudFolios
from SimpleFacturaSDK.models.Folios.Foliorequest import FolioRequest
from SimpleFacturaSDK.models.Folios.AnularFoliosRequest import AnularFoliosRequest
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType

from controllers.base_controller import BaseController


class FolioController(BaseController):

    def consulta_folios_disponibles(self, rut_emisor: str, tipo_dte: int, ambiente: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = FolioRequest(
                    credenciales=Credenciales(rut_emisor=rut_emisor),
                    CodigoTipoDte=DTEType(tipo_dte),
                    Ambiente=ambiente
                )
                return await client.Folios.ConsultaFoliosDisponibles(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def solicitar_folios(self, rut_empresa: str, tipo_dte: int, ambiente: int, cantidad: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = SolicitudFolios(
                    RutEmpresa=rut_empresa,
                    TipoDTE=tipo_dte,
                    Ambiente=ambiente
                )
                return await client.Folios.SolicitarFolios(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def consultar_folios(self, rut_emisor: str, tipo_dte: int, ambiente: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = FolioRequest(
                    credenciales=Credenciales(rut_emisor=rut_emisor),
                    CodigoTipoDte=DTEType(tipo_dte),
                    Ambiente=ambiente
                )
                return await client.Folios.ConsultarFolios(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def folios_sin_uso(self, rut_emisor: str, tipo_dte: int, ambiente: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = FolioRequest(
                    credenciales=Credenciales(rut_emisor=rut_emisor),
                    CodigoTipoDte=DTEType(tipo_dte),
                    Ambiente=ambiente
                )
                return await client.Folios.Folios_Sin_Uso(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def anular_folio(self, rut_emisor: str, tipo_dte: int, ambiente: int,
                     folio_inicio: int, folio_termino: int, motivo: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = AnularFoliosRequest(
                    credenciales=Credenciales(rut_emisor=rut_emisor),
                    codigoTipoDte=DTEType(tipo_dte),
                    ambiente=ambiente,
                    folioInicio=folio_inicio,
                    folioTermino=folio_termino,
                    motivoAnulacion=motivo
                )
                return await client.Folios.anular_Folio(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"
