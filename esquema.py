import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# CONFIGURACIÓN
# =========================================================

st.set_page_config(
    page_title="Metodologías de Minería de Datos",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# ENCABEZADO
# =========================================================
       
# =========================================================
# ENCABEZADO INSTITUCIONAL
# =========================================================
st.image("logo.png", width=400)

st.markdown("""
<div style='text-align: center;'>

<h1 style='color:#0B5394;'>
Metodologías para el Proceso de Minería de Datos
</h1>

<h3>
Proyecto Comparativo
</h3>

<hr style='border:1px solid #D3D3D3;'>

<h4>
Instituto Superior Tecnológico del Azuay
</h4>

<h4>
Periodo Académico 31-2026-1P
</h4>

<h4>
Carrera de Tecnología Superior en Big Data
</h4>

</div>
""", unsafe_allow_html=True)

# =========================================================
# INFORMACIÓN ACADÉMICA
# =========================================================

col1, col2 = st.columns(2)

with col1:

    st.info("""
    ### Docente
    
    Ing. Verónica Chimbo
    """)

with col2:

    st.info("""
    ### Asignatura
    
    Minería de Datos I
    """)

# =========================================================
# DATOS DE ESTUDIANTES
# =========================================================

st.markdown("## 👨‍🎓 Datos del estudiante")
st.write("""
**Nombre:*Michelle*     
**Apellido:*Yascaribay*    
**Correo electrónico:*michelle.yascaribay.est@tecazuay.edu.ec*
""")
st.divider()    

# =========================================================
# INTRODUCCIÓN
# =========================================================

st.markdown("""
## Introducción

En este proyecto se analizarán diferentes metodologías
de minería de datos y ciencia de datos.

Los estudiantes deberán completar la información correspondiente
a cada metodología y desarrollar una pequeña aplicación práctica
utilizando datos reales.
""")

st.divider()

# =========================================================
# MENÚ LATERAL
# =========================================================

st.sidebar.title("📚 Menú")

opcion = st.sidebar.radio(
    "Seleccione una metodología",
    [
        "Inicio",
        "KDD",
        "CRISP-DM",
        "SEMMA",
        "TDSP",
        "Comparativa"
    ]
)

# =========================================================
# INICIO
# =========================================================

if opcion == "Inicio":

    st.header("Bienvenido")

    st.markdown("""
    ## Objetivo

    Analizar y comparar metodologías utilizadas
    en proyectos de minería de datos.

    ## Actividades

    ✅ Completar descripción  
    ✅ Investigar fases  
    ✅ Identificar ventajas  
    ✅ Identificar desventajas  
    ✅ Investigar empresas  
    ✅ Desarrollar aplicación práctica
    """)

# =========================================================
# KDD
# =========================================================

elif opcion == "KDD":

    st.header("Metodología KDD")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Descripción",
        "Fases",
        "Ventajas",
        "Desventajas",
        "Empresas",
        "Aplicación"
    ])

    # -----------------------------------------------------

    with tab1:

        st.subheader("Descripción")

        st.write("""
        Knowledge Discovery in Databases) es un proceso iterativo y colaborativo
que permite transformar datos en conocimiento útil mediante técnicas de
preprocesamiento, minería de datos y evaluación de resultados.
        """)

    # -----------------------------------------------------

    with tab2:

        st.subheader("Fases")

        fases = pd.DataFrame({

            "Fase": [
                "Selección",
                "Preprocesamiento",
                "Transformación",
                "Mineria de datos",
                "Evaluación",
                "Presentación del conocimiento"
            ],

            "Descripción": [
                "Se seleccionan los datos relevantes para el objetivo del proyecto",
                "Se limpian y preparan los datos para mejorar su calidad",
                "Los datos se transforman a formatos adecuados para el análisis",
                "Se aplican algoritmos para descubrir patrones y modelos.",
                "Se evalúan los resultados obtenidos para verificar su validez.",
                "Se presenta el conocimiento descubierto para apoyar la toma de decisiones."
            ]
        })

        st.dataframe(fases, use_container_width=True)

    # -----------------------------------------------------

    with tab3:

        st.subheader("Ventajas")

        st.write("""
        ✔ Descubre conocimiento oculto en los datos.
        
        ✔ Facilita la toma de decisiones
        
        ✔ Puede aplicarse en diferentes sectores
                 
        ✔ Permite identificar patrones complejos.

        ✔ Mejora el aprovechamiento de la información.
        """)

    # -----------------------------------------------------

    with tab4:

        st.subheader("Desventajas")

        st.write("""
        ✘ Requiere grandes volúmenes de datos.
        
        ✘ Consume tiempo en preparación de datos.
        
        ✘ Necesita recursos computacionales elevados.
        
        ✘ Puede generar resultados difíciles de interpretar
        """)

    # -----------------------------------------------------

    with tab5:

        st.subheader("Empresas")

        empresas = pd.DataFrame({

            "Empresa": ["Google", "Amazon", "Netflix"],
            "Uso": ["Análisis de búsquedas", "Recomendación de productos", "Recomendación de contenido"]
        })

        st.table(empresas)

    # -----------------------------------------------------

    with tab6:

        st.subheader("Aplicación Práctica - KDD")

        st.write("""
      Esta aplicación implementa las etapas de la metodología KDD
      para descubrir conocimiento útil a partir de los datos.
      """)

    # =====================================================
    # 1. SELECCIÓN DE DATOS
    # =====================================================

    st.subheader("1. Selección de Datos")

    datos = {
        "Edad": [20, 22, 25, 30, 35, 40, 28, 32, 45, 50],
        "Ingreso": [400, 500, 600, 700, 800, 900, 650, 750, 1000, 1200],
        "Compras": [0, 1, 1, 1, 0, 1, 0, 1, 1, 1]
    }

    df = pd.DataFrame(datos)

    st.success("Datos seleccionados correctamente")

    st.dataframe(df)

    # =====================================================
    # 2. PREPROCESAMIENTO
    # =====================================================

    st.subheader("2. Preprocesamiento")

    st.write("Análisis de valores nulos")

    nulos = df.isnull().sum()

    st.dataframe(nulos)

    st.write("Dimensiones del conjunto de datos:")

    st.write(df.shape)

    # =====================================================
    # 3. TRANSFORMACIÓN
    # =====================================================

    st.subheader("3. Transformación de Datos")

    df_limpio = df.dropna()

    st.success("Datos transformados correctamente")

    st.dataframe(df_limpio)

    # =====================================================
    # 4. MINERÍA DE DATOS
    # =====================================================

    st.subheader("4. Minería de Datos")

    variable = st.selectbox(
        "Seleccione una variable",
        ["Edad", "Ingreso"]
    )

    fig, ax = plt.subplots()

    df_limpio[variable].hist(ax=ax)

    ax.set_title(f"Distribución de {variable}")

    st.pyplot(fig)

    # =====================================================
    # MODELO PREDICTIVO
    # =====================================================

    st.subheader("Modelo Predictivo")

    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier

    X = df_limpio[["Edad", "Ingreso"]]

    y = df_limpio["Compras"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.30,
        random_state=42
    )

    modelo = DecisionTreeClassifier()

    modelo.fit(X_train, y_train)

    predicciones = modelo.predict(X_test)

    st.success("Modelo entrenado correctamente")

    # =====================================================
    # 5. EVALUACIÓN
    # =====================================================

    st.subheader("5. Evaluación")

    from sklearn.metrics import (
        accuracy_score,
        precision_score,
        recall_score,
        f1_score,
        confusion_matrix
    )

    accuracy = accuracy_score(y_test, predicciones)

    precision = precision_score(
        y_test,
        predicciones,
        zero_division=0
    )

    recall = recall_score(
        y_test,
        predicciones,
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        predicciones,
        zero_division=0
    )

    st.metric("Accuracy", round(accuracy, 2))
    st.metric("Precision", round(precision, 2))
    st.metric("Recall", round(recall, 2))
    st.metric("F1 Score", round(f1, 2))

    st.write("Matriz de Confusión")

    matriz = confusion_matrix(
        y_test,
        predicciones
    )

    st.dataframe(matriz)

    # =====================================================
    # 6. INTERPRETACIÓN DEL CONOCIMIENTO
    # =====================================================

    st.subheader("6. Interpretación del Conocimiento")

    st.info("""
    Resultados obtenidos mediante KDD:

    • Se seleccionó un conjunto de datos de clientes.

    • Se verificó la calidad de los datos.

    • Se transformó la información para su análisis.

    • Se identificaron patrones mediante gráficos.

    • Se construyó un modelo de clasificación.

    • Se evaluó el rendimiento del modelo.

    • El conocimiento obtenido permite predecir
      si un cliente realizará una compra en función
      de su edad e ingreso.
    """)
