# Streamlit Hash Demo

Aplicación didáctica en Streamlit para explorar funciones hash criptográficas (SHA, BLAKE2), salting, peppering y HMAC.

## 🚀 Despliegue rápido (100% web)
1. Crea un repositorio en GitHub llamado `streamlit-hash-demo`.
2. Añade todos los archivos de esta carpeta (usa "Upload files" en la interfaz web de GitHub).
3. Conecta con [Streamlit Cloud](https://share.streamlit.io/new).
4. Configura `st.secrets` en Streamlit Cloud:
   ```
   PEPPER = "valor_unico_pepper"
   HMAC_KEY = "clave_hmac_segura"
   ```
5. Selecciona `app.py` como punto de entrada y despliega.

## 🧩 Funcionalidades
- Hash de texto y archivos (SHA-256, SHA-1, SHA-512, BLAKE2b)
- Salting y peppering
- HMAC con clave secreta
- Comparación de hashes
- Descarga de resultados (CSV)

## 🧠 Notas educativas
- Los hashes no son reversibles.
- SHA-1 tiene colisiones conocidas.
- La sal se almacena junto al hash, pero el pepper y las claves HMAC deben mantenerse en secreto.
