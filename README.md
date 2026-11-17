# Decision Tree vs. Random Forest

Trabajo Práctico de **Inteligencia Artificial** — 5.º Nivel, Ingeniería en Sistemas de Información — Ciclo lectivo 2026.

## Descripción

El proyecto compara un **árbol de decisión implementado por el equipo**, basado en C4.5, con **Random Forest de scikit-learn** para clasificar pacientes del conjunto UCI Heart Disease. Se analiza cómo cambian sus resultados al modificar los datos, los atributos y los parámetros de los modelos.

El notebook incluye un panel interactivo con ipywidgets para configurar las pruebas, entrenar los modelos y consultar métricas, matrices de confusión y visualizaciones. Las conclusiones principales utilizan **Cleveland con clasificación binaria** y **validación cruzada estratificada de 5 partes y 10 repeticiones**.

## Estructura del repositorio

| Carpeta / archivo | Contenido |
|---|---|
| `src/TP_IA_DT_vs_RF.ipynb` | Panel interactivo, preparación y análisis de datos, implementación del árbol, configuración de Random Forest, comparación automática y resultados documentados. |
| `data/` | Cuatro bases de UCI Heart Disease: Cleveland, Hungarian, Switzerland y VA Long Beach. |
| `results/evaluacion_minimo_hoja.csv` | Resultados registrados de 34 configuraciones, con sus parámetros, métricas, semillas y versiones de las librerías. |
| `tests/test_arbol.py` | Pruebas del mínimo de ejemplos por hoja en divisiones numéricas y categóricas, incluyendo valores faltantes. |
| `informe/main.tex` | Esqueleto de informe en LaTeX para LNCS; contiene apartados pendientes y no es el paper completo. |
| `TP-IA-2026.pdf` | Consignas del trabajo práctico. |
| `EjemploInforme.pdf` | Ejemplo de informe incluido en el repositorio. |