# =========================================================
# CRISP-DM
# =========================================================
elif opcion == "CRISP-DM":

    st.header("Metodología CRISP-DM")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Descripción",
        "Fases",
        "Ventajas",
        "Desventajas",
        "Empresas",
        "Aplicación"
    ])

    # -----------------------------------------------------

    with tab1:

        st.subheader("Descripción")

        st.write("""
        CRISP-DM (Cross Industry Standard Process for Data Mining) es una metodología estándar para proyectos de minería de datos. Está orientada al negocio y proporciona una estructura flexible para planificar, desarrollar e implementar soluciones basadas en datos.
        """)

    # -----------------------------------------------------

    with tab2:

        st.subheader("Fases")

        fases = pd.DataFrame({

            "Fase": [
                "Comprensión del Negocio",
                "Comprensión de los Datos",
                "Preparación de los Datos",
                "Modelado",
                "Evaluación",
                "Despliegue"
            ],

            "Descripción": [
                "Definición de objetivos y necesidades.",
                "Recopilación y exploración de datos",
                "Limpieza y transformación de información.",
                "Construcción de modelos analíticos.",
                "Validación de resultados obtenidos.",
                "Implementación de la solución"
            ]
        })

        st.dataframe(fases, use_container_width=True)

    # -----------------------------------------------------

    with tab3:

        st.subheader("Ventajas")

        st.write("""
        ✔  Orientada a objetivos empresariales
        
        ✔  Facilita la gestión de proyectos
        
        ✔ Promueve la mejora continua.
        """)

    # -----------------------------------------------------

    with tab4:

        st.subheader("Desventajas")

        st.write("""
        ✘  Puede requerir mucho tiempo.
        
        ✘ Necesita documentación constante.
        
        ✘ Requiere coordinación entre áreas
        """)

    # -----------------------------------------------------

    with tab5:

        st.subheader("Empresas")

        empresas = pd.DataFrame({

            "Empresa": ["IBM", "SAP", "Deloitte"],
            "Uso": ["Analítica empresarial", "Gestión de procesos", "Consultoría de datos"]
        })

        st.table(empresas)

    # -----------------------------------------------------

    with tab6:

        st.subheader("Aplicación Práctica")
        
    st.write("""
    Esta aplicación implementa las etapas de la metodología
    CRISP-DM para analizar el comportamiento de clientes.
    """)

    # =====================================================
    # 1. COMPRENSIÓN DEL NEGOCIO
    # =====================================================

    st.subheader("1. Comprensión del Negocio")

    st.info("""
    Objetivo:
    Identificar clientes fieles utilizando información
    de edad, saldo y compras realizadas.
    """)

    # =====================================================
    # 2. COMPRENSIÓN DE LOS DATOS
    # =====================================================

    datos = {
        "Edad": [18,22,25,28,30,35,40,45,50,55],
        "Saldo": [100,250,300,450,500,650,700,850,900,1200],
        "Compras": [1,2,2,3,4,4,5,6,6,8],
        "Cliente_Fiel": [0,0,0,1,1,1,1,1,1,1]
    }

    df = pd.DataFrame(datos)

    st.subheader("2. Comprensión de los Datos")

    st.dataframe(df)

    st.write("Resumen estadístico")

    st.dataframe(df.describe())

    # =====================================================
    # 3. PREPARACIÓN DE LOS DATOS
    # =====================================================

    st.subheader("3. Preparación de los Datos")

    st.write("Valores nulos")

    st.dataframe(df.isnull().sum())

    df_limpio = df.dropna()

    st.success("Datos preparados correctamente")

    # =====================================================
    # 4. MODELADO
    # =====================================================

    st.subheader("4. Modelado")

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()

    ax.scatter(
        df["Saldo"],
        df["Compras"]
    )

    ax.set_xlabel("Saldo")
    ax.set_ylabel("Compras")
    ax.set_title("Relación Saldo vs Compras")

    st.pyplot(fig)

    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier

    X = df_limpio[["Edad","Saldo","Compras"]]

    y = df_limpio["Cliente_Fiel"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.30,
        random_state=42
    )

    modelo = DecisionTreeClassifier()

    modelo.fit(
        X_train,
        y_train
    )

    pred = modelo.predict(X_test)

    # =====================================================
    # 5. EVALUACIÓN
    # =====================================================

    st.subheader("5. Evaluación")

    from sklearn.metrics import (
        accuracy_score,
        precision_score,
        recall_score,
        f1_score,
        confusion_matrix
    )

    st.write(
        "Accuracy:",
        accuracy_score(y_test,pred)
    )

    st.write(
        "Precision:",
        precision_score(
            y_test,
            pred,
            zero_division=0
        )
    )

    st.write(
        "Recall:",
        recall_score(
            y_test,
            pred,
            zero_division=0
        )
    )

    st.write(
        "F1 Score:",
        f1_score(
            y_test,
            pred,
            zero_division=0
        )
    )

    st.write("Matriz de Confusión")

    st.dataframe(
        confusion_matrix(
            y_test,
            pred
        )
    )

    # =====================================================
    # 6. DESPLIEGUE
    # =====================================================

    st.subheader("6. Despliegue")

    st.success("""
    El modelo puede utilizarse para identificar
    clientes fieles y apoyar estrategias de marketing.
    """)
            # AQUÍ COMPLETAR

