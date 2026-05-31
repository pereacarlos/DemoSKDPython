# SimpleFacturaSDK — Demo App (Python + tkinter)

Aplicación de escritorio interactiva que demuestra el uso completo de **SimpleFacturaSDK** para Python, cubriendo los ~63 endpoints distribuidos en 12 servicios del API de Simple Factura (facturación electrónica chilena SII).

---

## Requisitos previos

| Requisito | Versión mínima |
|-----------|---------------|
| Python | 3.10+ |
| Sistema operativo | Windows, Linux o macOS |

---

## Instalación

### 1. Clonar / descargar el proyecto

```bash
git clone <https://github.com/pereacarlos/DemoSKDPython.git>
cd DemoSKDPython
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` contiene:

```
SimpleFacturaSDK==1.2.0
aiohttp>=3.9.0
```

> **Nota:** `tkinter` viene incluido con Python para Windows; no requiere instalación separada.

### 4. Verificar que `config.py` exista en la raíz del proyecto

El SDK importa `BASE_URL` desde `config.py` en tiempo de carga del módulo. El archivo ya está incluido en el repositorio con el valor correcto:

```python
# config.py
BASE_URL = "https://api.simplefactura.cl"
```

Si necesitas apuntar a un entorno de pruebas diferente, modifica este archivo.

---

## Ejecutar la aplicación

Desde la carpeta raíz del proyecto (`DemoSKDPython/`):

```bash
python main.py
```

---

## Estructura del proyecto

```
DemoSKDPython/
├── main.py                          # Punto de entrada
├── config.py                        # BASE_URL del SDK
├── requirements.txt
├── README.md
├── controllers/
│   ├── base_controller.py           # Manejo de respuestas, bytes, PDF
│   ├── facturacion_controller.py    # Servicio Facturación (20 endpoints)
│   ├── boletahonorario_controller.py# Boleta Honorario Electrónica (10)
│   ├── clientes_controller.py       # Clientes (4)
│   ├── producto_controller.py       # Productos (2)
│   ├── folio_controller.py          # Folios (5)
│   ├── configuracion_controller.py  # Configuración (2)
│   ├── sucursal_controller.py       # Sucursales (1)
│   ├── proveedor_controller.py      # Proveedores (7)
│   ├── usuario_controller.py        # Usuarios (1)
│   ├── cesion_controller.py         # Cesiones (3)
│   ├── partner_controller.py        # Partners (4)
│   └── payku_controller.py          # Payku (5)
└── view/
    └── main_view.py                 # Interfaz gráfica (tkinter)
```

---

## Uso de la interfaz

### Credenciales

Al abrir la app verás una barra superior con los campos **Usuario** y **Contraseña**. Ingresa tus credenciales de Simple Factura antes de ejecutar cualquier endpoint.

- El botón **👁 Ver / 🔒 Ocultar** permite ver o enmascarar la contraseña.
- Las credenciales se reutilizan en todas las llamadas sin necesidad de reingresar.

### Navegación

El panel izquierdo muestra un árbol con los **12 servicios**. Expande cualquier servicio para ver sus endpoints. Al hacer clic en un endpoint el panel central muestra el formulario correspondiente.

### Formularios

- Cada campo viene **pre-cargado con datos de demostración** listos para ejecutar.
- Los campos de tipo **ruta/archivo** (certificado, CSV, logo, etc.) tienen un botón **📂** que abre el explorador de archivos.
- Los endpoints que requieren un JSON de solicitud muestran un área de texto editable con la estructura pre-armada.

### Ejecutar

Presiona el botón **▶ Ejecutar** para llamar al API. La ejecución corre en un hilo de fondo (sin bloquear la UI) y el resultado se muestra en el panel derecho al completarse.

### Respuestas

El panel de respuesta muestra el resultado con **resaltado de sintaxis**:

| Color | Significado |
|-------|-------------|
| Verde | Claves JSON / nombres de atributo XML |
| Celeste | Valores de tipo string |
| Naranja | Números |
| Morado | `true` / `false` / `null` |
| Gris | Llaves, corchetes, signos de puntuación |
| Azul | Tags XML |
| Rojo | Respuesta de error (status ≠ 200) |

**Archivos PDF:** se abren automáticamente con el visor predeterminado del sistema y se muestra la ruta del archivo temporal.

---

## Servicios y endpoints cubiertos

### 1. Facturación (20 endpoints)

| Endpoint | Descripción |
|----------|-------------|
| Obtener PDF | Descarga el PDF de un DTE emitido |
| Obtener Timbre | Obtiene el timbre digital del DTE |
| Obtener XML | Descarga el XML del DTE |
| Obtener DTE | Obtiene el objeto DTE completo |
| Obtener Sobre XML | Descarga el sobre XML del DTE |
| Obtener Trazas | Consulta el historial de estados del DTE |
| Facturación Individual V2 DTE | Emite una factura electrónica (33/34/etc.) |
| Facturación Individual V2 Boletas | Emite una boleta electrónica |
| Facturación Individual V2 Exportación | Emite DTE de exportación |
| Facturación Masiva | Carga masiva de DTE desde CSV |
| Emisión NC/ND V2 | Emite Nota de Crédito o Débito |
| Preview DTE | Previsualiza el DTE antes de emitir |
| Listado DTE Emitidos | Lista DTE emitidos en un rango de fechas |
| Consolidado Ventas | Consolidado de ventas por período |
| Conciliar Emitidos | Conciliación con el SII |
| Reenvío SII | Reenvía el DTE al SII |
| Anular Guía | Anula una guía de despacho |
| Enviar Correo | Envía el DTE por email al receptor |
| Obtener Correo Intercambio | Obtiene el correo de intercambio |

