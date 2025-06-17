# Classificador de Leads com IA 🎯

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://SEU-LINK-DO-STREAMLIT-CLOUD-VAI-AQUI)

Este é um SAAS construído com Streamlit e a API do Google Gemini para analisar e qualificar leads de vendas. A ferramenta classifica o potencial de um cliente em **Quente**, **Neutro** ou **Frio** com base nos dados fornecidos, oferecendo uma justificativa gerada por IA para auxiliar na tomada de decisão da equipe de vendas.

## 🚀 Acesso à Aplicação

Você pode testar a aplicação ao vivo no seguinte link:

**[➡️ Acessar o Classificador de Leads]([https://SEU-LINK-DO-STREAMLIT-CLOUD-VAI-AQUI](https://marcelypcosta-saas-classificador-de-leads-ia-app-pymqdf.streamlit.app/))**

## ✨ Funcionalidades Principais

* **Análise com IA Generativa:** Utiliza o modelo `gemini-1.5-flash` do Google para uma análise de alta qualidade.
* **Classificação de Leads:** Categoriza os leads em Quente, Neutro ou Frio para priorização de ações.
* **Justificativa Detalhada:** Fornece um parágrafo explicando os pontos positivos e negativos que levaram à classificação.
* **Formulários Dinâmicos:** A interface se adapta ao mercado de atuação selecionado (Imobiliário, Automobilístico, Varejo).
* **Interface Intuitiva e Responsiva:** Desenvolvido com Streamlit para uma experiência de usuário limpa e acessível em qualquer dispositivo.

## 🛠️ Tecnologias Utilizadas

* **Frontend:** [Streamlit](https://streamlit.io/)
* **IA / Backend:** [Google Generative AI (Gemini)](https://ai.google.dev/)
* **Linguagem:** Python 3
* **Deploy:** [Streamlit Community Cloud](https://streamlit.io/cloud)

## ⚙️ Configuração e Instalação Local

Para executar este projeto em sua máquina local, siga os passos abaixo.

### Pré-requisitos

* [Python 3.8+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/)
* Uma chave de API do Google Gemini ([obtenha aqui](https://aistudio.google.com/app/apikey))

### Passos para Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/marcelypcosta/SaaS-Classificador-de-Leads-IA.git
    cd SaaS-Classificador-de-Leads-IA
    ```

2.  **Crie um ambiente virtual (Recomendado):**
    ```bash
    python -m venv venv
    ```
    * No Windows:
        ```bash
        venv\Scripts\activate
        ```
    * No macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure suas chaves de API:**
    * Crie uma pasta chamada `.streamlit` na raiz do projeto.
    * Dentro dela, crie um arquivo chamado `secrets.toml`.
    * Adicione sua chave da API do Google ao arquivo, como no exemplo abaixo:
        ```toml
        # .streamlit/secrets.toml
        GOOGLE_API_KEY = "SUA_CHAVE_API_VAI_AQUI"
        ```

5.  **Execute a aplicação:**
    ```bash
    streamlit run seu_app.py
    ```
    Onde `seu_app.py` é o nome do seu arquivo principal Python.

## 🚀 Deploy

Este aplicativo foi implantado na [Streamlit Community Cloud](https://streamlit.io/cloud). O processo de deploy é contínuo e integrado ao GitHub:
1.  **Push:** Qualquer `git push` para o branch `main` aciona uma atualização automática do aplicativo.
2.  **Secrets:** As chaves de API são gerenciadas de forma segura através do painel de controle do Streamlit, na seção "Settings" > "Secrets" do aplicativo.

---

Desenvolvido por **Marcely, Lucas e Werner**
