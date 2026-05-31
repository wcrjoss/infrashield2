import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="InfraShield", layout="wide", page_icon="🛡️")

# Título y logo
st.title("🛡️ InfraShield")
st.markdown("### Plataforma Predictiva de Infraestructura Inteligente")

# Sidebar
st.sidebar.header("Navegación")
pagina = st.sidebar.selectbox("Ir a:", 
    ["Dashboard", "Predicciones", "Mapa", "Reportes"])

# Datos de ejemplo
data = {
    'Infraestructura': ['Av. Amazonas', 'Puente 6 de Diciembre', 'Calle Juan León Mera', 
                       'Vía a Mitad del Mundo', 'Puente Guayllabamba'],
    'Tipo': ['Carretera', 'Puente', 'Calle', 'Carretera', 'Puente'],
    'Edad_años': [12, 28, 8, 15, 35],
    'PCI_actual': [78, 45, 85, 62, 32],
    'Vida_Util_Restante': [4.2, 1.8, 5.5, 3.1, 0.9],
    'Riesgo': ['Medio', 'Alto', 'Bajo', 'Medio', 'Crítico']
}

df = pd.DataFrame(data)

# Dashboard principal
if pagina == "Dashboard":
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Riesgo Promedio", "Alto", "↑ 3%")
    with col2:
        st.metric("Vida Útil Promedio", "3.1 años", "↓ 0.4")
    with col3:
        st.metric("Ahorro Estimado", "$1.85M", "↑ $420k")
    with col4:
        st.metric("Infraestructuras en Riesgo", "23", "↑ 5")
    
    st.subheader("Estado de Infraestructura en Quito")
    fig = px.bar(df, x='Infraestructura', y='PCI_actual', color='Riesgo',
                 color_discrete_map={'Bajo':'green', 'Medio':'yellow', 'Alto':'orange', 'Crítico':'red'})
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Predicción de Deterioro (Próximos 5 años)")
    years = [0, 1, 2, 3, 4, 5]
    deterioro = [75, 68, 60, 51, 41, 30]
    fig2 = px.line(x=years, y=deterioro, markers=True, title="Evolución del PCI")
    st.plotly_chart(fig2, use_container_width=True)

elif pagina == "Predicciones":
    st.header("Nueva Predicción")
    infra = st.selectbox("Selecciona infraestructura", df['Infraestructura'])
    selected = df[df['Infraestructura'] == infra].iloc[0]
    
    st.write(f"**Estado actual:** PCI = {selected['PCI_actual']}")
    st.write(f"**Vida útil restante:** {selected['Vida_Util_Restante']} años")
    st.write(f"**Nivel de Riesgo:** {selected['Riesgo']}")

# ... (puedes seguir expandiendo)

st.sidebar.info("InfraShield v0.1 - Prototipo")