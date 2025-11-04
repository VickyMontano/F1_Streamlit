
---

##  Objetivos del proyecto

- Predecir el tiempo de vuelta (`LapTime`) en base a variables técnicas y contextuales.
- Evaluar modelos base y extendidos (Linear Regression, Random Forest, Gradient Boosting).
- Validar hipótesis sobre rendimiento relativo y predicción de ganadores.
- Comunicar hallazgos mediante visualizaciones interactivas con Altair.

---

##  Modelos entrenados

- `modelo_random_forest_enriquecido.pkl`: modelo final con features extendidas.
- `modelo_regresion_lineal.pkl`: baseline para comparación.

---

##  Visualizaciones interactivas

La app incluye:

- Comparación de errores residuales entre modelos.
- Gráfico de dispersión: predicción vs valor real.
- Validación de hipótesis por evento y continente.
- Aciertos Top-1 y Top-3 por circuito.

---

##  Validación de hipótesis

> **Hipótesis principal:** Si el modelo predice bien, debería identificar correctamente la mejor vuelta en cada circuito.  
> **Hipótesis derivada:** Si el modelo captura el rendimiento relativo, el verdadero ganador debería estar entre los tres con mejor tiempo predicho.

---

##  Cómo ejecutar la app localmente

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/F1_STREAMLIT.git
   cd F1_STREAMLIT
