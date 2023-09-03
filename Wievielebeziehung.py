import streamlit as st
import pandas as pd
import altair as alt

st.header("Wie viele Beziehungen hatten Sie bereits?")
st.subheader("Männer")

source = pd.DataFrame({
        'Anteil (%)': [7.7, 17, 16.8, 20.1, 13.5, 9.6, 4.7, 3.2, 1.6, 0.7],
        'Anzahl von Beziehungen': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
})
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil (%):Q',
        x='Anzahl von Beziehungen:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    2022
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Statista Research Department")