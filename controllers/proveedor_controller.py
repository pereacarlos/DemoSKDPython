import asyncio
from datetime import datetime

from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.SolicitudPdfDte import SolicitudPdfDte
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.models.GetFactura.ListadoRequest import ListaDteRequestEnt
from SimpleFacturaSDK.models.Proveedores.AcuseReciboExternoRequest import AcuseReciboExternoRequest
from SimpleFacturaSDK.models.Proveedores.ListaProveedorRequest import ListaProveedorRequest
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.enumeracion.ResponseType import ResponseType
from SimpleFacturaSDK.enumeracion.RejectionType import RejectionType
from SimpleFacturaSDK.enumeracion.ListaProveedorEnum import ListaProveedorEnum

from controllers.base_controller import BaseController


class ProveedorController(BaseController):

    def aceptar_rechazar_dte(self, rut_emisor: str, tipo_dte: int, folio: int,
                              ambiente: int, respuesta: int, tipo_rechazo: int, comentario: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                t_rechazo = RejectionType(tipo_rechazo) if tipo_rechazo > 0 else None
                solicitud = AcuseReciboExternoRequest(
                    credenciales=Credenciales(rut_emisor=rut_emisor),
                    dteReferenciadoExterno=DteReferenciadoExterno(
                        folio=folio,
                        codigoTipoDte=tipo_dte,
                        ambiente=ambiente
                    ),
                    respuesta=ResponseType(respuesta),
                    tipo_rechazo=t_rechazo,
                    comentario=comentario or None
                )
                return await client.Proveedores.Aceptar_RechazarDTE(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def listar_dte_recibidos(self, rut_emisor: str, tipo_dte: int, desde: str, hasta: str, ambiente: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = ListaDteRequestEnt(
                    Credenciales=Credenciales(rut_emisor=rut_emisor),
                    ambiente=AmbienteEnum(ambiente),
                    codigoTipoDte=DTEType(tipo_dte),
                    desde=datetime.strptime(desde, "%Y-%m-%d"),
                    hasta=datetime.strptime(hasta, "%Y-%m-%d"),
                )
                return await client.Proveedores.listarDteRecibidos(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def obtener_xml_recibido(self, rut_emisor: str, tipo_dte: int, folio: int, ambiente: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = SolicitudPdfDte(
                    credenciales=Credenciales(rut_emisor=rut_emisor),
                    dte_referenciado_externo=DteReferenciadoExterno(
                        folio=folio,
                        codigoTipoDte=tipo_dte,
                        ambiente=ambiente
                    )
                )
                return await client.Proveedores.obtenerXml(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def obtener_pdf_recibido(self, rut_emisor: str, tipo_dte: int, folio: int, ambiente: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = SolicitudPdfDte(
                    credenciales=Credenciales(rut_emisor=rut_emisor),
                    dte_referenciado_externo=DteReferenciadoExterno(
                        folio=folio,
                        codigoTipoDte=tipo_dte,
                        ambiente=ambiente
                    )
                )
                return await client.Proveedores.obtener_pdf(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def conciliar_recibidos(self, rut_emisor: str, mes: int, anio: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = Credenciales(rut_emisor=rut_emisor)
                return await client.Proveedores.ConciliarRecibidos(solicitud, mes, anio)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def obtener_trazas_recibidas(self, rut_emisor: str, tipo_dte: int, folio: int, ambiente: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = SolicitudPdfDte(
                    credenciales=Credenciales(rut_emisor=rut_emisor),
                    dte_referenciado_externo=DteReferenciadoExterno(
                        folio=folio,
                        codigoTipoDte=tipo_dte,
                        ambiente=ambiente
                    )
                )
                return await client.Proveedores.obtener_TrazasRecibidas(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def actualizar_lista_proveedor(self, rut_emisor: str, rut_proveedor: str, lista: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = ListaProveedorRequest(
                    Credenciales=Credenciales(rut_emisor=rut_emisor),
                    RutProveedor=rut_proveedor,
                    ListaProveedor=ListaProveedorEnum(lista)
                )
                return await client.Proveedores.actualizar_Lista_Proveedor(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"