# =========================================================
# SEMMA
# =========================================================

elif opcion == "SEMMA":

    st.header("Metodología SEMMA")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Descripción",
        "Fases",
        "Ventajas",
        "Desventajas",
        "Empresas",
        "Aplicación"
    ])

    # -----------------------------------------------------

    with tab1:

        st.subheader("Descripción")

        st.write("""
        SEMMA (Sample, Explore, Modify, Model, Assess) es una metodología desarrollada por SAS Institute que se enfoca en el análisis estadístico y el modelado predictivo para descubrir patrones en los datos.
        """)

    # -----------------------------------------------------

    with tab2:

        st.subheader("Fases")

        fases = pd.DataFrame({

            "Fase": [
                "Sample(Muestreo)",
                "Explore(Exploración)",
                "Modify(Modificación)",
                "Model(Modelado)",
                "Assess(Evaluación)"
            ],

            "Descripción": [
                "Selección de una muestra representativa.",
                "Exploración y comprensión de datos.",
                "Transformación y preparación de información.",
                "Construcción de modelos predictivos.",
                "Evaluación de resultados."
            ]
        })

        st.dataframe(fases, use_container_width=True)

    # -----------------------------------------------------

    with tab3:

        st.subheader("Ventajas")

        st.write("""
        ✔ Excelente para modelado predictivo.
        
        ✔ Fuerte enfoque estadístico.
        
        ✔ Optimiza el análisis de grandes conjuntos de datos.
        """)

    # -----------------------------------------------------

    with tab4:

        st.subheader("Desventajas")

        st.write("""
        ✘ Dependencia de software SAS.
        
        ✘ Menor enfoque en objetivos empresariales.
        
        ✘  Costos de licenciamiento.
        """)

    # -----------------------------------------------------

    with tab5:

        st.subheader("Empresas")

        empresas = pd.DataFrame({

            "Empresa": ["SAS Institute", "BBVA", "Mapfre"],
            "Uso": ["Analítica avanzada", "Detección de fraude", "Gestión de riesgos"]
        })

        st.table(empresas)

    # -----------------------------------------------------

    with tab6:

        st.subheader("Aplicación Práctica")
        

    st.write("""
    Esta aplicación implementa las fases de la metodología SEMMA:
    Sample, Explore, Modify, Model y Assess.
    """)

    # =====================================================
    # SAMPLE
    # =====================================================

    st.subheader("1. Sample (Muestreo)")

    datos = {
        "Edad": [18,22,25,30,35,40,45,50,28,33],
        "Salario": [400,500,600,800,1000,1200,1500,1800,700,900],
        "Visitas_Web": [5,8,10,15,20,25,30,35,12,18],
        "Compra": [0,0,1,1,1,1,1,1,0,1]
    }

    df = pd.DataFrame(datos)

    st.success("Muestra de datos seleccionada")

    st.dataframe(df)

    # =====================================================
    # EXPLORE
    # =====================================================

    st.subheader("2. Explore (Exploración)")

    st.write("Estadísticas descriptivas")

    st.dataframe(df.describe())

    variable = st.selectbox(
        "Seleccione una variable",
        ["Edad", "Salario", "Visitas_Web"],
        key="semma_graf"
    )

    fig, ax = plt.subplots()

    df[variable].hist(ax=ax)

    ax.set_title(f"Distribución de {variable}")

    st.pyplot(fig)

    # =====================================================
    # MODIFY
    # =====================================================

    st.subheader("3. Modify (Transformación)")

    df["Salario_Miles"] = df["Salario"] / 1000

    st.success(
        "Se creó la variable Salario_Miles"
    )

    st.dataframe(df)

    # =====================================================
    # MODEL
    # =====================================================

    st.subheader("4. Model (Modelado)")

    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier

    X = df[["Edad","Salario","Visitas_Web"]]

    y = df["Compra"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.30,
        random_state=42
    )

    modelo = DecisionTreeClassifier()

    modelo.fit(X_train, y_train)

    pred = modelo.predict(X_test)

    st.success("Modelo entrenado correctamente")

    # =====================================================
    # ASSESS
    # =====================================================

    st.subheader("5. Assess (Evaluación)")

    from sklearn.metrics import (
        accuracy_score,
        precision_score,
        recall_score,
        f1_score,
        confusion_matrix
    )

    st.write(
        "Accuracy:",
        accuracy_score(y_test, pred)
    )

    st.write(
        "Precision:",
        precision_score(
            y_test,
            pred,
            average="weighted",
            zero_division=0
        )
    )

    st.write(
        "Recall:",
        recall_score(
            y_test,
            pred,
            average="weighted",
            zero_division=0
        )
    )

    st.write(
        "F1 Score:",
        f1_score(
            y_test,
            pred,
            average="weighted",
            zero_division=0
        )
    )

    st.write("Matriz de Confusión")

    st.dataframe(
        confusion_matrix(
            y_test,
            pred
        )
    )

    st.info("""
    Con SEMMA se realizó:

    ✔ Sample: selección de la muestra.

    ✔ Explore: análisis exploratorio y gráficos.

    ✔ Modify: creación de nuevas variables.

    ✔ Model: entrenamiento del modelo predictivo.

    ✔ Assess: evaluación del rendimiento del modelo.
    """)

