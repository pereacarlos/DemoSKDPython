import asyncio
import json
from datetime import datetime
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.SolicitudPdfDte import SolicitudPdfDte
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.models.GetFactura.ListadoRequest import ListaDteRequestEnt
from SimpleFacturaSDK.models.GetFactura.ReenvioSiiRequest import ReenvioSiiRequest
from SimpleFacturaSDK.models.GetFactura.AnularGuiaRequest import AnularGuiaRequest
from SimpleFacturaSDK.models.GetFactura.EnvioMailRequest import EnvioMailRequest, DteClass, MailClass
from SimpleFacturaSDK.models.GetFactura.RequestDTE import RequestDTE
from SimpleFacturaSDK.models.GetFactura.CesionDteRequest import CesionDteRequest
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum

from controllers.base_controller import BaseController


class FacturacionController(BaseController):

    def obtener_pdf(self, rut_emisor: str, sucursal: str, tipo_dte: int, folio: int, ambiente: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = SolicitudPdfDte(
                    credenciales=Credenciales(rut_emisor=rut_emisor, nombre_sucursal=sucursal),
                    dte_referenciado_externo=DteReferenciadoExterno(
                        folio=folio,
                        codigoTipoDte=tipo_dte,
                        ambiente=ambiente
                    )
                )
                return await client.Facturacion.obtener_pdf(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def obtener_timbre(self, rut_emisor: str, sucursal: str, tipo_dte: int, folio: int, ambiente: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = SolicitudPdfDte(
                    credenciales=Credenciales(rut_emisor=rut_emisor, nombre_sucursal=sucursal),
                    dte_referenciado_externo=DteReferenciadoExterno(
                        folio=folio,
                        codigoTipoDte=tipo_dte,
                        ambiente=ambiente
                    )
                )
                return await client.Facturacion.obtener_timbre(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def obtener_xml(self, rut_emisor: str, sucursal: str, tipo_dte: int, folio: int, ambiente: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = SolicitudPdfDte(
                    credenciales=Credenciales(rut_emisor=rut_emisor, nombre_sucursal=sucursal),
                    dte_referenciado_externo=DteReferenciadoExterno(
                        folio=folio,
                        codigoTipoDte=tipo_dte,
                        ambiente=ambiente
                    )
                )
                return await client.Facturacion.obtener_xml(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def obtener_dte(self, rut_emisor: str, sucursal: str, tipo_dte: int, folio: int, ambiente: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = SolicitudPdfDte(
                    credenciales=Credenciales(rut_emisor=rut_emisor, nombre_sucursal=sucursal),
                    dte_referenciado_externo=DteReferenciadoExterno(
                        folio=folio,
                        codigoTipoDte=tipo_dte,
                        ambiente=ambiente
                    )
                )
                return await client.Facturacion.obtener_dte(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def obtener_sobre_xml(self, rut_emisor: str, sucursal: str, tipo_dte: int, folio: int, ambiente: int, sobre: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = SolicitudPdfDte(
                    credenciales=Credenciales(rut_emisor=rut_emisor, nombre_sucursal=sucursal),
                    dte_referenciado_externo=DteReferenciadoExterno(
                        folio=folio,
                        codigoTipoDte=tipo_dte,
                        ambiente=ambiente
                    )
                )
                return await client.Facturacion.obtener_sobreXml(solicitud, sobre)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def facturacion_individual_v2_dte(self, sucursal: str, request_json: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                data = json.loads(request_json)
                solicitud = RequestDTE(**data) if data else RequestDTE()
                return await client.Facturacion.facturacion_individualV2_Dte(solicitud, sucursal)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def facturacion_individual_v2_boletas(self, sucursal: str, request_json: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                data = json.loads(request_json)
                solicitud = RequestDTE(**data) if data else RequestDTE()
                return await client.Facturacion.facturacion_individualV2_Boletas(solicitud, sucursal)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def facturacion_individual_v2_exportacion(self, sucursal: str, request_json: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                data = json.loads(request_json)
                solicitud = RequestDTE(**data) if data else RequestDTE()
                return await client.Facturacion.facturacion_individualV2_Exportacion(solicitud, sucursal)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def facturacion_masiva(self, rut_emisor: str, path_csv: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                credenciales = Credenciales(rut_emisor=rut_emisor)
                return await client.Facturacion.facturacion_Masiva(credenciales, path_csv)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def emision_nc_nd_v2(self, sucursal: str, motivo: int, request_json: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                data = json.loads(request_json)
                solicitud = RequestDTE(**data) if data else RequestDTE()
                return await client.Facturacion.EmisionNC_ND_V2(solicitud, sucursal, motivo)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def listado_dte_emitidos(self, rut_emisor: str, sucursal: str, tipo_dte: int, desde: str, hasta: str, ambiente: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = ListaDteRequestEnt(
                    Credenciales=Credenciales(rut_emisor=rut_emisor, nombre_sucursal=sucursal),
                    ambiente=AmbienteEnum(ambiente),
                    codigoTipoDte=DTEType(tipo_dte),
                    desde=datetime.strptime(desde, "%Y-%m-%d"),
                    hasta=datetime.strptime(hasta, "%Y-%m-%d"),
                )
                return await client.Facturacion.listadoDteEmitidos(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def enviar_correo(self, rut_empresa: str, folio: int, tipo_dte: int, email_to: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = EnvioMailRequest(
                    RutEmpresa=rut_empresa,
                    Dte=DteClass(folio=folio, tipoDTE=tipo_dte),
                    Mail=MailClass(to=[email_to], ccos=[], ccs=[]),
                    Xml=False,
                    Pdf=True,
                    Comments=None
                )
                return await client.Facturacion.enviarCorreo(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def consolidado_ventas(self, rut_emisor: str, sucursal: str, desde: str, hasta: str, ambiente: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = ListaDteRequestEnt(
                    Credenciales=Credenciales(rut_emisor=rut_emisor, nombre_sucursal=sucursal),
                    ambiente=AmbienteEnum(ambiente),
                    desde=datetime.strptime(desde, "%Y-%m-%d"),
                    hasta=datetime.strptime(hasta, "%Y-%m-%d"),
                )
                return await client.Facturacion.consolidadoVentas(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def conciliar_emitidos(self, rut_emisor: str, sucursal: str, mes: int, anio: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = Credenciales(rut_emisor=rut_emisor, nombre_sucursal=sucursal)
                return await client.Facturacion.ConciliarEmitidos(solicitud, mes, anio)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def obtener_trazas(self, rut_emisor: str, sucursal: str, tipo_dte: int, folio: int, ambiente: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = SolicitudPdfDte(
                    credenciales=Credenciales(rut_emisor=rut_emisor, nombre_sucursal=sucursal),
                    dte_referenciado_externo=DteReferenciadoExterno(
                        folio=folio,
                        codigoTipoDte=tipo_dte,
                        ambiente=ambiente
                    )
                )
                return await client.Facturacion.obtener_Trazas(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def preview_dte(self, sucursal: str, request_json: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                data = json.loads(request_json)
                solicitud = RequestDTE(**data) if data else RequestDTE()
                return await client.Facturacion.preview_Dte(solicitud, sucursal)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def reenvio_sii(self, rut_emisor: str, sucursal: str, tipo_dte: int, folio: int, ambiente: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = ReenvioSiiRequest(
                    Credenciales=Credenciales(rut_emisor=rut_emisor, nombre_sucursal=sucursal),
                    ambiente=AmbienteEnum(ambiente),
                    folio=float(folio),
                    codigoTipoDte=DTEType(tipo_dte)
                )
                return await client.Facturacion.reenvio_Sii(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def anular_guia(self, rut_empresa: str, folio: int, ambiente: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = AnularGuiaRequest(
                    RutEmpresa=rut_empresa,
                    Folio=folio,
                    Ambiente=ambiente
                )
                return await client.Facturacion.anular_guia(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def obtener_correo_intercambio(self, rut_emisor: str, sucursal: str, rut_header: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = Credenciales(rut_emisor=rut_emisor, nombre_sucursal=sucursal)
                return await client.Facturacion.obtener_correo_intercambio(solicitud, rut_header)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"
