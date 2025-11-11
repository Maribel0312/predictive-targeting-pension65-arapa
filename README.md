# Pension 65 - Predictive Targeting Model

Machine learning models for optimizing beneficiary targeting in Peru's Pension 65 social program.

## Project Structure

\\\
predictive-targeting-pension65-arapa/
│
├── data/
│   ├── raw/                 # Datos originales (ENAHO, SISFOH, etc.)
│   ├── processed/           # Datos limpios listos para modelado
│   ├── interim/             # Datos intermedios durante procesamiento
│   └── external/            # Datos de terceros (censo, shapefiles, etc.)
│
├── notebooks/               # Jupyter notebooks para exploración
│   ├── 01_exploratory_data_analysis.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_training.ipynb
│   └── 05_model_evaluation.ipynb
│
├── src/                     # Código fuente del proyecto
│   ├── data/                # Scripts para descarga y procesamiento
│   ├── features/            # Feature engineering
│   ├── models/              # Entrenamiento y predicción
│   └── visualization/       # Visualizaciones
│
├── models/                  # Modelos entrenados
│   ├── trained/             # Modelos serializados (.pkl, .joblib)
│   └── evaluation/          # Métricas y resultados
│
├── reports/                 # Reportes generados
│   ├── figures/             # Gráficos para publicación
│   └── tables/              # Tablas de resultados
│
├── latex/                   # Manuscrito de tesis
│   ├── main.tex
│   ├── sections/            # Capítulos
│   └── references.bib
│
├── config/                  # Archivos de configuración
│   └── config.yaml
│
├── tests/                   # Tests unitarios
│
├── requirements.txt         # Dependencias Python
├── .gitignore              # Archivos a ignorar en git
└── README.md               # Este archivo
\\\

## Setup

1. Clone the repository
2. Create virtual environment: \python -m venv venv\
3. Activate: \.\venv\Scripts\activate\
4. Install dependencies: \pip install -r requirements.txt\

## Data Sources

- ENAHO 2023-2024 (INEI)
- SISFOH Padrón General de Hogares
- Pension 65 administrative records
- Census 2017

## Author

Fernando Ramires Pacori  
Universidad Nacional del Altiplano - Puno  
Master's in Educational Informatics

## License

MIT License