# =========================================================
# TDSP
# =========================================================

elif opcion == "TDSP":

    st.header("Metodología TDSP")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Descripción",
        "Fases",
        "Ventajas",
        "Desventajas",
        "Empresas",
        "Aplicación"
    ])

    # -----------------------------------------------------

    with tab1:

        st.subheader("Descripción")

        st.write("""
        (Team Data Science Process) es una metodología desarrollada por Microsoft
para proyectos de ciencia de datos. Facilita el trabajo colaborativo,
la construcción de modelos predictivos y el despliegue de soluciones
analíticas en entornos empresariales.
        """)

    # -----------------------------------------------------

    with tab2:

        st.subheader("Fases")

        fases = pd.DataFrame({

            "Fase": [
                "Comprensión del Negocio",
                "Adquisición y Comprensión de Datos",
                "Modelado",
                "Despliegue",
                "Aceptación del Cliente"
            ],

            "Descripción": [
                "Definir los objetivos del negocio y los criterios de éxito.",
                "Recolectar, explorar y comprender los datos disponibles",
                "Preparar los datos y construir modelos analíticos.",
                "Implementar el modelo en un entorno productivo.",
                "Validar los resultados con el cliente y verificar los objetivos"
            ]
        })

        st.dataframe(fases, use_container_width=True)

    # -----------------------------------------------------

    with tab3:

        st.subheader("Ventajas")

        st.write("""
        ✔  Facilita el trabajo colaborativo
        
        ✔  Integración con Azure y Microsoft.
        
        ✔ Ideal para proyectos de inteligencia artificial.

        """)

    # -----------------------------------------------------

    with tab4:

        st.subheader("Desventajas")

        st.write("""
        ✘ Puede resultar complejo para proyectos pequeños
        
        ✘ Curva de aprendizaje considerable.
        
        ✘ Requiere conocimientos técnicos avanzados.
        """)

    # -----------------------------------------------------

    with tab5:

        st.subheader("Empresas")

        empresas = pd.DataFrame({
        
    "Empresa": ["Microsoft", "Accenture", "EY"],
    "Uso": [
        "Inteligencia artificial",
        "Analítica avanzada",
        "Transformación digital"
    ]
})
            

        st.table(empresas)

    # -----------------------------------------------------

    with tab6:

        st.subheader("Aplicación Práctica")

    st.write("""
    Esta aplicación implementa las fases de la metodología
    Team Data Science Process (TDSP) desarrollada por Microsoft.
    """)

    # =====================================================
    # 1. COMPRENSIÓN DEL NEGOCIO
    # =====================================================

    st.subheader("1. Comprensión del Negocio")

    st.info("""
    Objetivo:
    Predecir si una campaña generará ventas altas
    utilizando datos de publicidad, visitas web y clientes.
    """)

    # =====================================================
    # 2. ADQUISICIÓN Y COMPRENSIÓN DE DATOS
    # =====================================================

    st.subheader("2. Adquisición y Comprensión de Datos")

    datos = {
        "Publicidad": [100,150,200,250,300,350,400,450,500,550],
        "Visitas_Web": [500,700,900,1200,1500,1800,2000,2300,2600,3000],
        "Clientes": [20,30,40,55,65,80,95,110,125,140],
        "Ventas_Altas": [0,0,0,0,1,1,1,1,1,1]
    }

    df = pd.DataFrame(datos)

    st.dataframe(df)

    st.write("Resumen estadístico")

    st.dataframe(df.describe())

    # =====================================================
    # 3. MODELADO
    # =====================================================

    st.subheader("3. Modelado")

    fig, ax = plt.subplots()

    ax.plot(
        df["Publicidad"],
        df["Clientes"],
        marker="o"
    )

    ax.set_title("Publicidad vs Clientes")

    st.pyplot(fig)

    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier

    X = df[["Publicidad", "Visitas_Web", "Clientes"]]

    y = df["Ventas_Altas"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.30,
        random_state=42
    )

    modelo = DecisionTreeClassifier()

    modelo.fit(X_train, y_train)

    pred = modelo.predict(X_test)

    st.success("Modelo entrenado correctamente")

    # =====================================================
    # 4. DESPLIEGUE
    # =====================================================

    st.subheader("4. Despliegue")

    nueva_publicidad = st.number_input(
        "Publicidad",
        min_value=0
    )

    nuevas_visitas = st.number_input(
        "Visitas Web",
        min_value=0
    )

    nuevos_clientes = st.number_input(
        "Clientes",
        min_value=0
    )

    if st.button("Predecir Ventas"):

        resultado = modelo.predict([[
            nueva_publicidad,
            nuevas_visitas,
            nuevos_clientes
        ]])

        if resultado[0] == 1:

            st.success("Se predicen ventas altas")

        else:

            st.warning("No se predicen ventas altas")

    # =====================================================
    # 5. ACEPTACIÓN DEL CLIENTE
    # =====================================================

    st.subheader("5. Aceptación del Cliente")

    from sklearn.metrics import (
        accuracy_score,
        precision_score,
        recall_score,
        f1_score,
        confusion_matrix
    )

    st.write(
        "Accuracy:",
        accuracy_score(y_test, pred)
    )

    st.write(
        "Precision:",
        precision_score(
            y_test,
            pred,
            zero_division=0
        )
    )

    st.write(
        "Recall:",
        recall_score(
            y_test,
            pred,
            zero_division=0
        )
    )

    st.write(
        "F1 Score:",
        f1_score(
            y_test,
            pred,
            zero_division=0
        )
    )

    st.write("Matriz de Confusión")

    st.dataframe(
        confusion_matrix(
            y_test,
            pred
        )
    )

    st.info("""
    Con TDSP se logró:

    ✔ Comprender el problema empresarial.

    ✔ Obtener y analizar los datos.

    ✔ Construir un modelo predictivo.

    ✔ Desplegar una herramienta de predicción.

    ✔ Evaluar los resultados para el cliente.
    """)

