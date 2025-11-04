# utils.py
import pandas as pd
import altair as alt

def plot_regresion_modelo(y_test, y_pred, nombre_modelo="Modelo"):
    """
    Genera un gráfico de dispersión y_test vs y_pred con línea ideal.
    Parámetros:
        y_test: array o Serie con valores reales
        y_pred: array o Serie con predicciones
        nombre_modelo: título del gráfico
    Retorna:
        Altair Chart listo para mostrar en Streamlit
    """
    df_dispersion = pd.DataFrame({
        "y_test": y_test,
        "y_pred": y_pred
    })

    dispersion = (
        alt.Chart(df_dispersion)
        .mark_circle(size=80, color="blue", opacity=0.6)
        .encode(
            x=alt.X("y_test:Q", title="Valores reales (LapTime)", scale=alt.Scale(domain=[65, 160])),
            y=alt.Y("y_pred:Q", title="Predicciones (LapTime)", scale=alt.Scale(domain=[65, 160])),
            tooltip=[
                alt.Tooltip("y_test:Q", title="Real", format=".2f"),
                alt.Tooltip("y_pred:Q", title="Predicho", format=".2f")
            ]
        )
        .properties(width=600, height=500)
    )

    min_val = min(df_dispersion["y_test"].min(), df_dispersion["y_pred"].min())
    max_val = max(df_dispersion["y_test"].max(), df_dispersion["y_pred"].max())
    df_linea = pd.DataFrame({"x": [min_val, max_val], "y": [min_val, max_val]})

    ideal = (
        alt.Chart(df_linea)
        .mark_line(strokeDash=[5, 5], color="red")
        .encode(x="x:Q", y="y:Q")
    )

    final_dispersion = dispersion + ideal
    final_dispersion = final_dispersion.properties(title=f"{nombre_modelo}: y_test vs y_pred")

    return final_dispersion