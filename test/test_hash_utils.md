# Tests manuales de verificación

## 1️⃣ Hash de texto
**Entrada:** "Hola Mundo"  
**Algoritmo:** sha256  
**Resultado esperado:** `a591a6d40bf420404a011733cfb7b190...` (similar)

## 2️⃣ Salting
**Entrada:** "Hola Mundo", Sal aleatoria  
**Resultado:** Cambia en cada ejecución.

## 3️⃣ HMAC
**Entrada:** "Hola Mundo", Clave `"clave_hmac_segura"`  
**Algoritmo:** sha256  
**Resultado:** Hash HMAC diferente del hash normal.

## 4️⃣ Comparación
**hash1 == hash2 →** ✅  
**hash1 != hash2 →** ❌