El paper se desarrolla en el [documento compartido de Google Docs](https://docs.google.com/document/d/1_8UZ3zgx0VWtODc3NY-_P7Tmg6hPTO2PXrFg1WSmvps/edit?tab=t.27y76tbig40u), en la pestaña **Propuesta Paper — LNCS**.

## Datos y preparación

Las cuatro bases contienen 13 atributos de pacientes y una variable objetivo que indica ausencia de enfermedad (`0`) o uno de cuatro niveles de enfermedad (`1` a `4`). El panel permite trabajar con las cinco clases originales o agruparlas en dos: **0 = sin enfermedad y 1 = con enfermedad**.

- Cleveland: `processed.cleveland.data`, con 303 pacientes.
- Hungarian: `reprocessed.hungarian.data`, que conserva las cinco clases originales.
- Switzerland: `processed.switzerland.data`.
- VA Long Beach: `processed.va.data`.

La carga reconoce `?` y, en Hungarian, `-9` como valores faltantes. También convierte en faltantes los valores de `ca` mayores que 3 y los ceros de colesterol (`chol`) y presión arterial en reposo (`trestbps`). La columna `origen` identifica la base y permite filtrarla; no se utiliza como atributo predictivo.

El árbol propio envía los casos con un valor faltante a la rama más poblada. Random Forest utiliza un pipeline que completa los faltantes con la mediana calculada sobre los datos de entrenamiento. El análisis exploratorio permite inspeccionar la calidad de las bases, la distribución de clases y los atributos.

## Ejecución

### Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amil-nicolas21/Trabajo-Practico-IA/blob/main/src/TP_IA_DT_vs_RF.ipynb)

1. Abrir el notebook mediante el enlace anterior.
2. Seleccionar **Entorno de ejecución → Ejecutar todo** y esperar a que terminen todas las celdas.
3. Volver al panel que aparece al principio del notebook.
4. Configurar las pruebas y pulsar **Ejecutar** o **Ejecutar validación cruzada**, según corresponda.

La celda de preparación clona el repositorio y carga los archivos de `data/`. En Colab también sincroniza esa copia con `origin/main` mediante `git reset --hard`; los cambios locales realizados dentro de esa copia se descartan al volver a ejecutar dicha celda.

### Ejecución local

Clonar el repositorio y entrar en su carpeta:

```shell
git clone https://github.com/amil-nicolas21/Trabajo-Practico-IA.git
cd Trabajo-Practico-IA
```

En Windows, crear un entorno e instalar las dependencias:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install numpy pandas scikit-learn ipywidgets ipykernel jupyterlab graphviz
```

Abrir `src/TP_IA_DT_vs_RF.ipynb` en VS Code, con las extensiones Python y Jupyter, y seleccionar el entorno `.venv` como kernel de Python. Otra opción es abrir JupyterLab desde la raíz del repositorio:

```powershell
.\.venv\Scripts\python.exe -m jupyter lab
```

Ejecutar todas las celdas antes de utilizar los botones del panel: aunque la interfaz aparece primero, depende de las funciones y los datos definidos más abajo.

Para dibujar el árbol también se necesita el programa Graphviz y su ejecutable `dot` disponible en `PATH`. Si no puede generar el gráfico, el notebook muestra el árbol en texto.

## Uso del panel

| Pestaña | Función |
|---|---|
| **1. Datos** | Elegir las bases, dos o cinco clases, el porcentaje de prueba y la semilla de las particiones. |
| **2. Decision Tree** | Elegir el criterio de división, la profundidad máxima, los mínimos de ejemplos para dividir y por hoja, la ganancia mínima y la visualización del árbol. |
| **3. Atributos** | Seleccionar atributos y crear atributos derivados mediante fórmulas. Permite aplicar la misma selección a Random Forest. |
| **4. Random Forest** | Elegir cantidad de árboles, profundidad máxima, criterio y cantidad de atributos considerados por división. |
| **5. Validación cruzada** | Evaluar la configuración en varias particiones y repeticiones, y guardar una referencia en memoria para comparar con otra configuración. |
| **6. Análisis de datos** | Explorar la calidad de las bases y las características de los atributos. |

La ejecución simple usa por defecto **Cleveland, dos clases, 80 % para entrenamiento, 20 % para prueba y semilla 42**. Se pueden ejecutar ambos modelos o uno solo. Cada ejecución simple reemplaza la salida anterior.

Se muestran accuracy, precisión, recall y F1 macro, además de matrices de confusión y tiempos. En los promedios macro, cada clase tiene el mismo peso. La validación cruzada muestra los promedios y la variación entre evaluaciones; la desviación estándar no representa un intervalo de confianza.

## Secciones del notebook y resultados del paper

Después del panel, las secciones 1 a 5 preparan el entorno y los datos, realizan el análisis exploratorio y definen los modelos.

La **sección 6, Evaluación y comparación**, ejecuta una comparación automática con las cuatro bases, las cinco clases originales y una separación estratificada de 70 % para entrenamiento y 30 % para prueba. Es un escenario diferente de la ejecución simple por defecto del panel y de los experimentos principales del paper.

La **sección 7, Resultados y notas para el informe**, documenta las pruebas sobre Cleveland con dos clases. Sus tablas son resultados registrados previamente: ejecutar todo el notebook no vuelve a calcularlas ni las actualiza automáticamente.

### Configuración de los resultados principales

Para evaluar las configuraciones de referencia desde el panel:

1. En **Datos**, seleccionar solo Cleveland, dos clases y semilla **0**.
2. En **Atributos**, mantener los 13 originales, sin derivados, y aplicar la misma selección a Random Forest.
3. Seleccionar **Ambos** modelos y configurar sus parámetros según la tabla siguiente.
4. En **Validación cruzada**, seleccionar **5 partes** y **10** en el control **Cantidad de semillas**, que corresponde a las repeticiones.
5. Pulsar **Ejecutar validación cruzada**. Se realizan 50 evaluaciones por modelo; el porcentaje de prueba de la ejecución simple no se utiliza en este modo.

| Parámetro | Decision Tree propio | Random Forest |
|---|---|---|
| Criterio | Razón de ganancia | Entropía |
| Profundidad máxima | 6 | 4 |
| Mínimo de ejemplos para dividir | 2 | — |
| Mínimo de ejemplos por hoja | 5 | — |
| Ganancia mínima | 0,1 | — |
| Cantidad de árboles | — | 100 |
| Atributos por división | — | Raíz cuadrada |

La semilla de Random Forest permanece en **42**, definida por `SEED` en el notebook. Los resultados registrados son:

| Modelo | Accuracy medio | F1 macro medio |
|---|---|---|
| Línea base: responder siempre la clase más frecuente | 54,1 % | 35,1 % |
| Decision Tree sin límites adicionales | 71,4 % | 71,1 % |
| Decision Tree con la configuración anterior | 77,0 % | 76,4 % |
| Random Forest de 100 árboles sin límite de profundidad | 82,5 % | 82,2 % |
| Random Forest con la configuración anterior | 83,2 % | 82,8 % |

Random Forest obtiene mayor rendimiento promedio en estas evaluaciones. Limitar el árbol propio mejora su promedio frente a dejarlo sin límites adicionales. Agregar atributos derivados no produjo mejoras confirmables: el aumento visto en el árbol sin límites no es concluyente y desaparece al regularizarlo. La selección de parámetros sobre las mismas particiones puede producir una estimación optimista del rendimiento seleccionado.

Las versiones utilizadas para los resultados registrados figuran en el CSV: NumPy **2.5.4**, pandas **3.1.0** y scikit-learn **1.9.1**. Las instrucciones de instalación anteriores no fijan versiones; para comparar mediciones, se deben considerar las versiones, los datos, los parámetros y las semillas.

La carpeta `results/` almacena resultados guardados. **El panel no exporta automáticamente sus ejecuciones a esa carpeta**, ni modifica el CSV existente.

## Implementación y pruebas

El árbol propio calcula entropía, ganancia de información y razón de ganancia. Utiliza umbrales para atributos numéricos y una rama por categoría para atributos categóricos. Controla su tamaño mediante profundidad máxima, mínimo de ejemplos y ganancia mínima. **No implementa la poda posterior de C4.5**; el tratamiento de faltantes también es una simplificación, por lo que se describe como una implementación basada en ese algoritmo.

Para ejecutar las pruebas locales desde la raíz del repositorio:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Estas pruebas comprueban las divisiones y la conservación de los ejemplos en las hojas; no recalculan los experimentos del paper.

## Equipo

- Aguirre, Amilcar.
- Benetucci, Ignacio.
- Nikcevich, Adriano.
- Desza, Joaquín.
- Rosin, Zaira.

## Referencias

- Janosi, A.; Steinbrunn, W.; Pfisterer, M.; Detrano, R.: *Heart Disease*. UCI Machine Learning Repository (1988). DOI: [10.24432/C52P4X](https://doi.org/10.24432/C52P4X).
- Detrano, R., et al.: *International application of a new probability algorithm for the diagnosis of coronary artery disease*. American Journal of Cardiology 64, 304–310 (1989).
- Quinlan, J. R.: *C4.5: Programs for Machine Learning*. Morgan Kaufmann (1993).
- Breiman, L.: *Random Forests*. Machine Learning 45, 5–32 (2001).
- Liu, B.: *Web Data Mining*. 2.ª ed. Springer (2011).
- Pedregosa, F., et al.: *Scikit-learn: Machine Learning in Python*. Journal of Machine Learning Research 12, 2825–2830 (2011).
- Nadeau, C.; Bengio, Y.: *Inference for the Generalization Error*. Machine Learning 52, 239–281 (2003). Referencia de la corrección utilizada en la comparación orientativa del panel.

## Seguimiento

[Tablero de Trello del proyecto](https://trello.com/invite/b/6ab00159ba67ed7cecc7e2c2/ATTIa04f3a8fde39c860847e5039941e9d5172C1D293/tp1iadtvsrf)