### 2. Boleta Honorario Electrónica (10 endpoints)

| Endpoint | Descripción |
|----------|-------------|
| Obtener PDF (Emitida) | PDF de BHE emitida |
| Listado BHE Emitidas | Lista de BHE emitidas por período |
| Obtener PDF (Recibida) | PDF de BHE recibida |
| Listado BHE Recibidas | Lista de BHE recibidas por período |
| Emitir BHE | Emite una nueva Boleta de Honorario |
| Emitir BHE Terceros | Emite BHE por cuenta de terceros |
| Anular BHE | Anula una BHE emitida |
| Observar BHE | Registra una observación en una BHE |
| Conciliar BHE Emitidas | Conciliación de BHE emitidas |
| Conciliar BHE Recibidas | Conciliación de BHE recibidas |

### 3. Clientes (4 endpoints)

| Endpoint | Descripción |
|----------|-------------|
| Crear Cliente | Registra un nuevo receptor externo |
| Listar Clientes | Lista todos los clientes |
| Obtener Datos Cliente | Obtiene los datos de un cliente por RUT |
| Actualizar Cliente | Actualiza los datos de un cliente |

### 4. Productos (2 endpoints)

| Endpoint | Descripción |
|----------|-------------|
| Listar Productos | Lista el catálogo de productos |
| Agregar Producto | Agrega un nuevo producto al catálogo |

### 5. Folios (5 endpoints)

| Endpoint | Descripción |
|----------|-------------|
| Consulta Folios Disponibles | Consulta folios disponibles por tipo DTE |
| Solicitar Folios | Solicita nuevos folios al SII |
| Consultar Folios | Consulta folios en uso |
| Folios Sin Uso | Lista folios sin usar |
| Anular Folio | Anula un rango de folios |

### 6. Configuración (2 endpoints)

| Endpoint | Descripción |
|----------|-------------|
| Obtener Configuración | Obtiene la configuración de la empresa |
| Agregar Logo | Carga el logotipo de la empresa |

### 7. Sucursales (1 endpoint)

| Endpoint | Descripción |
|----------|-------------|
| Listar Sucursales | Lista todas las sucursales registradas |

### 8. Proveedores (7 endpoints)

| Endpoint | Descripción |
|----------|-------------|
| Aceptar / Rechazar DTE | Responde a un DTE recibido |
| Listar DTE Recibidos | Lista DTE recibidos en un período |
| Obtener XML Recibido | Descarga el XML de un DTE recibido |
| Obtener PDF Recibido | Descarga el PDF de un DTE recibido |
| Conciliar Recibidos | Conciliación de DTE recibidos |
| Obtener Trazas Recibidas | Historial de estados de DTE recibido |
| Actualizar Lista Proveedor | Mueve un proveedor a lista blanca/negra |

### 9. Usuarios (1 endpoint)

| Endpoint | Descripción |
|----------|-------------|
| Listar Usuarios | Lista los usuarios de la cuenta |

### 10. Cesiones (3 endpoints)

| Endpoint | Descripción |
|----------|-------------|
| Ceder Factura | Cede una factura a un cesionario |
| Obtener Trazas de Cesión Emitida | Historial de una cesión |
| Listado Cesiones Emitidas | Lista cesiones emitidas por período |

### 11. Partners (4 endpoints)

| Endpoint | Descripción |
|----------|-------------|
| Listar Empresas | Lista empresas del partner |
| DTE Emitidos Partner | DTE emitidos a través del partner |
| DTE Recibidos Partner | DTE recibidos a través del partner |
| Obtener PDF Partner | PDF de DTE gestionado por el partner |

### 12. Payku (5 endpoints)

| Endpoint | Descripción |
|----------|-------------|
| Transacciones | Lista transacciones de Payku |
| Activar / Desactivar | Habilita o deshabilita la integración |
| Generar URL | Genera link de pago para un DTE |
| Reenviar Link QR | Reenvía el link/QR de pago |
| Marcar Pagado o Pendiente | Cambia el estado de pago de un DTE |

---

## Datos de demostración pre-cargados

Los formularios se pre-llenan con los siguientes valores de ejemplo. Puedes modificarlos antes de ejecutar:

| Campo | Valor demo |
|-------|-----------|
| RUT Emisor | `78181331-1` |
| RUT Receptor | `17096073-4` |
| Nombre Sucursal | `Casa Matriz` |
| Ambiente | `0` (Certificación) |
| Folio | `1` |
| Tipo DTE | `33` (Factura Electrónica) |
| Desde | `2026-01-01` |
| Hasta | `2026-01-31` |
| Mes / Año | `1` / `2026` |

> **Importante:** Los datos pre-cargados son de ejemplo. Para ejecutar correctamente los endpoints debes reemplazarlos con los RUTs, folios y credenciales reales de tu cuenta en Simple Factura.

---

## Notas técnicas

- **Entorno:** El valor `0` en el campo Ambiente corresponde a **Certificación (SII)**. Usa `1` para **Producción**.
- **Nombre Sucursal:** Los endpoints de Facturación requieren que el campo `Nombre Sucursal` no esté vacío; de lo contrario la API retorna error 500 "Nombre de sucursal vacia".
- **Async/sync:** Cada controlador usa `asyncio.run()` para ejecutar las llamadas async del SDK de forma sincrónica. La UI lanza cada llamada en un `threading.Thread(daemon=True)` para no bloquear la interfaz.
- **Respuestas binarias:** Los endpoints que retornan PDF abren automáticamente el archivo con el visor predeterminado. Los que retornan bytes de timbre o XML los decodifican y los muestran como texto.

---

## Licencia

Este proyecto es un demo de referencia. Consulta los términos de uso del SDK en [Simple Factura](https://www.simplefactura.cl).
