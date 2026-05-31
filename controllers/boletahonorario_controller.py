import asyncio
from datetime import datetime

from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.BoletaHonorarios.BHERequest import BHERequest
from SimpleFacturaSDK.models.BoletaHonorarios.ListaBHERequest import ListaBHERequest
from SimpleFacturaSDK.models.BoletaHonorarios.AnularBheEnt import AnularBheEnt
from SimpleFacturaSDK.models.BoletaHonorarios.BheObservacionEnt import BheObservacionEnt
from SimpleFacturaSDK.models.BoletaHonorarios.BHData import BHData, Receptor, Emisor, Detalle
from SimpleFacturaSDK.enumeracion.AnulacionBoletaHonorario import AnulacionBoletaHonorario
from SimpleFacturaSDK.enumeracion.ObservacionBoletaHonorario import ObservacionBoletaHonorario
from SimpleFacturaSDK.enumeracion.TipoRetencion import TipoRetencion

from controllers.base_controller import BaseController


class BoletaHonorarioController(BaseController):

    def obtener_pdf(self, rut_emisor: str, folio: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = BHERequest(
                    credenciales=Credenciales(rut_emisor=rut_emisor),
                    Folio=folio
                )
                return await client.BoletaHonorarioService.ObtenerPdf(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def listado_bhe_emitidos(self, rut_emisor: str, nombre_sucursal: str, desde: str, hasta: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                lista_req = ListaBHERequest(
                    credenciales=Credenciales(
                        rut_emisor=rut_emisor,
                        nombre_sucursal=nombre_sucursal
                    ),
                    Folio=None,
                    Desde=desde,
                    Hasta=hasta
                )
                return await client.BoletaHonorarioService.ListadoBHEEmitidos(lista_req)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def obtener_pdf_recibida(self, rut_emisor: str, folio: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = BHERequest(
                    credenciales=Credenciales(rut_emisor=rut_emisor),
                    Folio=folio
                )
                return await client.BoletaHonorarioService.ObtenerPdfBoletaRecibida(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def listado_bhe_recibidos(self, rut_emisor: str, nombre_sucursal: str, desde: str, hasta: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                lista_req = ListaBHERequest(
                    credenciales=Credenciales(
                        rut_emisor=rut_emisor,
                        nombre_sucursal=nombre_sucursal
                    ),
                    Folio=None,
                    Desde=desde,
                    Hasta=hasta
                )
                return await client.BoletaHonorarioService.ListadoBHERecibido(lista_req)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def emitir_bhe(self, rut_emisor: str, rut_receptor: str, nombre_receptor: str,
                   direccion_receptor: str, comuna_receptor: str, region_receptor: int,
                   nombre_servicio: str, valor_servicio: int, correo: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = BHData(
                    RutEmisor=rut_emisor,
                    Correo=correo,
                    Retencion=TipoRetencion.Receptor,
                    FechaEmision=datetime.now().strftime("%d-%m-%Y"),
                    Receptor=Receptor(
                        Rut=rut_receptor,
                        Nombre=nombre_receptor,
                        Direccion=direccion_receptor,
                        Comuna=comuna_receptor,
                        Region=region_receptor
                    ),
                    Emisor=Emisor(Rut=rut_emisor),
                    Detalles=[Detalle(Nombre=nombre_servicio, Valor=valor_servicio)]
                )
                return await client.BoletaHonorarioService.EmitirBHE(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def emitir_bhe_terceros(self, rut_emisor: str, rut_receptor: str, nombre_receptor: str,
                            direccion_receptor: str, comuna_receptor: str, region_receptor: int,
                            nombre_servicio: str, valor_servicio: int, correo: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = BHData(
                    RutEmisor=rut_emisor,
                    Correo=correo,
                    Retencion=TipoRetencion.Receptor,
                    FechaEmision=datetime.now().strftime("%d-%m-%Y"),
                    Receptor=Receptor(
                        Rut=rut_receptor,
                        Nombre=nombre_receptor,
                        Direccion=direccion_receptor,
                        Comuna=comuna_receptor,
                        Region=region_receptor
                    ),
                    Emisor=Emisor(Rut=rut_emisor),
                    Detalles=[Detalle(Nombre=nombre_servicio, Valor=valor_servicio)]
                )
                return await client.BoletaHonorarioService.EmitirBHETerceros(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def anular_bhe(self, rut_empresa: str, folio: int, motivo: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = AnularBheEnt(
                    RutEmpresa=rut_empresa,
                    Folio=folio,
                    Motivo=AnulacionBoletaHonorario(motivo)
                )
                return await client.BoletaHonorarioService.AnularBHE(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def observar_bhe(self, rut_empresa: str, rut_contribuyente: str, folio: int, observacion: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = BheObservacionEnt(
                    RutEmpresa=rut_empresa,
                    rutContribuyente=rut_contribuyente,
                    Folio=folio,
                    Observacion=ObservacionBoletaHonorario(observacion)
                )
                return await client.BoletaHonorarioService.ObservarBHE(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def conciliar_bhe_emitidas(self, rut_emisor: str, mes: int, anio: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                credenciales = Credenciales(rut_emisor=rut_emisor)
                return await client.BoletaHonorarioService.ConciliarBHEEmitidas(credenciales, mes, anio)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def conciliar_bhe_recibidas(self, rut_emisor: str, mes: int, anio: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                credenciales = Credenciales(rut_emisor=rut_emisor)
                return await client.BoletaHonorarioService.ConciliarBHERecibidas(credenciales, mes, anio)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"