# =========================================================
# COMPARATIVA
# =========================================================

elif opcion == "Comparativa":

    st.header("Comparativa General")

    comparativa = pd.DataFrame({

        "Aspecto": [
            "Cantidad de fases",
            "Orientación",
            "Uso empresarial",
            "Nivel técnico",
            "Flexibilidad"
        ],

        "KDD": [
            "5",
            "Descubrimiento de conocimiento",
            "Alta",
            "Medio",
            "Media"
        ],

        "CRISP-DM": [
            "6",
            "Negocio y análisis",
            "Muy alta",
            "Medio",
            "Alta"
        ],

        "SEMMA": [
            "5",
            "Modelado estadístico",
            "Media",
            "Alta",
            "Media"
        ],

        "TDSP": [
            "5",
            "Ciencia de datos colaborativa",
            "Alta",
            "Alta",
            "Alta"
        ]
    })

    st.dataframe(
        comparativa,
        use_container_width=True
    )

    st.subheader("Conclusión")

    st.write("""
logías KDD, CRISP-DM, SEMMA y TDSP constituyen enfoques fundamentales para el desarrollo de proyectos de minería y ciencia de datos, ya que proporcionan una estructura organizada para transformar datos en conocimiento útil. Cada una posee características particulares: KDD se enfoca en el descubrimiento de conocimiento, CRISP-DM en la comprensión del negocio y la solución de problemas empresariales, SEMMA en el análisis estadístico y modelado predictivo, y TDSP en la colaboración y gestión integral de proyectos de ciencia de datos. A través de la comparación y las aplicaciones prácticas desarrolladas, se evidenció que todas permiten realizar procesos de selección, preparación, análisis, modelado y evaluación de datos de manera eficiente, contribuyendo a una mejor toma de decisiones. Por ello, la elección de una metodología dependerá de los objetivos del proyecto, el entorno de trabajo y las necesidades específicas de cada organización.

    """)

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Proyecto académico desarrollado con Streamlit."
)