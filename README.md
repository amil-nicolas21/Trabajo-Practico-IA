# Decision Tree vs. Random Forest

Trabajo Práctico de **Inteligencia Artificial** – 5º Nivel, Ingeniería en Sistemas de Información – Ciclo lectivo 2026.

## Descripción

El proyecto implementa desde cero el algoritmo **Decision Tree (DT)**, basado en C4.5 (Quinlan), y lo compara con el modelo de ensamble **Random Forest (RF)** de Scikit-learn en problemas de clasificación. Se evalúa el rendimiento de ambos modelos con distintas métricas (accuracy, precision, recall, F1, matriz de confusión, tiempos) al variar sus hiperparámetros.

El notebook incluye una interfaz interactiva (ipywidgets) que permite configurar los modelos, ejecutar pruebas y ver los resultados sin tocar el código.

## Objetivos

1. Implementar el algoritmo DT de forma íntegra.
2. Comparar el DT implementado con RF en rendimiento.
3. Elaborar un informe completo con las pruebas realizadas.

## Contenido

| Carpeta / archivo | Descripción |
|---|---|
| `notebook/TP_IA_DT_vs_RF.ipynb` | Notebook principal (Google Colab) |
| `src/` | Implementación del Decision Tree propio |
| `data/` | Dataset indicado por la cátedra |
| `results/` | Tablas y gráficos de los experimentos |
| `informe/` | Informe en formato LNCS |

## Cómo ejecutarlo

1. Abrir el notebook en Google Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amil-nicolas21/Trabajo-Practico-IA/blob/main/Untitled0.ipynb)
2. Ejecutar la primera celda para instalar dependencias.
3. Ejecutar *Runtime → Run all*.
4. Usar el panel interactivo para elegir modelo, parámetros y partición.

## Tecnologías

Python · NumPy · pandas · scikit-learn · matplotlib · ipywidgets · Google Colab

## Seguimiento

Tablero de Trello: [enlace]

## Equipo

- Integrante 1
- Integrante 2
- Integrante 3

## Referencias

- Liu, B. *Web Data Mining*, 2nd ed. Springer.
- Breiman, L. *Random Forests*. Machine Learning 45, 5–32 (2001).
