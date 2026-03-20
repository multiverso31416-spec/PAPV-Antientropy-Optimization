# ==========================================
# PAPV-01: KERNEL DE ESTABILIDAD
# NODO: MAR DE COBO / ARQUITECTO: F. FAULHABER
# ==========================================

import os

def ejecutar_limpieza_antientropica(directorio="."):
    print("--- Iniciando Escaneo del Nodo ---")
    # Filtro de paso bajo: identificamos archivos de ruido (temporales)
    ruido = ['.tmp', '.log', '.old', '.bak']
    contador = 0
    
    for archivo in os.listdir(directorio):
        if any(archivo.endswith(ext) for ext in ruido):
            try:
                os.remove(os.path.join(directorio, archivo))
                print(f"Entropía removida: {archivo}")
                contador += 1
            except:
                pass
                
    print(f"Proceso completo. {contador} unidades de ruido eliminadas.")
    print("Estado del Nodo: SINÉRGICO")

if __name__ == "__main__":
    ejecutar_limpieza_antientropica()
