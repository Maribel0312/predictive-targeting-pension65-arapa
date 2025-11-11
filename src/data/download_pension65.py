"""
Script para consultar y descargar datos de Pensión 65
"""

import pandas as pd
import requests
from pathlib import Path

def download_pension65_data():
    """
    Descarga datos públicos de Pensión 65
    """
    
    data_dir = Path('data/raw/pension65')
    data_dir.mkdir(parents=True, exist_ok=True)
    
    print("📥 Descargando datos de Pensión 65...")
    
    # URL de datos abiertos del gobierno
    base_url = "https://datosabiertos.gob.pe/dataset/"
    
    print("\n📋 Fuentes de datos disponibles:")
    print("1. Portal de Datos Abiertos: https://datosabiertos.gob.pe")
    print("   Buscar: 'Pensión 65 Información de Usuarios'")
    print("\n2. Para datos de ARAPA específicamente:")
    print("   Contactar: bmadueno@pension65.gob.pe")
    print("   Solicitar: Padrón de beneficiarios distrito de Arapa")
    
    # Crear archivo de ejemplo
    ejemplo_data = {
        'departamento': ['PUNO'],
        'provincia': ['AZANGARO'],
        'distrito': ['ARAPA'],
        'total_beneficiarios': [720]
    }
    
    df_ejemplo = pd.DataFrame(ejemplo_data)
    df_ejemplo.to_csv(data_dir / 'pension65_arapa_resumen.csv', index=False)
    
    print(f"\n✅ Archivo de ejemplo creado en: {data_dir}")

if __name__ == "__main__":
    download_pension65_data()
