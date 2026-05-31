import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="InfraShield",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo personalizado
st.markdown("""
<style>
    .main-header {font-size: 2.5rem; color: #00b4d8;}
    .metric-card {background-color: #0e1117; padding: 15px; border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

# ================== DATOS DE EJEMPLO (Quito) ==================
data = {
    'Infraestructura': ['Av. Amazonas', 'Puente 6 de Diciembre', 'Calle Juan León Mera', 
                       'Vía a Mitad del Mundo', 'Puente Guayllabamba', 'Av. Mariscal Sucre'],
    'Tipo': ['Carretera', 'Puente', 'Calle', 'Carretera', 'Puente', 'Carretera'],
    'Edad_años': [12, 28, 8, 15, 35, 18],
    'PCI_actual': [78, 45, 85, 62, 32, 55],
    'Vida_Util_Restante': [4.2, 1.8, 5.5, 3.1, 0.9, 2.4],
    'Riesgo': ['Medio', 'Alto', 'Bajo', 'Medio', 'Crítico', 'Alto'],
    'Costo_Mantenimiento': [45000, 125000, 28000, 67000, 210000, 89000]
}

df = pd.DataFrame(data)

# ================== SIDEBAR ==================
st.sidebar.image("https://img.icons8.com/fluency/96/000000/shield.png", width=80)
st.sidebar.title("🛡️ InfraShield")
st.sidebar.markdown("**Sistema Predictivo de Infraestructura**")
st.sidebar.divider()

pagina = st.sidebar.selectbox("Menú Principal", 
    ["🏠 Dashboard", "🔮 Predicciones", "🗺️ Mapa", "📊 Reportes", "📈 Simulación ML"])

st.sidebar.divider()
st.sidebar.info("📍 Quito, Ecuador\n\nVersión 0.2 - Mejorada")

# ================== DASHBOARD ==================
if pagina == "🏠 Dashboard":
    st.title("🛡️ InfraShield - Dashboard")
    st.markdown("### Sistema Predictivo de Infraestructura Inteligente - Quito")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Riesgo Promedio", "Alto", "↑ 4%")
    with col2:
        st.metric("Vida Útil Promedio", "2.98 años", "↓ 0.3")
    with col3:
        st.metric("Ahorro Estimado 2026", "$2.45M", "↑ $680k")
    with col4:
        st.metric("Elementos en Riesgo", "28", "↑ 7")

    st.divider()

    colA, colB = st.columns([2, 1])
    
    with colA:
        st.subheader("Estado Actual de Infraestructuras")
        fig = px.bar(df, x='Infraestructura', y='PCI_actual', color='Riesgo',
                     color_discrete_map={'Bajo':'#00ff88', 'Medio':'#ffcc00', 'Alto':'#ff8800', 'Crítico':'#ff3333'},
                     title="Índice de Condición Pavimentaria (PCI)")
        st.plotly_chart(fig, use_container_width=True)

    with colB:
        st.subheader("Distribución de Riesgo")
        fig_pie = px.pie(df, names='Riesgo', color='Riesgo',
                        color_discrete_map={'Bajo':'#00ff88', 'Medio':'#ffcc00', 'Alto':'#ff8800', 'Crítico':'#ff3333'})
        st.plotly_chart(fig_pie, use_container_width=True)

    st.subheader("Predicción de Deterioro (Próximos 5 años)")
    years = list(range(2026, 2031))
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(x=years, y=[75, 68, 59, 48, 35], name='Av. Amazonas', mode='lines+markers'))
    fig_line.add_trace(go.Scatter(x=years, y=[45, 38, 29, 18, 8], name='Puente 6 de Diciembre', mode='lines+markers'))
    st.plotly_chart(fig_line, use_container_width=True)

# ================== PREDICCIONES ==================
elif pagina == "🔮 Predicciones":
    st.title("🔮 Nueva Predicción")
    
    infra_seleccionada = st.selectbox("Selecciona una infraestructura", df['Infraestructura'])
    fila = df[df['Infraestructura'] == infra_seleccionada].iloc[0]
    
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"**{fila['Infraestructura']}**")
        st.metric("PCI Actual", f"{fila['PCI_actual']}/100")
        st.metric("Vida Útil Restante", f"{fila['Vida_Util_Restante']} años")
    
    with col2:
        st.metric("Nivel de Riesgo", fila['Riesgo'], delta=None)
        st.metric("Costo Estimado de Reparación", f"${fila['Costo_Mantenimiento']:,}")

    st.divider()
    st.subheader("Simulación de Predicción")
    meses = st.slider("Meses hacia el futuro", 6, 60, 24)
    
    if st.button("🔮 Realizar Predicción con Modelo", type="primary"):
        # Simulación simple de ML
        deterioro = max(10, fila['PCI_actual'] - (meses * 1.1))
        st.success(f"**Predicción:** En {meses} meses el PCI bajará a **{deterioro:.1f}**")
        st.info("Recomendación: Realizar mantenimiento preventivo antes de 12 meses")

# ================== MAPA (Simulado) ==================
elif pagina == "🗺️ Mapa":
    st.title("🗺️ Mapa Predictivo - Quito")
    st.image("https://i.imgur.com/5z3vK8J.png", use_column_width=True)  # Imagen simulada
    st.warning("Mapa interactivo completo con Folium o Mapbox se agregará en la siguiente versión")

# ================== REPORTES ==================
elif pagina == "📊 Reportes":
    st.title("📊 Reportes Generales")
    st.dataframe(df.style.background_gradient(cmap='RdYlGn_r'), use_container_width=True)

# ================== SIMULACIÓN ML ==================
elif pagina == "📈 Simulación ML":
    st.title("📈 Simulación de Modelo de Machine Learning")
    st.info("Esta es una simulación de cómo funcionaría un modelo XGBoost o Random Forest")
    
    st.subheader("Factores que influyen en la predicción")
    edad = st.slider("Edad de la infraestructura (años)", 1, 50, 15)
    trafico = st.slider("Tráfico diario (vehículos)", 5000, 80000, 25000)
    lluvia = st.slider("Índice de lluvia anual", 600, 1500, 950)
    
    pci_predicho = max(10, 95 - (edad * 1.8) - (tráfico/2000) - (lluvia/50))
    
    st.metric("PCI Predicho", f"{pci_predicho:.1f}/100")
    st.progress((pci_predicho)/100)

st.caption("© 2026 InfraShield - Proyecto Predictivo de Infraestructura | Quito, Ecuador")