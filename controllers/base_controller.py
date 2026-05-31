import json
import os
import platform
import subprocess
import tempfile


class BaseController:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @staticmethod
    def _open_file(path: str) -> None:
        system = platform.system()
        if system == "Windows":
            os.startfile(path)
        elif system == "Darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])

    def _handle_bytes(self, data: bytes, status: int) -> str:
        if data[:4] == b'%PDF':
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
            tmp.write(data)
            tmp.close()
            self._open_file(tmp.name)
            return f"✓ Status: {status}\nPDF abierto ({len(data):,} bytes)\nArchivo temporal: {tmp.name}"

        # Try to decode as text
        for enc in ('utf-8', 'iso-8859-1', 'latin-1'):
            try:
                text = data.decode(enc)
            except UnicodeDecodeError:
                continue

            # JSON
            try:
                parsed = json.loads(text)
                return f"✓ Status: {status}\n{json.dumps(parsed, indent=2, ensure_ascii=False)}"
            except (json.JSONDecodeError, ValueError):
                pass

            # XML or plain text
            stripped = text.lstrip()
            if stripped.startswith('<'):
                return f"✓ Status: {status}\n{text}"

            return f"✓ Status: {status}\n{text}"

        # Truly opaque binary
        return f"✓ Status: {status}\nDatos binarios: {len(data):,} bytes"

    def format_response(self, response) -> str:
        if response is None:
            return "Error: No se recibió respuesta del servidor."
        if response.status == 200:
            if response.data is None:
                msg = response.message or "Operación exitosa"
                return f"✓ Status: {response.status}\nMensaje: {msg}"
            if isinstance(response.data, bytes):
                return self._handle_bytes(response.data, response.status)
            try:
                if hasattr(response.data, '__iter__') and not isinstance(response.data, str):
                    items = list(response.data)
                    if items and hasattr(items[0], '__dict__'):
                        data_str = json.dumps([i.__dict__ for i in items], indent=2, default=str, ensure_ascii=False)
                    else:
                        data_str = json.dumps(items, indent=2, default=str, ensure_ascii=False)
                elif hasattr(response.data, '__dict__'):
                    data_str = json.dumps(response.data.__dict__, indent=2, default=str, ensure_ascii=False)
                else:
                    data_str = json.dumps(response.data, indent=2, default=str, ensure_ascii=False)
            except Exception:
                data_str = str(response.data)
            return f"✓ Status: {response.status}\nDatos:\n{data_str}"
        else:
            err = response.message or "Error desconocido"
            return f"✗ Status: {response.status}\nError: {err}"
