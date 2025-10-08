import streamlit as st
import pandas as pd
from hash_utils import hash_text, hash_file_chunked, with_salt, with_pepper, hmac_text, compare_hashes

st.set_page_config(page_title="Hash Demo", page_icon="🔐", layout="wide")

st.title("🔐 Demo educativa de funciones Hash")

# Sección 1: Hash de texto
st.header("1️⃣ Hash de texto")
text_input = st.text_area("Introduce texto:", "Hola Mundo")
algorithm = st.selectbox("Algoritmo", ['sha256', 'sha1', 'sha512', 'blake2b'])
if st.button("Calcular hash"):
    st.write(hash_text(text_input, algorithm))

# Sección 2: Hash con sal
st.header("2️⃣ Salting")
use_custom_salt = st.checkbox("Usar sal personalizada")
salt_value = st.text_input("Sal (opcional)") if use_custom_salt else None
salt, salted_text = with_salt(text_input, salt_value)
st.write("Sal:", salt)
st.write("Hash con sal:", hash_text(salted_text, algorithm))

# Sección 3: Pepper y HMAC
st.header("3️⃣ Pepper y HMAC")
if "PEPPER" in st.secrets and "HMAC_KEY" in st.secrets:
    peppered_text = with_pepper(text_input, st.secrets["PEPPER"])
    st.write("Hash con pepper:", hash_text(peppered_text, algorithm))
    st.write("HMAC:", hmac_text(text_input, st.secrets["HMAC_KEY"], algorithm))
else:
    st.warning("⚠️ Configura PEPPER y HMAC_KEY en st.secrets para activar esta sección.")

# Sección 4: Hash de archivo
st.header("4️⃣ Hash de archivo")
uploaded_file = st.file_uploader("Sube un archivo (máx 10MB)", type=None)
if uploaded_file is not None:
    if uploaded_file.size > 10 * 1024 * 1024:
        st.error("Archivo demasiado grande (>10MB).")
    else:
        uploaded_file.seek(0)
        file_hash = hash_file_chunked(uploaded_file, algorithm)
        st.write("Hash del archivo:", file_hash)

# Sección 5: Comparar hashes
st.header("5️⃣ Comparar hashes")
hash1 = st.text_input("Hash 1")
hash2 = st.text_input("Hash 2")
if st.button("Comparar"):
    result = compare_hashes(hash1.strip(), hash2.strip())
    st.write("Coinciden ✅" if result else "No coinciden ❌")

# Sección 6: Descargar resultados
st.header("6️⃣ Guardar resultados")
if st.button("Descargar CSV de ejemplo"):
    df = pd.DataFrame([{"Texto": text_input, "Algoritmo": algorithm, "Hash": hash_text(text_input, algorithm)}])
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Descargar CSV", csv, "hash_result.csv", "text/csv")
