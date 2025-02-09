import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Importação dos dados

data = pd.read_csv("data/Pedidos.csv")

df = pd.DataFrame(data)

def main():
    st.title("Dashboard de Vendas :shopping_trolley:")
    
    aba1, aba2, aba3 = st.tabs(["Dataset", "Receita", "Vendedores"])

    with aba1:
        display_dataframe(df)
    with aba2:
        display_charts(df)
    with aba3:
        display_metrics(df)

# Exibição do DataFrame
def display_dataframe(data):
    st.header("Visualização do DataFrame")
    st.sidebar.header("Filtros")
    selected_region = st.sidebar.multiselect(
        "Selecione as regiões",
        data["Regiao"].unique(),
        data["Regiao"].unique()
    )
    filtered_data = data[data["Regiao"].isin(selected_region)]
    st.write(filtered_data)


# Exibição de gráficos
def display_charts(data):
    st.header("Visualização de Gráficos")

    # Desempenho por região

    st.subheader("Desempenho por região")
    fig, ax = plt.subplots(figsize=(10, 6))  
    sns.countplot(x="Regiao", data=data, ax=ax)  
    st.pyplot(fig)

    # Itens mais vendidos

    st.subheader("Itens mais vendidos")
    fig, ax = plt.subplots(figsize=(10, 6))  
    sns.countplot(x="Item", data=data, ax=ax) 
    st.pyplot(fig)

    # Preço médio por item

    st.subheader("Preço médio por item")
    avg_price = data.groupby("Item")["PrecoUnidade"].mean().sort_values(ascending=False)
    st.write(avg_price)


# Exibição de métricas
def display_metrics(data):
    st.subheader("Métricas")

    total_sales = data["Unidades"].sum()
    average_price = data["PrecoUnidade"].mean()
    most_product = data["Vendedor"].value_counts().idxmax()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("O vendedor mais produtivo foi: ", most_product)
    with col2:
        st.metric("Vendas totais: ", total_sales)
    with col3:
        st.metric("Preço médio: ", round(average_price, 2))


# Executando o app
if __name__ == "__main__":
    main()
