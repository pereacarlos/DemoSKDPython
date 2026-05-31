import asyncio
from datetime import datetime

from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.models.Payku.PaykuRequests import (
    PaykuTransaccionesRequest,
    PaykuToggleRequest,
    PaykuReenviarLinkRequest,
    MarcarPagadoOPendienteRequest,
)

from controllers.base_controller import BaseController


class PaykuController(BaseController):

    def transacciones(self, rut_emisor: str, desde: str, hasta: str) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = PaykuTransaccionesRequest(
                    credenciales=Credenciales(rut_emisor=rut_emisor),
                    desde=datetime.strptime(desde, "%Y-%m-%d"),
                    hasta=datetime.strptime(hasta, "%Y-%m-%d")
                )
                return await client.PaykuService.transacciones(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def activar_desactivar(self, rut_emisor: str, activo: bool) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = PaykuToggleRequest(
                    credenciales=Credenciales(rut_emisor=rut_emisor),
                    activo=activo
                )
                return await client.PaykuService.activar_desactivar(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def generar_url(self, rut_emisor: str, tipo_dte: int, folio: int, ambiente: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = PaykuReenviarLinkRequest(
                    credenciales=Credenciales(rut_emisor=rut_emisor),
                    dte=DteReferenciadoExterno(
                        folio=folio,
                        codigoTipoDte=tipo_dte,
                        ambiente=ambiente
                    )
                )
                return await client.PaykuService.generar_url(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def reenviar_link_qr(self, rut_emisor: str, tipo_dte: int, folio: int, ambiente: int) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = PaykuReenviarLinkRequest(
                    credenciales=Credenciales(rut_emisor=rut_emisor),
                    dte=DteReferenciadoExterno(
                        folio=folio,
                        codigoTipoDte=tipo_dte,
                        ambiente=ambiente
                    )
                )
                return await client.PaykuService.reenviar_link_qr(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"

    def marcar_pagado_o_pendiente(self, rut_emisor: str, tipo_dte: int, folio: int,
                                   ambiente: int, pagado: bool) -> str:
        async def _exec():
            async with ClientSimpleFactura(self.username, self.password) as client:
                solicitud = MarcarPagadoOPendienteRequest(
                    credenciales=Credenciales(rut_emisor=rut_emisor),
                    dteReferenciadoExterno=DteReferenciadoExterno(
                        folio=folio,
                        codigoTipoDte=tipo_dte,
                        ambiente=ambiente
                    ),
                    pagado=pagado
                )
                return await client.PaykuService.marcar_dte_pagado_o_pendiente(solicitud)
        try:
            return self.format_response(asyncio.run(_exec()))
        except Exception as e:
            return f"✗ Error inesperado: {e}"
