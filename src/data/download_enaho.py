"""
Script para descargar datos de ENAHO desde INEI
Autor: Fernando Ramires Pacori
"""

import requests
import os
from pathlib import Path
import zipfile

def download_enaho_data():
    """
    Descarga microdatos de ENAHO 2024 desde INEI
    """
    
    # Crear directorio si no existe
    data_dir = Path('data/raw/enaho')
    data_dir.mkdir(parents=True, exist_ok=True)
    
    print("📥 Descargando datos de ENAHO 2024...")
    print("⚠️  NOTA: Debes descargar manualmente desde:")
    print("   https://proyectos.inei.gob.pe/microdatos/")
    print("\nPasos:")
    print("1. Ir a la página de microdatos del INEI")
    print("2. Buscar 'ENAHO 2024'")
    print("3. Descargar módulos:")
    print("   - Módulo 01: Características del hogar")
    print("   - Módulo 34: Sumarias")
    print("   - Módulo 85: Programas sociales")
    print("4. Guardar archivos .zip en: data/raw/enaho/")
    print("\n5. Ejecutar este script nuevamente para descomprimir")
    
    # Verificar si hay archivos zip para descomprimir
    zip_files = list(data_dir.glob('*.zip'))
    
    if zip_files:
        print(f"\n✅ Encontrados {len(zip_files)} archivos ZIP")
        for zip_file in zip_files:
            print(f"   Descomprimiendo: {zip_file.name}")
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall(data_dir)
        print("✅ Descompresión completada!")
    else:
        print("\n⚠️  No se encontraron archivos ZIP en data/raw/enaho/")

if __name__ == "__main__":
    download_enaho_data()
