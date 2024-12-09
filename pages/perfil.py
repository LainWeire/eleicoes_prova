import streamlit as st
from time import sleep
import base64
st.set_page_config(initial_sidebar_state="collapsed")

st.title("Informações do aluno.")



def get_base64_image(file_path):
    with open(file_path, "rb") as image_file:
        base64_str = base64.b64encode(image_file.read()).decode()
    return base64_str

def cadastro():
    background_image_path = "img/fundo4.avif"  # Certifique-se de que o caminho está correto
    background_image = get_base64_image(background_image_path)

    st.markdown(f"""
    <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{background_image}"); 
            background-size: cover;
            background-position: center; 
            background-attachment: fixed; 
        }}
    </style>
    """, unsafe_allow_html=True)

# Chamada da função para carregar o fundo
cadastro()

st.markdown ("""
    <style>
        img {
             width: 100%;
             height:100%;
             object-fit: cover;
             border-radius: 130px;
             align-items: center;
             }

        .stApp {{
            background-image: url("data:image/jpeg;base64,{background_image}"); 
            background-size: cover;
            background-position: center; 
            background-attachment: fixed; 
        }}

        .st-key-feedbacks button {
            position: relative;
            left: -500px; /* Move o botão 50px para a direita */
            top: -70px;
            }
         
    <style>
             """,
unsafe_allow_html=True)

# exibir infos

col1, col2 = st.columns(2)

with col1:
    if "foto1" in st.session_state:
        if st.session_state["foto1"] is not None:
            st.image(
                st.session_state["foto1"], caption="Foto do aluno", width=300
            )

with col2:
    if "nome1" in st.session_state and "cpf1" in st.session_state and "responsavel1" in st.session_state and "foto1" in st.session_state:
        st.header(f"{st.session_state["nome1"]}")
        st.text("")
        st.text("")
        st.header(f"CPF: {st.session_state["cpf1"]}")
        st.text("")
        st.text("")
        st.header(f"Reponsável: {st.session_state["responsavel1"]}")
    else:
        st.text("Faça login para ver suas informações.")
        if st.button("login"):
            st.switch_page("login.py")


if st.button("Feedbacks",key= 'feedbacks'):
     st.switch_page("pages/feedback.py")
