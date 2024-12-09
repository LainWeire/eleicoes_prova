import streamlit as st
import time
import pandas as pd 
from time import sleep
import webbrowser

st.set_page_config(initial_sidebar_state="collapsed")

df = pd.read_csv("dados12.csv")
candidatos = df['Candidatos'].tolist()
votos = df['Votos'].tolist()

plt.bar(candidatos, votos)
plt.xlabel('Candidatos')
plt.ylabel('Votos')

plt.title('Resultado das Eleições')


st.title("Resultado dos votos")

st.text("")
st.text("")
st.text("")

def count_down(ts):
    placeholder = st.empty()  # Espaço dinâmico para exibir o tempo
    while ts > 0:
        hours, remainder = divmod(ts, 3600)  # Converte segundos em horas e o restante
        mins, secs = divmod(remainder, 60)  # Converte o restante em minutos e segundos
        horas_agora = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)  # Formato HH:MM:SS
        placeholder.text(horas_agora)  # Atualiza o texto no Streamlit
        time.sleep(1)
        ts -= 1
    st.pyplot(plt.gcf())

# Defina o horário alvo (data e hora específicas)
target_datetime = datetime(2024, 12, 7, 11, 32, 30)
now = datetime.now()  # Hora atual
time_remaining = int((target_datetime - now).total_seconds())  # Diferença em segundos

# Se o tempo restante for maior que 0, iniciar a contagem
if time_remaining > 0:
    count_down(time_remaining)
else:
    st.text("O resultado já saiu!!")
    st.text("Confira os resultados no gráfico abaixo:")
    st.pyplot(plt.gcf())

import base64

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

        .st-key-perfil button 
            position: relative;
            left: -500px; /* Move o botão 50px para a direita */
            top: -100px;
            

        .st-key-feedbacks button 
            position: relative;
            left: -500px; /* Move o botão 50px para a direita */
            top: -100px;
         
        }}
    </style>
    """, unsafe_allow_html=True)

# Chamada da função para carregar o fundo
cadastro()

if st.button("Perfil do aluno",key= 'perfil'):
     st.switch_page("pages/perfil.py")

if st.button("Feedbacks",key= 'feedbacks'):
     st.switch_page("pages/feedback.py")
