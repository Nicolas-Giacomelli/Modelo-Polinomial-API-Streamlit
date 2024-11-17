import streamlit as st
import json
import requests

#Titulo da aplicação
st.title('Modelo de predição de Salário')

#Inputs do usuario
st.write('Quantos meses o profissional esta na empresa?')
tempo_na_empresa = st.slider("Meses",min_value=1, max_value=120,value=60,step=1)

st.write('Qual nivel do profissional na empresa?')
nivel_na_empresa = st.slider("Nivel",min_value=1,max_value=10,value=5,step=1)

#Preparar os dados pra api
input_features = {'tempo_na_empresa':tempo_na_empresa,
                  'nivel_na_empresa':nivel_na_empresa}

#Criar um botão e capturar um evento deste botão para disparar api
if st.button('Estimar Salario'):
    res = requests.post(url='http://127.0.0.1:8000/predict', data=json.dumps(input_features))
    res_json = json.loads(res.text)
    salario_em_reais = round(res_json['salario_em_reais'],2)
    st.subheader(f'O salario estimado é de R$: {salario_em_reais}')