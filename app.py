import streamlit as st
import google.generativeai as genai

# --- Configurações Iniciais ---
st.set_page_config(
    page_title="Classificador de Leads",
    page_icon="🎯",
    layout="centered"
)

# Configuração da API do Google Gemini
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception as e:
    st.error(f"Erro ao configurar a API do Google. Verifique sua chave. Detalhes: {e}")
    st.stop()


# --- Título e Seleção de Mercado ---
st.title("Classificador de Leads com IA")
st.markdown("Selecione o mercado e preencha os dados do lead para receber uma análise de potencial.")

mercado = st.selectbox(
    "Escolha o mercado de atuação:",
    ("Selecione um mercado...", "Imobiliário", "Automobilístico", "Varejo")
)

# --- Formulários Dinâmicos ---
dados_lead = {}
formulario_enviado = False

st.markdown("---")

if mercado == "Imobiliário":
    with st.form("form_imobiliario"):
        st.subheader("Dados do Lead - Mercado Imobiliário")
        dados_lead["Nome"] = st.text_input("Nome do Cliente")
        dados_lead["Renda Mensal"] = st.number_input("Renda Mensal (R$)", min_value=0, step=500)
        dados_lead["Possui Imóvel Próprio"] = st.radio("Possui Imóvel Próprio?", ("Não", "Sim"))
        dados_lead["Região de Interesse"] = st.text_input("Região de Interesse (Bairro, Cidade)")
        dados_lead["Observações"] = st.text_area("Observações Adicionais")
        formulario_enviado = st.form_submit_button("Analisar Potencial do Cliente", use_container_width=True)

elif mercado == "Automobilístico":
    with st.form("form_automobilistico"):
        st.subheader("Dados do Lead - Mercado Automobilístico")
        dados_lead["Nome"] = st.text_input("Nome do Cliente")
        dados_lead["Renda Mensal"] = st.number_input("Renda Mensal (R$)", min_value=0, step=500)
        dados_lead["Necessidade do Veículo"] = st.select_slider(
            "Qual a necessidade do veículo?",
            options=["Apenas Curiosidade", "Planejando para o Futuro", "Necessidade Urgente"]
        )
        dados_lead["Modelo de Interesse"] = st.text_input("Modelo(s) de Interesse")
        dados_lead["Observações"] = st.text_area("Observações Adicionais")
        formulario_enviado = st.form_submit_button("Analisar Potencial do Cliente", use_container_width=True)

elif mercado == "Varejo":
    with st.form("form_varejo"):
        st.subheader("🛒 Dados do Lead - Mercado de Varejo")
        dados_lead["Nome"] = st.text_input("Nome do Cliente")
        dados_lead["Frequência de Compra"] = st.number_input("Frequência de Compra (vezes por mês)", min_value=0, step=1)
        dados_lead["Categorias de Interesse"] = st.multiselect(
            "Categorias de Produtos de Interesse",
            ["Eletrônicos", "Roupas e Acessórios", "Alimentos e Bebidas", "Casa e Decoração", "Livros", "Esportes"]
        )
        dados_lead["Último Produto Comprado"] = st.text_input("Último Produto Comprado")
        dados_lead["Observações"] = st.text_area("Observações Adicionais")
        formulario_enviado = st.form_submit_button("Analisar Potencial do Cliente", use_container_width=True)


# --- Lógica da IA e Exibição do Resultado ---
if formulario_enviado:
    if not any(str(v) for v in dados_lead.values() if isinstance(v, (str, int, float)) and v not in ["Nome"]):
         st.warning("Por favor, preencha pelo menos um campo de informação do lead para análise.")
    else:
        # Construção do Prompt para a IA
        prompt = f"""
        Aja como um especialista em vendas e qualificação de leads do mercado de **{mercado}**.
        Sua tarefa é analisar os dados de um potencial cliente e classificá-lo em uma das três categorias: Quente, Neutro ou Frio.

        **Dados do Lead:**
        {chr(10).join([f"- {chave}: {valor}" for chave, valor in dados_lead.items() if valor])}

        **Instruções:**
        1.  Primeiro, determine a temperatura do lead. A resposta DEVE começar com "### Quente", "### Neutro", ou "### Frio".
        2.  Após a classificação, escreva um parágrafo conciso (entre 5 e 10 linhas) justificando sua análise. Explique os pontos positivos e negativos que te levaram a essa conclusão com base nos dados fornecidos.

        Analise os dados e forneça sua classificação e justificativa.
        """

        with st.spinner(f"Analisando o potencial de {dados_lead.get('Nome', 'lead')}..."):
            try:
                response = model.generate_content(prompt)
                st.markdown("---")
                st.subheader("Análise de Potencial")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Houve um problema ao gerar a análise. Tente novamente. Detalhes: {e}")

