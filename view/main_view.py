import tkinter as tk
from tkinter import ttk
import threading
import json

from controllers.boletahonorario_controller import BoletaHonorarioController
from controllers.facturacion_controller import FacturacionController
from controllers.clientes_controller import ClientesController
from controllers.producto_controller import ProductoController
from controllers.folio_controller import FolioController
from controllers.configuracion_controller import ConfiguracionController
from controllers.sucursal_controller import SucursalController
from controllers.proveedor_controller import ProveedorController
from controllers.usuario_controller import UsuarioController
from controllers.cesion_controller import CesionController
from controllers.partner_controller import PartnerController
from controllers.payku_controller import PaykuController

RUT_EMISOR   = "78181331-1"
RUT_RECEPTOR = "17096073-4"
SUCURSAL     = "Casa Matriz"
AMBIENTE     = "0"
FOLIO        = "1"
TIPO_DTE     = "33"
DESDE        = "2025-01-01"
HASTA        = "2025-01-31"
MES          = "1"
ANIO         = "2025"
EMAIL        = "receptor@empresa.cl"
RUT_EMPRESA  = "78181331-1"

INVOICE_JSON = json.dumps({
    "Documento": {
        "Encabezado": {
            "IdDoc": {
                "TipoDTE": 33,
                "FchEmis": "2025-01-15",
                "FchVenc": "2025-02-15",
                "FmaPago": 1
            },
            "Emisor": {
                "RUTEmisor": "78181331-1",
                "RznSoc": "Mi Empresa SpA",
                "GiroEmis": "Servicios de Tecnología",
                "Telefono": ["912345678"],
                "CorreoEmisor": "contacto@miempresa.cl",
                "Acteco": [620010],
                "DirOrigen": "Av. Providencia 1234",
                "CmnaOrigen": "Providencia",
                "CiudadOrigen": "Santiago"
            },
            "Receptor": {
                "RUTRecep": "17096073-4",
                "RznSocRecep": "Juan Pérez",
                "CorreoRecep": "juan@ejemplo.cl",
                "DirRecep": "Calle Los Álamos 567",
                "CmnaRecep": "Las Condes",
                "CiudadRecep": "Santiago",
                "GiroRecep": "Servicios"
            },
            "Totales": {
                "MntNeto": 100000,
                "TasaIVA": "19",
                "IVA": 19000,
                "MntTotal": 119000
            }
        },
        "Detalle": [
            {
                "NroLinDet": 1,
                "NmbItem": "Servicio de Consultoría",
                "QtyItem": 1.0,
                "UnmdItem": "Srv",
                "PrcItem": 100000.0,
                "MontoItem": 100000
            }
        ]
    }
}, indent=2, ensure_ascii=False)

NC_ND_JSON = json.dumps({
    "Documento": {
        "Encabezado": {
            "IdDoc": {
                "TipoDTE": 61,
                "FchEmis": "2025-01-20",
                "FmaPago": 1
            },
            "Emisor": {
                "RUTEmisor": "78181331-1",
                "RznSoc": "Mi Empresa SpA",
                "GiroEmis": "Servicios de Tecnología",
                "Telefono": ["912345678"],
                "CorreoEmisor": "contacto@miempresa.cl",
                "Acteco": [620010],
                "DirOrigen": "Av. Providencia 1234",
                "CmnaOrigen": "Providencia",
                "CiudadOrigen": "Santiago"
            },
            "Receptor": {
                "RUTRecep": "17096073-4",
                "RznSocRecep": "Juan Pérez",
                "CorreoRecep": "juan@ejemplo.cl",
                "DirRecep": "Calle Los Álamos 567",
                "CmnaRecep": "Las Condes",
                "CiudadRecep": "Santiago",
                "GiroRecep": "Servicios"
            },
            "Totales": {
                "MntNeto": 50000,
                "TasaIVA": "19",
                "IVA": 9500,
                "MntTotal": 59500
            }
        },
        "Detalle": [
            {
                "NroLinDet": 1,
                "NmbItem": "Devolución Parcial Servicio",
                "QtyItem": 1.0,
                "UnmdItem": "Srv",
                "PrcItem": 50000.0,
                "MontoItem": 50000
            }
        ],
        "Referencia": [
            {
                "NroLinRef": 1,
                "TpoDocRef": "33",
                "FolioRef": "1",
                "CodRef": 1,
                "RazonRef": "Corrección de monto",
                "FchRef": "2025-01-15"
            }
        ]
    }
}, indent=2, ensure_ascii=False)


def _f(label, key, default, ftype="entry", options=None):
    return {"label": label, "key": key, "default": default, "type": ftype, "options": options or []}


