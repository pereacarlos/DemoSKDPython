import asyncio
from datetime import datetime

from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.Partner.WizardEmisorRequest import WizardEmisorRequest, EmisorReq, SucursalReq
from SimpleFacturaSDK.models.Partner.PartnerDteResumenRequest import PartnerDteResumenRequest
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.enumeracion.PlanUsuario import PlanUsuarioEnum

from controllers.base_controller import BaseController


class PartnerController(BaseController):

    def enrolamiento_empresa(self, rut_empresa: str, razon_social: str, rut_rep_legal: str,
                              giro: str, email: str, direccion: str, ciudad: str, comuna: str,
                              telefono: str, unidad_sii: str, ambiente: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = WizardEmisorRequest(
                    Emisor=EmisorReq(
                        RutEmpresa=rut_empresa,
                        RazonSocial=razon_social,
                        RutRepresentanteLegal=rut_rep_legal,
                        Giro=giro,
                        Email=email,
                        DireccionFacturacion=direccion,
                        Ciudad=ciudad,
                        Comuna=comuna,
                        Telefono=telefono,
                        FechaResolucion=datetime(2019, 2, 11),
                        NumeroResolucion=0,
                        Ambiente=AmbienteEnum(ambiente),
                        UnidadSii=unidad_sii
                    ),
                    Sucursal=SucursalReq(Nombre="Casa Matriz", Direccion=direccion),
                    ActividadesEconomicas=[620010],
                    Plan=PlanUsuarioEnum.Independiente
                )
                return await client.PartnerService.enrolamiento_empresa(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def obtener_actividades_economicas(self) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                return await client.PartnerService.obtener_actividades_economicas()
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def upload_logo(self, rut_emisor: str, path_logo: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                credenciales = Credenciales(rut_emisor=rut_emisor)
                return await client.PartnerService.upload_logo(credenciales, path_logo)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def obtener_resumen_dtes(self, rut_emisor: str, anio: int, mes: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = PartnerDteResumenRequest(
                    Credenciales=Credenciales(rut_emisor=rut_emisor),
                    Anio=anio,
                    Mes=mes
                )
                return await client.PartnerService.obtener_resumen_dtes(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"
