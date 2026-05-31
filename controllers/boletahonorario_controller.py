from SimpleFacturaSDK.services.BoletaHonorarioService import BoletaHonorarioService
from SimpleFacturaSDK.models.BoletaHonorarios.BHERequest import BHERequest
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.BoletaHonorarios.ListaBHERequest import ListaBHERequest
import os
from dotenv import load_dotenv
load_dotenv()

class BoletaHonorarioController:
    def setUp(self):
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")
     
        
        self.client_api = ClientSimpleFactura(username, password)
        self.service = self.client_api.BoletaHonorarioService()

    def obtener_pdf(self):
        try:
            solicitud = BHERequest(
                solicitud= BHERequest(
                    credenciales=Credenciales(
                        rut_emisor="78181331-1"
                    ),
                    Folio=15
                )
            )
            response = self.service.ObtenerPdf(solicitud)
            if response.status == 200:
                with open("boleta.pdf", "wb") as file:
                    file.write(response.data)
                print("PDF guardado con éxito.")
            else:
                print(f"Error: {response.message}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def listado_emitidos(self):
        try:
            fecha_desde = "2026-05-01"
            fecha_hasta = "2026-05-31"
            solicitud = BHERequest(
                solicitud= ListaBHERequest(
                    credenciales=Credenciales(
                        rut_emisor="78181331-1",
                        nombre_sucursal="Casa Matriz"
                    ),
                    Folio=None,
                    Desde=fecha_desde,
                    Hasta=fecha_hasta
                )
            )
            response = self.service.ListadoBHEEmitidos(solicitud)
            if response.status == 200:
                print("Listado obtenido:", response.data)
            else:
                print(f"Error: {response.message}")
        except Exception as e:
            print(f"Error inesperado: {e}")