REGISTRY = [
    ("Boleta Honorario", [
        ("Obtener PDF (Emitida)", [
            _f("RUT Emisor",  "rut_emisor", RUT_EMISOR),
            _f("Folio",       "folio",      FOLIO),
        ], lambda f, u, p: BoletaHonorarioController(u, p).obtener_pdf(
            f["rut_emisor"], int(f["folio"])
        )),

        ("Listado BHE Emitidas", [
            _f("RUT Emisor",      "rut_emisor",     RUT_EMISOR),
            _f("Nombre Sucursal", "nombre_sucursal", SUCURSAL),
            _f("Desde (YYYY-MM-DD)", "desde",        DESDE),
            _f("Hasta (YYYY-MM-DD)", "hasta",        HASTA),
        ], lambda f, u, p: BoletaHonorarioController(u, p).listado_bhe_emitidos(
            f["rut_emisor"], f["nombre_sucursal"], f["desde"], f["hasta"]
        )),

        ("Obtener PDF (Recibida)", [
            _f("RUT Emisor", "rut_emisor", RUT_EMISOR),
            _f("Folio",      "folio",      FOLIO),
        ], lambda f, u, p: BoletaHonorarioController(u, p).obtener_pdf_recibida(
            f["rut_emisor"], int(f["folio"])
        )),

        ("Listado BHE Recibidas", [
            _f("RUT Emisor",         "rut_emisor",     RUT_EMISOR),
            _f("Nombre Sucursal",    "nombre_sucursal", SUCURSAL),
            _f("Desde (YYYY-MM-DD)", "desde",           DESDE),
            _f("Hasta (YYYY-MM-DD)", "hasta",           HASTA),
        ], lambda f, u, p: BoletaHonorarioController(u, p).listado_bhe_recibidos(
            f["rut_emisor"], f["nombre_sucursal"], f["desde"], f["hasta"]
        )),

        ("Emitir BHE", [
            _f("RUT Emisor",         "rut_emisor",       RUT_EMISOR),
            _f("RUT Receptor",       "rut_receptor",     "12345678-9"),
            _f("Nombre Receptor",    "nombre_receptor",  "Pedro González"),
            _f("Dirección Receptor", "dir_receptor",     "Av. Las Heras 100"),
            _f("Comuna Receptor",    "comuna_receptor",  "Santiago"),
            _f("Región (número)",    "region_receptor",  "13"),
            _f("Nombre Servicio",    "nombre_servicio",  "Asesoría Contable"),
            _f("Valor Servicio",     "valor_servicio",   "150000"),
            _f("Correo",             "correo",           EMAIL),
        ], lambda f, u, p: BoletaHonorarioController(u, p).emitir_bhe(
            f["rut_emisor"], f["rut_receptor"], f["nombre_receptor"],
            f["dir_receptor"], f["comuna_receptor"], int(f["region_receptor"]),
            f["nombre_servicio"], int(f["valor_servicio"]), f["correo"]
        )),

        ("Emitir BHE Terceros", [
            _f("RUT Emisor",         "rut_emisor",       RUT_EMISOR),
            _f("RUT Receptor",       "rut_receptor",     "12345678-9"),
            _f("Nombre Receptor",    "nombre_receptor",  "Pedro González"),
            _f("Dirección Receptor", "dir_receptor",     "Av. Las Heras 100"),
            _f("Comuna Receptor",    "comuna_receptor",  "Santiago"),
            _f("Región (número)",    "region_receptor",  "13"),
            _f("Nombre Servicio",    "nombre_servicio",  "Asesoría Contable"),
            _f("Valor Servicio",     "valor_servicio",   "150000"),
            _f("Correo",             "correo",           EMAIL),
        ], lambda f, u, p: BoletaHonorarioController(u, p).emitir_bhe_terceros(
            f["rut_emisor"], f["rut_receptor"], f["nombre_receptor"],
            f["dir_receptor"], f["comuna_receptor"], int(f["region_receptor"]),
            f["nombre_servicio"], int(f["valor_servicio"]), f["correo"]
        )),

        ("Anular BHE", [
            _f("RUT Empresa", "rut_empresa", RUT_EMPRESA),
            _f("Folio",       "folio",       FOLIO),
            _f("Motivo (1=ServicioNoPagado, 2=NoEfectuado, 3=Error)", "motivo", "3",
               "combo", ["1 - Servicio No Pagado", "2 - Servicio No Efectuado", "3 - Error Digitación"]),
        ], lambda f, u, p: BoletaHonorarioController(u, p).anular_bhe(
            f["rut_empresa"], int(f["folio"]),
            int(f["motivo"].split(" ")[0]) if " " in f["motivo"] else int(f["motivo"])
        )),

        ("Observar BHE", [
            _f("RUT Empresa",       "rut_empresa",        RUT_EMPRESA),
            _f("RUT Contribuyente", "rut_contribuyente",   RUT_RECEPTOR),
            _f("Folio",             "folio",               FOLIO),
            _f("Observación (1=NoReconoceRelación, 2=NoReconoceEmisor)", "observacion", "1",
               "combo", ["1 - No reconoce relación", "2 - No reconoce emisor"]),
        ], lambda f, u, p: BoletaHonorarioController(u, p).observar_bhe(
            f["rut_empresa"], f["rut_contribuyente"], int(f["folio"]),
            int(f["observacion"].split(" ")[0]) if " " in f["observacion"] else int(f["observacion"])
        )),

        ("Conciliar BHE Emitidas", [
            _f("RUT Emisor", "rut_emisor", RUT_EMISOR),
            _f("Mes",        "mes",        MES),
            _f("Año",        "anio",       ANIO),
        ], lambda f, u, p: BoletaHonorarioController(u, p).conciliar_bhe_emitidas(
            f["rut_emisor"], int(f["mes"]), int(f["anio"])
        )),

        ("Conciliar BHE Recibidas", [
            _f("RUT Emisor", "rut_emisor", RUT_EMISOR),
            _f("Mes",        "mes",        MES),
            _f("Año",        "anio",       ANIO),
        ], lambda f, u, p: BoletaHonorarioController(u, p).conciliar_bhe_recibidas(
            f["rut_emisor"], int(f["mes"]), int(f["anio"])
        )),
    ]),

    # ── Facturación ───────────────────────────────────────────────────────────
    ("Facturación", [
        ("Obtener PDF", [
            _f("RUT Emisor",    "rut_emisor", RUT_EMISOR),
            _f("Nombre Sucursal","sucursal",  SUCURSAL),
            _f("Tipo DTE",      "tipo_dte",   TIPO_DTE),
            _f("Folio",         "folio",      FOLIO),
            _f("Ambiente (0=Cert, 1=Prod)", "ambiente", AMBIENTE),
        ], lambda f, u, p: FacturacionController(u, p).obtener_pdf(
            f["rut_emisor"], f["sucursal"], int(f["tipo_dte"]), int(f["folio"]), int(f["ambiente"])
        )),

        ("Obtener Timbre", [
            _f("RUT Emisor",    "rut_emisor", RUT_EMISOR),
            _f("Nombre Sucursal","sucursal",  SUCURSAL),
            _f("Tipo DTE",      "tipo_dte",   TIPO_DTE),
            _f("Folio",         "folio",      FOLIO),
            _f("Ambiente",      "ambiente",   AMBIENTE),
        ], lambda f, u, p: FacturacionController(u, p).obtener_timbre(
            f["rut_emisor"], f["sucursal"], int(f["tipo_dte"]), int(f["folio"]), int(f["ambiente"])
        )),

        ("Obtener XML", [
            _f("RUT Emisor",    "rut_emisor", RUT_EMISOR),
            _f("Nombre Sucursal","sucursal",  SUCURSAL),
            _f("Tipo DTE",      "tipo_dte",   TIPO_DTE),
            _f("Folio",         "folio",      FOLIO),
            _f("Ambiente",      "ambiente",   AMBIENTE),
        ], lambda f, u, p: FacturacionController(u, p).obtener_xml(
            f["rut_emisor"], f["sucursal"], int(f["tipo_dte"]), int(f["folio"]), int(f["ambiente"])
        )),

        ("Obtener DTE", [
            _f("RUT Emisor",    "rut_emisor", RUT_EMISOR),
            _f("Nombre Sucursal","sucursal",  SUCURSAL),
            _f("Tipo DTE",      "tipo_dte",   TIPO_DTE),
            _f("Folio",         "folio",      FOLIO),
            _f("Ambiente",      "ambiente",   AMBIENTE),
        ], lambda f, u, p: FacturacionController(u, p).obtener_dte(
            f["rut_emisor"], f["sucursal"], int(f["tipo_dte"]), int(f["folio"]), int(f["ambiente"])
        )),

        ("Obtener Sobre XML", [
            _f("RUT Emisor",    "rut_emisor", RUT_EMISOR),
            _f("Nombre Sucursal","sucursal",  SUCURSAL),
            _f("Tipo DTE",      "tipo_dte",   TIPO_DTE),
            _f("Folio",         "folio",      FOLIO),
            _f("Ambiente",      "ambiente",   AMBIENTE),
            _f("Valor Sobre",   "sobre",      "1"),
        ], lambda f, u, p: FacturacionController(u, p).obtener_sobre_xml(
            f["rut_emisor"], f["sucursal"], int(f["tipo_dte"]), int(f["folio"]), int(f["ambiente"]), int(f["sobre"])
        )),

        ("Facturación Individual V2 - DTE", [
            _f("Sucursal",      "sucursal",     SUCURSAL),
            _f("Request JSON",  "request_json", INVOICE_JSON, "json"),
        ], lambda f, u, p: FacturacionController(u, p).facturacion_individual_v2_dte(
            f["sucursal"], f["request_json"]
        )),

        ("Facturación Individual V2 - Boletas", [
            _f("Sucursal",     "sucursal",     SUCURSAL),
            _f("Request JSON", "request_json", INVOICE_JSON, "json"),
        ], lambda f, u, p: FacturacionController(u, p).facturacion_individual_v2_boletas(
            f["sucursal"], f["request_json"]
        )),

        ("Facturación Individual V2 - Exportación", [
            _f("Sucursal",     "sucursal",     SUCURSAL),
            _f("Request JSON", "request_json", INVOICE_JSON, "json"),
        ], lambda f, u, p: FacturacionController(u, p).facturacion_individual_v2_exportacion(
            f["sucursal"], f["request_json"]
        )),

        ("Facturación Masiva (CSV)", [
            _f("RUT Emisor", "rut_emisor", RUT_EMISOR),
            _f("Ruta CSV",   "path_csv",   "C:/facturas/masivo.csv"),
        ], lambda f, u, p: FacturacionController(u, p).facturacion_masiva(
            f["rut_emisor"], f["path_csv"]
        )),

        ("Emisión NC / ND V2", [
            _f("Sucursal",     "sucursal",     SUCURSAL),
            _f("Motivo (1=Anula, 2=Corrige texto, 3=Corrige montos)", "motivo", "1",
               "combo", ["1 - Anula doc. referencia", "2 - Corrige texto", "3 - Corrige montos"]),
            _f("Request JSON", "request_json", NC_ND_JSON, "json"),
        ], lambda f, u, p: FacturacionController(u, p).emision_nc_nd_v2(
            f["sucursal"],
            int(f["motivo"].split(" ")[0]) if " " in f["motivo"] else int(f["motivo"]),
            f["request_json"]
        )),

        ("Listado DTE Emitidos", [
            _f("RUT Emisor",         "rut_emisor", RUT_EMISOR),
            _f("Nombre Sucursal",    "sucursal",   SUCURSAL),
            _f("Tipo DTE",           "tipo_dte",   TIPO_DTE),
            _f("Desde (YYYY-MM-DD)", "desde",      DESDE),
            _f("Hasta (YYYY-MM-DD)", "hasta",      HASTA),
            _f("Ambiente",           "ambiente",   AMBIENTE),
        ], lambda f, u, p: FacturacionController(u, p).listado_dte_emitidos(
            f["rut_emisor"], f["sucursal"], int(f["tipo_dte"]), f["desde"], f["hasta"], int(f["ambiente"])
        )),

        ("Enviar Correo", [
            _f("RUT Empresa", "rut_empresa", RUT_EMPRESA),
            _f("Folio",       "folio",       FOLIO),
            _f("Tipo DTE",    "tipo_dte",    TIPO_DTE),
            _f("Email Destino","email_to",   EMAIL),
        ], lambda f, u, p: FacturacionController(u, p).enviar_correo(
            f["rut_empresa"], int(f["folio"]), int(f["tipo_dte"]), f["email_to"]
        )),

        ("Consolidado Ventas", [
            _f("RUT Emisor",         "rut_emisor", RUT_EMISOR),
            _f("Nombre Sucursal",    "sucursal",   SUCURSAL),
            _f("Desde (YYYY-MM-DD)", "desde",      DESDE),
            _f("Hasta (YYYY-MM-DD)", "hasta",      HASTA),
            _f("Ambiente",           "ambiente",   AMBIENTE),
        ], lambda f, u, p: FacturacionController(u, p).consolidado_ventas(
            f["rut_emisor"], f["sucursal"], f["desde"], f["hasta"], int(f["ambiente"])
        )),

        ("Conciliar Emitidos", [
            _f("RUT Emisor",      "rut_emisor", RUT_EMISOR),
            _f("Nombre Sucursal", "sucursal",   SUCURSAL),
            _f("Mes",             "mes",        MES),
            _f("Año",             "anio",       ANIO),
        ], lambda f, u, p: FacturacionController(u, p).conciliar_emitidos(
            f["rut_emisor"], f["sucursal"], int(f["mes"]), int(f["anio"])
        )),

        ("Obtener Trazas", [
            _f("RUT Emisor",     "rut_emisor", RUT_EMISOR),
            _f("Nombre Sucursal","sucursal",   SUCURSAL),
            _f("Tipo DTE",       "tipo_dte",   TIPO_DTE),
            _f("Folio",          "folio",      FOLIO),
            _f("Ambiente",       "ambiente",   AMBIENTE),
        ], lambda f, u, p: FacturacionController(u, p).obtener_trazas(
            f["rut_emisor"], f["sucursal"], int(f["tipo_dte"]), int(f["folio"]), int(f["ambiente"])
        )),

        ("Ceder Factura", [
            _f("RUT Empresa",           "rut_empresa",           RUT_EMPRESA),
            _f("Folio",                 "folio",                 FOLIO),
            _f("RUT Cesionario",        "rut_cesionario",        "76111222-3"),
            _f("RUT Persona Autorizada","rut_persona_autorizada","12345678-9"),
            _f("Correo Deudor",         "correo_deudor",         EMAIL),
            _f("Otras Condiciones",     "otras_condiciones",     "Pago a 30 días"),
        ], lambda f, u, p: FacturacionController(u, p).ceder_factura(
            f["rut_empresa"], int(f["folio"]), f["rut_cesionario"],
            f["rut_persona_autorizada"], f["correo_deudor"], f["otras_condiciones"]
        )),

        ("Preview DTE", [
            _f("Sucursal",     "sucursal",     SUCURSAL),
            _f("Request JSON", "request_json", INVOICE_JSON, "json"),
        ], lambda f, u, p: FacturacionController(u, p).preview_dte(
            f["sucursal"], f["request_json"]
        )),

        ("Reenvío SII", [
            _f("RUT Emisor",     "rut_emisor", RUT_EMISOR),
            _f("Nombre Sucursal","sucursal",   SUCURSAL),
            _f("Tipo DTE",       "tipo_dte",   TIPO_DTE),
            _f("Folio",          "folio",      FOLIO),
            _f("Ambiente",       "ambiente",   AMBIENTE),
        ], lambda f, u, p: FacturacionController(u, p).reenvio_sii(
            f["rut_emisor"], f["sucursal"], int(f["tipo_dte"]), int(f["folio"]), int(f["ambiente"])
        )),

        ("Anular Guía Despacho", [
            _f("RUT Empresa", "rut_empresa", RUT_EMPRESA),
            _f("Folio",       "folio",       FOLIO),
            _f("Ambiente",    "ambiente",    AMBIENTE),
        ], lambda f, u, p: FacturacionController(u, p).anular_guia(
            f["rut_empresa"], int(f["folio"]), int(f["ambiente"])
        )),

        ("Obtener Correo Intercambio", [
            _f("RUT Emisor",     "rut_emisor",  RUT_EMISOR),
            _f("Nombre Sucursal","sucursal",    SUCURSAL),
            _f("RUT Header",     "rut_header",  RUT_RECEPTOR),
        ], lambda f, u, p: FacturacionController(u, p).obtener_correo_intercambio(
            f["rut_emisor"], f["sucursal"], f["rut_header"]
        )),
    ]),

    # ── Clientes ─────────────────────────────────────────────────────────────
    ("Clientes", [
        ("Crear Cliente", [
            _f("RUT Emisor",   "rut_emisor",   RUT_EMISOR),
            _f("RUT Cliente",  "rut",          "11111111-1"),
            _f("Razón Social", "razon_social", "Cliente Demo SpA"),
            _f("Giro",         "giro",         "Comercio al por menor"),
            _f("Dir. Particular","dir_part",   "Los Pinos 100"),
            _f("Dir. Factura",  "dir_fact",    "Los Pinos 100"),
            _f("Correo Particular","correo_par","info@clientedemo.cl"),
            _f("Correo Factura","correo_fact", "factura@clientedemo.cl"),
            _f("Ciudad",        "ciudad",      "Santiago"),
            _f("Comuna",        "comuna",      "Providencia"),
        ], lambda f, u, p: ClientesController(u, p).crear_cliente(
            f["rut_emisor"], f["rut"], f["razon_social"], f["giro"],
            f["dir_part"], f["dir_fact"], f["correo_par"], f["correo_fact"],
            f["ciudad"], f["comuna"]
        )),

        ("Listar Clientes", [
            _f("RUT Emisor", "rut_emisor", RUT_EMISOR),
        ], lambda f, u, p: ClientesController(u, p).listar_clientes(f["rut_emisor"])),

        ("Obtener Datos Cliente", [
            _f("RUT Emisor",  "rut_emisor",  RUT_EMISOR),
            _f("RUT Cliente", "rut_cliente", "11111111-1"),
        ], lambda f, u, p: ClientesController(u, p).obtener_datos_cliente(
            f["rut_emisor"], f["rut_cliente"]
        )),

        ("Actualizar Cliente", [
            _f("RUT Emisor",    "rut_emisor",   RUT_EMISOR),
            _f("RUT Cliente",   "rut",          "11111111-1"),
            _f("Razón Social",  "razon_social", "Cliente Demo SpA Actualizado"),
            _f("Giro",          "giro",         "Comercio al por mayor"),
            _f("Dir. Particular","dir_part",    "Los Pinos 200"),
            _f("Dir. Factura",  "dir_fact",     "Los Pinos 200"),
            _f("Correo Particular","correo_par","nuevo@clientedemo.cl"),
            _f("Correo Factura","correo_fact",  "factura2@clientedemo.cl"),
            _f("Ciudad",        "ciudad",       "Valparaíso"),
            _f("Comuna",        "comuna",       "Viña del Mar"),
        ], lambda f, u, p: ClientesController(u, p).actualizar_cliente(
            f["rut_emisor"], f["rut"], f["razon_social"], f["giro"],
            f["dir_part"], f["dir_fact"], f["correo_par"], f["correo_fact"],
            f["ciudad"], f["comuna"]
        )),
    ]),

    # ── Productos ─────────────────────────────────────────────────────────────
    ("Productos", [
        ("Crear Producto", [
            _f("RUT Emisor",     "rut_emisor",   RUT_EMISOR),
            _f("Nombre",         "nombre",       "Servicio de Asesoría"),
            _f("Código de Barra","codigo_barra", "SKU-001"),
            _f("Unidad Medida",  "unidad_medida","Srv"),
            _f("Precio",         "precio",       "50000"),
            _f("Exento (True/False)", "exento",  "False",
               "combo", ["True", "False"]),
        ], lambda f, u, p: ProductoController(u, p).crear_producto(
            f["rut_emisor"], f["nombre"], f["codigo_barra"], f["unidad_medida"],
            float(f["precio"]), f["exento"].lower() == "true"
        )),

        ("Listar Productos", [
            _f("RUT Emisor", "rut_emisor", RUT_EMISOR),
        ], lambda f, u, p: ProductoController(u, p).listar_productos(f["rut_emisor"])),
    ]),

    # ── Folios ────────────────────────────────────────────────────────────────
    ("Folios", [
        ("Consulta Folios Disponibles", [
            _f("RUT Emisor", "rut_emisor", RUT_EMISOR),
            _f("Tipo DTE",   "tipo_dte",   TIPO_DTE),
            _f("Ambiente",   "ambiente",   AMBIENTE),
        ], lambda f, u, p: FolioController(u, p).consulta_folios_disponibles(
            f["rut_emisor"], int(f["tipo_dte"]), int(f["ambiente"])
        )),

        ("Solicitar Folios", [
            _f("RUT Empresa", "rut_empresa", RUT_EMPRESA),
            _f("Tipo DTE",    "tipo_dte",    TIPO_DTE),
            _f("Ambiente",    "ambiente",    AMBIENTE),
            _f("Cantidad",    "cantidad",    "50"),
        ], lambda f, u, p: FolioController(u, p).solicitar_folios(
            f["rut_empresa"], int(f["tipo_dte"]), int(f["ambiente"]), int(f["cantidad"])
        )),

        ("Consultar Folios", [
            _f("RUT Emisor", "rut_emisor", RUT_EMISOR),
            _f("Tipo DTE",   "tipo_dte",   TIPO_DTE),
            _f("Ambiente",   "ambiente",   AMBIENTE),
        ], lambda f, u, p: FolioController(u, p).consultar_folios(
            f["rut_emisor"], int(f["tipo_dte"]), int(f["ambiente"])
        )),

        ("Folios Sin Uso", [
            _f("RUT Emisor", "rut_emisor", RUT_EMISOR),
            _f("Tipo DTE",   "tipo_dte",   TIPO_DTE),
            _f("Ambiente",   "ambiente",   AMBIENTE),
        ], lambda f, u, p: FolioController(u, p).folios_sin_uso(
            f["rut_emisor"], int(f["tipo_dte"]), int(f["ambiente"])
        )),

        ("Anular Folio", [
            _f("RUT Emisor",    "rut_emisor",    RUT_EMISOR),
            _f("Tipo DTE",      "tipo_dte",      TIPO_DTE),
            _f("Ambiente",      "ambiente",      AMBIENTE),
            _f("Folio Inicio",  "folio_inicio",  "1"),
            _f("Folio Término", "folio_termino", "1"),
            _f("Motivo",        "motivo",        "No utilizado"),
        ], lambda f, u, p: FolioController(u, p).anular_folio(
            f["rut_emisor"], int(f["tipo_dte"]), int(f["ambiente"]),
            int(f["folio_inicio"]), int(f["folio_termino"]), f["motivo"]
        )),
    ]),

    # ── Configuración ─────────────────────────────────────────────────────────
    ("Configuración", [
        ("Datos Empresa", [
            _f("RUT Emisor", "rut_emisor", RUT_EMISOR),
        ], lambda f, u, p: ConfiguracionController(u, p).datos_empresa(f["rut_emisor"])),

        ("Subir Certificado Digital", [
            _f("RUT Emisor",          "rut_emisor",       RUT_EMISOR),
            _f("Ruta Certificado .pfx","path_certificado","C:/certificados/empresa.pfx"),
        ], lambda f, u, p: ConfiguracionController(u, p).subir_certificado_digital(
            f["rut_emisor"], f["path_certificado"]
        )),
    ]),

    # ── Sucursales ────────────────────────────────────────────────────────────
    ("Sucursales", [
        ("Listar Sucursales", [
            _f("RUT Emisor", "rut_emisor", RUT_EMISOR),
        ], lambda f, u, p: SucursalController(u, p).listar_sucursales(f["rut_emisor"])),
    ]),

    # ── Proveedor ─────────────────────────────────────────────────────────────
    ("Proveedor", [
        ("Aceptar / Rechazar DTE", [
            _f("RUT Emisor", "rut_emisor", RUT_EMISOR),
            _f("Tipo DTE",   "tipo_dte",   TIPO_DTE),
            _f("Folio",      "folio",      FOLIO),
            _f("Ambiente",   "ambiente",   AMBIENTE),
            _f("Respuesta (3=Aceptado, 4=Con reparos, 5=Rechazado)", "respuesta", "3",
               "combo", ["3 - Aceptado", "4 - Con reparos", "5 - Rechazado"]),
            _f("Tipo Rechazo (0=N/A, 1=RCD, 3=RFP, 4=RFT)", "tipo_rechazo", "0"),
            _f("Comentario", "comentario", "Recibido conforme"),
        ], lambda f, u, p: ProveedorController(u, p).aceptar_rechazar_dte(
            f["rut_emisor"], int(f["tipo_dte"]), int(f["folio"]), int(f["ambiente"]),
            int(f["respuesta"].split(" ")[0]) if " " in f["respuesta"] else int(f["respuesta"]),
            int(f["tipo_rechazo"]), f["comentario"]
        )),

        ("Listar DTE Recibidos", [
            _f("RUT Emisor",         "rut_emisor", RUT_EMISOR),
            _f("Tipo DTE",           "tipo_dte",   TIPO_DTE),
            _f("Desde (YYYY-MM-DD)", "desde",      DESDE),
            _f("Hasta (YYYY-MM-DD)", "hasta",      HASTA),
            _f("Ambiente",           "ambiente",   AMBIENTE),
        ], lambda f, u, p: ProveedorController(u, p).listar_dte_recibidos(
            f["rut_emisor"], int(f["tipo_dte"]), f["desde"], f["hasta"], int(f["ambiente"])
        )),

        ("Obtener XML (Recibido)", [
            _f("RUT Emisor", "rut_emisor", RUT_EMISOR),
            _f("Tipo DTE",   "tipo_dte",   TIPO_DTE),
            _f("Folio",      "folio",      FOLIO),
            _f("Ambiente",   "ambiente",   AMBIENTE),
        ], lambda f, u, p: ProveedorController(u, p).obtener_xml_recibido(
            f["rut_emisor"], int(f["tipo_dte"]), int(f["folio"]), int(f["ambiente"])
        )),

        ("Obtener PDF (Recibido)", [
            _f("RUT Emisor", "rut_emisor", RUT_EMISOR),
            _f("Tipo DTE",   "tipo_dte",   TIPO_DTE),
            _f("Folio",      "folio",      FOLIO),
            _f("Ambiente",   "ambiente",   AMBIENTE),
        ], lambda f, u, p: ProveedorController(u, p).obtener_pdf_recibido(
            f["rut_emisor"], int(f["tipo_dte"]), int(f["folio"]), int(f["ambiente"])
        )),

        ("Conciliar Recibidos", [
            _f("RUT Emisor", "rut_emisor", RUT_EMISOR),
            _f("Mes",        "mes",        MES),
            _f("Año",        "anio",       ANIO),
        ], lambda f, u, p: ProveedorController(u, p).conciliar_recibidos(
            f["rut_emisor"], int(f["mes"]), int(f["anio"])
        )),

        ("Obtener Trazas Recibidas", [
            _f("RUT Emisor", "rut_emisor", RUT_EMISOR),
            _f("Tipo DTE",   "tipo_dte",   TIPO_DTE),
            _f("Folio",      "folio",      FOLIO),
            _f("Ambiente",   "ambiente",   AMBIENTE),
        ], lambda f, u, p: ProveedorController(u, p).obtener_trazas_recibidas(
            f["rut_emisor"], int(f["tipo_dte"]), int(f["folio"]), int(f["ambiente"])
        )),

        ("Actualizar Lista Proveedor", [
            _f("RUT Emisor",   "rut_emisor",   RUT_EMISOR),
            _f("RUT Proveedor","rut_proveedor", "87654321-0"),
            _f("Lista (1=Negra, 2=Blanca, 3=Desconocido)", "lista", "2",
               "combo", ["1 - Lista Negra", "2 - Lista Blanca", "3 - Desconocido"]),
        ], lambda f, u, p: ProveedorController(u, p).actualizar_lista_proveedor(
            f["rut_emisor"], f["rut_proveedor"],
            int(f["lista"].split(" ")[0]) if " " in f["lista"] else int(f["lista"])
        )),
    ]),

    # ── Usuarios ──────────────────────────────────────────────────────────────
    ("Usuarios", [
        ("Listar Usuarios", [
            _f("RUT Emisor", "rut_emisor", RUT_EMISOR),
        ], lambda f, u, p: UsuarioController(u, p).listar_usuarios(f["rut_emisor"])),
    ]),

    # ── Cesiones ─────────────────────────────────────────────────────────────
    ("Cesiones", [
        ("Ceder Factura", [
            _f("RUT Empresa",            "rut_empresa",            RUT_EMPRESA),
            _f("Folio",                  "folio",                  FOLIO),
            _f("RUT Cesionario",         "rut_cesionario",         "76111222-3"),
            _f("RUT Persona Autorizada", "rut_persona_autorizada", "12345678-9"),
            _f("Correo Deudor",          "correo_deudor",          EMAIL),
            _f("Otras Condiciones",      "otras_condiciones",      "Pago a 30 días"),
        ], lambda f, u, p: CesionController(u, p).ceder_factura(
            f["rut_empresa"], int(f["folio"]), f["rut_cesionario"],
            f["rut_persona_autorizada"], f["correo_deudor"], f["otras_condiciones"]
        )),

        ("Obtener Trazas Cesión Emitida", [
            _f("RUT Emisor", "rut_emisor", RUT_EMISOR),
            _f("Folio",      "folio",      FOLIO),
            _f("Ambiente",   "ambiente",   AMBIENTE),
        ], lambda f, u, p: CesionController(u, p).obtener_trazas_cesion_emitida(
            f["rut_emisor"], int(f["folio"]), int(f["ambiente"])
        )),

        ("Listado Cesiones Emitidas", [
            _f("RUT Emisor",         "rut_emisor", RUT_EMISOR),
            _f("Ambiente",           "ambiente",   AMBIENTE),
            _f("Desde (YYYY-MM-DD)", "desde",      DESDE),
            _f("Hasta (YYYY-MM-DD)", "hasta",      HASTA),
        ], lambda f, u, p: CesionController(u, p).listado_cesiones_emitidas(
            f["rut_emisor"], int(f["ambiente"]), f["desde"], f["hasta"]
        )),
    ]),

    # ── Partner ───────────────────────────────────────────────────────────────
    ("Partner", [
        ("Enrolamiento Empresa", [
            _f("RUT Empresa",        "rut_empresa",    RUT_EMPRESA),
            _f("Razón Social",       "razon_social",   "Mi Empresa SpA"),
            _f("RUT Rep. Legal",     "rut_rep_legal",  "12345678-9"),
            _f("Giro",               "giro",           "Servicios de Tecnología"),
            _f("Email",              "email",          "admin@miempresa.cl"),
            _f("Dirección",          "direccion",      "Av. Providencia 1234"),
            _f("Ciudad",             "ciudad",         "Santiago"),
            _f("Comuna",             "comuna",         "Providencia"),
            _f("Teléfono",           "telefono",       "+56912345678"),
            _f("Unidad SII",         "unidad_sii",     "Santiago Oriente"),
            _f("Ambiente",           "ambiente",       AMBIENTE),
        ], lambda f, u, p: PartnerController(u, p).enrolamiento_empresa(
            f["rut_empresa"], f["razon_social"], f["rut_rep_legal"], f["giro"],
            f["email"], f["direccion"], f["ciudad"], f["comuna"],
            f["telefono"], f["unidad_sii"], int(f["ambiente"])
        )),

        ("Obtener Actividades Económicas", [],
         lambda _f, u, p: PartnerController(u, p).obtener_actividades_economicas()),

        ("Upload Logo", [
            _f("RUT Emisor", "rut_emisor", RUT_EMISOR),
            _f("Ruta Logo",  "path_logo",  "C:/logos/empresa.png"),
        ], lambda f, u, p: PartnerController(u, p).upload_logo(
            f["rut_emisor"], f["path_logo"]
        )),

        ("Obtener Resumen DTEs", [
            _f("RUT Emisor", "rut_emisor", RUT_EMISOR),
            _f("Año",        "anio",       ANIO),
            _f("Mes",        "mes",        MES),
        ], lambda f, u, p: PartnerController(u, p).obtener_resumen_dtes(
            f["rut_emisor"], int(f["anio"]), int(f["mes"])
        )),
    ]),

    # ── Payku ─────────────────────────────────────────────────────────────────
    ("Payku", [
        ("Transacciones", [
            _f("RUT Emisor",         "rut_emisor", RUT_EMISOR),
            _f("Desde (YYYY-MM-DD)", "desde",      DESDE),
            _f("Hasta (YYYY-MM-DD)", "hasta",      HASTA),
        ], lambda f, u, p: PaykuController(u, p).transacciones(
            f["rut_emisor"], f["desde"], f["hasta"]
        )),

        ("Activar / Desactivar", [
            _f("RUT Emisor",             "rut_emisor", RUT_EMISOR),
            _f("Activo (True/False)",    "activo",     "True",
               "combo", ["True", "False"]),
        ], lambda f, u, p: PaykuController(u, p).activar_desactivar(
            f["rut_emisor"], f["activo"].lower() == "true"
        )),

        ("Generar URL", [
            _f("RUT Emisor", "rut_emisor", RUT_EMISOR),
            _f("Tipo DTE",   "tipo_dte",   TIPO_DTE),
            _f("Folio",      "folio",      FOLIO),
            _f("Ambiente",   "ambiente",   AMBIENTE),
        ], lambda f, u, p: PaykuController(u, p).generar_url(
            f["rut_emisor"], int(f["tipo_dte"]), int(f["folio"]), int(f["ambiente"])
        )),

        ("Reenviar Link QR", [
            _f("RUT Emisor", "rut_emisor", RUT_EMISOR),
            _f("Tipo DTE",   "tipo_dte",   TIPO_DTE),
            _f("Folio",      "folio",      FOLIO),
            _f("Ambiente",   "ambiente",   AMBIENTE),
        ], lambda f, u, p: PaykuController(u, p).reenviar_link_qr(
            f["rut_emisor"], int(f["tipo_dte"]), int(f["folio"]), int(f["ambiente"])
        )),

        ("Marcar DTE Pagado / Pendiente", [
            _f("RUT Emisor",          "rut_emisor", RUT_EMISOR),
            _f("Tipo DTE",            "tipo_dte",   TIPO_DTE),
            _f("Folio",               "folio",      FOLIO),
            _f("Ambiente",            "ambiente",   AMBIENTE),
            _f("Pagado (True/False)", "pagado",     "True",
               "combo", ["True", "False"]),
        ], lambda f, u, p: PaykuController(u, p).marcar_pagado_o_pendiente(
            f["rut_emisor"], int(f["tipo_dte"]), int(f["folio"]), int(f["ambiente"]),
            f["pagado"].lower() == "true"
        )),
    ]),
]


# ── Main View ─────────────────────────────────────────────────────────────────

class MainView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SimpleFactura SDK — Demo")
        self.root.geometry("1400x860")
        self.root.minsize(1100, 680)

        # Colour palette
        BG      = "#F5F6FA"
        SIDEBAR = "#2C3E50"
        ACCENT  = "#3498DB"
        BTN_BG  = "#2980B9"
        BTN_FG  = "#FFFFFF"
        RESULT_BG = "#1E1E2E"
        RESULT_FG = "#E8E8E8"

        self.root.configure(bg=BG)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                         background=SIDEBAR, foreground="#ECF0F1",
                         fieldbackground=SIDEBAR, rowheight=28,
                         font=("Segoe UI", 9),
                         indent=20)
        style.configure("Treeview.Heading",
                         background="#1A252F", foreground="#ECF0F1",
                         font=("Segoe UI", 9, "bold"))
        style.map("Treeview", background=[("selected", ACCENT)])
        style.configure("Execute.TButton",
                         background=BTN_BG, foreground=BTN_FG,
                         font=("Segoe UI", 10, "bold"),
                         padding=(20, 8))
        style.map("Execute.TButton", background=[("active", "#1A6FA8")])
        style.configure("TLabel", background=BG, font=("Segoe UI", 9))
        style.configure("TFrame", background=BG)
        style.configure("Header.TLabel",
                         background=BG, font=("Segoe UI", 13, "bold"),
                         foreground="#2C3E50")
        style.configure("Cred.TLabel",
                         background="#EAF0FB", font=("Segoe UI", 9))
        style.configure("Cred.TFrame", background="#EAF0FB")

        # ── Top credential bar ──
        cred_bar = ttk.Frame(self.root, style="Cred.TFrame", padding=6)
        cred_bar.pack(side=tk.TOP, fill=tk.X)

        ttk.Label(cred_bar, text="Usuario:", style="Cred.TLabel").pack(side=tk.LEFT, padx=(8, 2))
        self.var_user = tk.StringVar(value="demo@chilesystems.com")
        tk.Entry(cred_bar, textvariable=self.var_user, width=28,
                 font=("Segoe UI", 9), relief="flat",
                 highlightthickness=1, highlightbackground="#BDC3D0").pack(side=tk.LEFT, padx=(0, 12))

        ttk.Label(cred_bar, text="Contraseña:", style="Cred.TLabel").pack(side=tk.LEFT, padx=(0, 2))
        self.var_pass = tk.StringVar(value="Rv8Il4eV")
        self._pass_entry = tk.Entry(cred_bar, textvariable=self.var_pass, width=18, show="*",
                                     font=("Segoe UI", 9), relief="flat",
                                     highlightthickness=1, highlightbackground="#BDC3D0")
        self._pass_entry.pack(side=tk.LEFT, padx=(0, 3))

        def _toggle_pass():
            if self._pass_entry.cget("show") == "*":
                self._pass_entry.configure(show="")
                _btn_eye.configure(text="🔒")
            else:
                self._pass_entry.configure(show="*")
                _btn_eye.configure(text="👁")

        _btn_eye = tk.Button(cred_bar, text="👁", font=("Segoe UI", 9),
                              relief="flat", bg="#EAF0FB", activebackground="#D0E4F7",
                              cursor="hand2", bd=0, padx=4, command=_toggle_pass)
        _btn_eye.pack(side=tk.LEFT, padx=(0, 12))

        ttk.Label(cred_bar,
                  text="← Ingresa tus credenciales antes de ejecutar",
                  style="Cred.TLabel", foreground="#7F8C8D").pack(side=tk.LEFT)

        # ── Main body: sidebar + content ──
        body = tk.Frame(self.root, bg=BG)
        body.pack(fill=tk.BOTH, expand=True)

        # Sidebar
        sidebar = tk.Frame(body, bg=SIDEBAR, width=300)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        sidebar.pack_propagate(False)

        tk.Label(sidebar, text="  SimpleFactura SDK",
                 bg=SIDEBAR, fg="#ECF0F1",
                 font=("Segoe UI", 11, "bold"), anchor="w",
                 padx=8, pady=12).pack(fill=tk.X)

        tk.Frame(sidebar, bg="#1A252F", height=1).pack(fill=tk.X)

        # Scrollbar must be packed BEFORE the treeview so it appears to the right
        tree_scroll = tk.Scrollbar(sidebar, orient="vertical", bg=SIDEBAR)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree = ttk.Treeview(sidebar, show="tree", selectmode="browse",
                                   yscrollcommand=tree_scroll.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tree_scroll.configure(command=self.tree.yview)

        # Content panel
        content = tk.Frame(body, bg=BG)
        content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Title
        self.lbl_title = ttk.Label(content, text="Selecciona un endpoint →",
                                    style="Header.TLabel", padding=(16, 12, 0, 4))
        self.lbl_title.pack(fill=tk.X)

        ttk.Separator(content, orient="horizontal").pack(fill=tk.X, padx=12, pady=(0, 8))

        # Form + result split
        paned = tk.PanedWindow(content, orient=tk.VERTICAL,
                                sashwidth=6, bg="#BDC3D0", relief="flat")
        paned.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 10))

        # Form panel (scrollable)
        form_outer = tk.Frame(paned, bg=BG)
        paned.add(form_outer, minsize=160)

        form_canvas = tk.Canvas(form_outer, bg=BG, highlightthickness=0)
        form_vscroll = tk.Scrollbar(form_outer, orient="vertical",
                                     command=form_canvas.yview)
        form_canvas.configure(yscrollcommand=form_vscroll.set)
        form_vscroll.pack(side=tk.RIGHT, fill=tk.Y)
        form_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.form_frame = tk.Frame(form_canvas, bg=BG)
        self.form_canvas_window = form_canvas.create_window(
            (0, 0), window=self.form_frame, anchor="nw"
        )
        self.form_frame.bind("<Configure>", lambda _: form_canvas.configure(
            scrollregion=form_canvas.bbox("all")
        ))
        form_canvas.bind("<Configure>", lambda e: form_canvas.itemconfig(
            self.form_canvas_window, width=e.width
        ))

        # Result panel
        result_frame = tk.Frame(paned, bg=BG)
        paned.add(result_frame, minsize=160)

        tk.Label(result_frame, text="Resultado:", bg=BG,
                 font=("Segoe UI", 9, "bold"), fg="#2C3E50",
                 anchor="w").pack(fill=tk.X, pady=(6, 2))

        res_scroll = tk.Scrollbar(result_frame, orient="vertical")
        res_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text = tk.Text(
            result_frame, wrap=tk.WORD,
            bg=RESULT_BG, fg=RESULT_FG,
            font=("Consolas", 9),
            relief="flat", state=tk.DISABLED,
            insertbackground=RESULT_FG,
            yscrollcommand=res_scroll.set
        )
        res_scroll.configure(command=self.result_text.yview)
        self.result_text.pack(fill=tk.BOTH, expand=True)

        # Syntax-highlight colour tags
        self.result_text.tag_configure("hdr_ok",      foreground="#98C379", font=("Consolas", 9, "bold"))
        self.result_text.tag_configure("hdr_err",     foreground="#E06C75", font=("Consolas", 9, "bold"))
        self.result_text.tag_configure("loading",     foreground="#E5C07B", font=("Consolas", 9, "italic"))
        self.result_text.tag_configure("lbl_datos",   foreground="#7F848E", font=("Consolas", 9))
        self.result_text.tag_configure("json_key",    foreground="#56B6C2")
        self.result_text.tag_configure("json_str",    foreground="#98C379")
        self.result_text.tag_configure("json_num",    foreground="#D19A66")
        self.result_text.tag_configure("json_kw",     foreground="#C678DD")
        self.result_text.tag_configure("json_punct",  foreground="#5C6370")
        self.result_text.tag_configure("xml_tag",     foreground="#E06C75")
        self.result_text.tag_configure("xml_attr",    foreground="#D19A66")
        self.result_text.tag_configure("xml_str",     foreground="#98C379")
        self.result_text.tag_configure("xml_pi",      foreground="#7F848E")

        # ── Build treeview ──
        self._node_map: dict[str, tuple] = {}  # iid → (fields, handler)

        for service_label, endpoints in REGISTRY:
            parent = self.tree.insert("", tk.END, text=f"  {service_label}",
                                       open=False)
            for ep_name, fields, handler in endpoints:
                iid = self.tree.insert(parent, tk.END, text=f"  {ep_name}")
                self._node_map[iid] = (fields, handler, ep_name, service_label)

        self.tree.bind("<<TreeviewSelect>>", self._on_tree_select)
        self._current_vars: dict[str, tk.StringVar] = {}
        self._current_handler = None

    # ── Tree selection ─────────────────────────────────────────────────────────

    def _on_tree_select(self, _event):
        selected = self.tree.selection()
        if not selected:
            return
        iid = selected[0]
        if iid not in self._node_map:
            return
        fields, handler, ep_name, svc_label = self._node_map[iid]
        self._build_form(fields, handler, ep_name, svc_label)

    # ── Build dynamic form ─────────────────────────────────────────────────────

    def _build_form(self, fields, handler, ep_name, svc_label):
        for w in self.form_frame.winfo_children():
            w.destroy()
        self._current_vars = {}
        self._current_handler = handler

        self.lbl_title.configure(text=f"{svc_label}  ›  {ep_name}")

        if not fields:
            ttk.Label(self.form_frame, text="Este endpoint no requiere parámetros.",
                       foreground="#7F8C8D", padding=(12, 8)).pack(anchor="w")
        else:
            for field in fields:
                row = tk.Frame(self.form_frame, bg=self.form_frame["bg"])
                row.pack(fill=tk.X, padx=16, pady=5)

                lbl = tk.Label(row, text=field["label"] + ":",
                                bg=self.form_frame["bg"],
                                font=("Segoe UI", 9), fg="#2C3E50",
                                width=30, anchor="w")
                lbl.pack(side=tk.LEFT, padx=(4, 6))

                var = tk.StringVar(value=field["default"])
                self._current_vars[field["key"]] = var

                if field["type"] == "json":
                    txt_outer = tk.Frame(row, bg="#BDC3D0",
                                          highlightthickness=0, bd=1, relief="solid")
                    txt_outer.pack(side=tk.LEFT, fill=tk.X, expand=True)
                    txt_vsc = tk.Scrollbar(txt_outer, orient="vertical")
                    txt_vsc.pack(side=tk.RIGHT, fill=tk.Y)
                    txt_hsc = tk.Scrollbar(txt_outer, orient="horizontal")
                    txt_hsc.pack(side=tk.BOTTOM, fill=tk.X)
                    txt = tk.Text(txt_outer, height=16, width=60,
                                   font=("Consolas", 8), relief="flat", bd=0,
                                   highlightthickness=0,
                                   bg="#FAFBFC", wrap=tk.NONE,
                                   yscrollcommand=txt_vsc.set,
                                   xscrollcommand=txt_hsc.set)
                    txt_vsc.configure(command=txt.yview)
                    txt_hsc.configure(command=txt.xview)
                    txt.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
                    txt.insert("1.0", field["default"])
                    self._current_vars[f"__text__{field['key']}"] = txt

                elif field["type"] == "combo":
                    combo = ttk.Combobox(row, textvariable=var,
                                          values=field["options"],
                                          state="readonly", width=38,
                                          font=("Segoe UI", 9))
                    combo.pack(side=tk.LEFT)

                else:
                    entry = tk.Entry(row, textvariable=var, width=40,
                                      font=("Segoe UI", 9), relief="flat",
                                      highlightthickness=1,
                                      highlightbackground="#BDC3D0",
                                      bg="#FAFBFC")
                    entry.pack(side=tk.LEFT)

        # Execute button
        btn_row = tk.Frame(self.form_frame, bg=self.form_frame["bg"])
        btn_row.pack(fill=tk.X, padx=12, pady=(10, 6))
        ttk.Button(btn_row, text="  ▶  Ejecutar  ", style="Execute.TButton",
                   command=self._execute).pack(side=tk.LEFT)

    # ── Execute ────────────────────────────────────────────────────────────────

    def _execute(self):
        if self._current_handler is None:
            return

        # Collect field values
        fields_dict = {}
        for key, var in self._current_vars.items():
            if key.startswith("__text__"):
                real_key = key[len("__text__"):]
                fields_dict[real_key] = var.get("1.0", tk.END).strip()
            else:
                fields_dict[key] = var.get()

        username = self.var_user.get().strip()
        password = self.var_pass.get().strip()

        self._set_result("⏳ Ejecutando…")

        handler = self._current_handler

        def run():
            try:
                result = handler(fields_dict, username, password)
            except Exception as exc:
                result = f"✗ Error inesperado: {exc}"
            self.root.after(0, lambda: self._set_result(result))

        threading.Thread(target=run, daemon=True).start()

    def _set_result(self, text: str):
        w = self.result_text
        w.configure(state=tk.NORMAL)
        w.delete("1.0", tk.END)

        if text.startswith("⏳"):
            w.insert(tk.END, text, "loading")
        elif text.startswith("✗") or text.startswith("✓"):
            nl = text.find("\n")
            if nl == -1:
                tag = "hdr_err" if text.startswith("✗") else "hdr_ok"
                w.insert(tk.END, text, tag)
            else:
                header, body = text[:nl + 1], text[nl + 1:]
                tag = "hdr_err" if text.startswith("✗") else "hdr_ok"
                w.insert(tk.END, header, tag)
                if body.startswith("Datos:\n"):
                    w.insert(tk.END, "Datos:\n", "lbl_datos")
                    body = body[7:]
                elif body.startswith("PDF abierto") or body.startswith("Datos binarios"):
                    w.insert(tk.END, body)
                    w.configure(state=tk.DISABLED)
                    return
                b = body.lstrip()
                if b.startswith("{") or b.startswith("["):
                    self._highlight_json(body)
                elif b.startswith("<"):
                    self._highlight_xml(body)
                else:
                    w.insert(tk.END, body)
        else:
            w.insert(tk.END, text)

        w.configure(state=tk.DISABLED)

    # ── Syntax highlighting ────────────────────────────────────────────────────

    def _highlight_json(self, text: str):
        import re
        w = self.result_text
        TOKEN = re.compile(
            r'("(?:[^"\\]|\\.)*")'          # 1 string
            r'|(\btrue\b|\bfalse\b|\bnull\b)' # 2 keyword
            r'|(-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)'  # 3 number
            r'|([{}\[\],:])'                 # 4 punctuation
            r'|(\s+)'                        # 5 whitespace
            r'|(.)',                          # 6 other
            re.DOTALL
        )
        tokens = list(TOKEN.finditer(text))
        n = len(tokens)
        for i, m in enumerate(tokens):
            s, kw, num, punct, ws, other = m.groups()
            if s:
                is_key = False
                for j in range(i + 1, min(i + 6, n)):
                    nxt = tokens[j]
                    if nxt.group(5):
                        continue
                    is_key = nxt.group(4) == ":"
                    break
                w.insert(tk.END, s, "json_key" if is_key else "json_str")
            elif kw:
                w.insert(tk.END, kw, "json_kw")
            elif num:
                w.insert(tk.END, num, "json_num")
            elif punct:
                w.insert(tk.END, punct, "json_punct")
            elif ws:
                w.insert(tk.END, ws)
            else:
                w.insert(tk.END, other or "")

    def _highlight_xml(self, text: str):
        import re
        w = self.result_text
        ATTR = re.compile(r'([\w:.-]+)(=)("[^"]*"|\'[^\']*\')')
        for m in re.finditer(r'(<[^>]+>)|([^<]+)', text, re.DOTALL):
            tag_src, content = m.group(1), m.group(2)
            if tag_src:
                if tag_src.startswith("<?") or tag_src.startswith("<!"):
                    w.insert(tk.END, tag_src, "xml_pi")
                elif tag_src.startswith("</"):
                    w.insert(tk.END, tag_src, "xml_tag")
                else:
                    inner = tag_src[1:-1]
                    close_slash = "/" if inner.endswith("/") else ""
                    if close_slash:
                        inner = inner[:-1]
                    nm = re.match(r"^(/?[\w:.-]+)", inner)
                    if nm:
                        w.insert(tk.END, "<", "xml_tag")
                        w.insert(tk.END, nm.group(1), "xml_tag")
                        rest = inner[nm.end():]
                        last = 0
                        for am in ATTR.finditer(rest):
                            if am.start() > last:
                                w.insert(tk.END, rest[last:am.start()])
                            w.insert(tk.END, am.group(1), "xml_attr")
                            w.insert(tk.END, am.group(2))
                            w.insert(tk.END, am.group(3), "xml_str")
                            last = am.end()
                        if last < len(rest):
                            w.insert(tk.END, rest[last:])
                        w.insert(tk.END, close_slash + ">", "xml_tag")
                    else:
                        w.insert(tk.END, tag_src, "xml_tag")
            elif content:
                w.insert(tk.END, content)

    # ── Run ────────────────────────────────────────────────────────────────────

    def run(self):
        self.root.mainloop()
