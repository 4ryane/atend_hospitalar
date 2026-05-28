#Reuso de código

import streamlit as st
from persistencia import salvar_fila_em_arquivos, carregar_fila_de_arquivo
from algoritmo import triagem_buble_s, busca_paciente

# Configuração da página
st.set_page_config(page_title="Sistema SSA - Atendimento ao Cliente", page_icon=":hospital",layout="centered")

st.title("Sistema SSA - Atendimento ao Cliente")
st.subheader("Módulo de triagem hospitalar")

# Carregar dados 
if 'fila' not in st.session_state:
    st.session_state.fila = carregar_fila_de_arquivo()

# Aba de cadastro

with st.expander("Cadastar Paciente"):
    nome = st.text_input("Nome do Paciente")
    prioridade = st.selectbox("Prioridade", options=[1,2,3,4,5], format_func=lambda x: f"{x}-{'Urgente'if x==1 else 'Leve' if x==5 else 'Moderada'}")
    sintoma = st.text_input("Sintoma")
    idade = st.number_input("idade", min_value=0, max_value=120, step=1)

if st.button("Cadastar"):
    paciente = {
        "id": len(st.session_state.fila)+1,
        "nome": nome,
        "prioridade": prioridade,
        "sintoma": sintoma,
        "idade": idade
    }
    st.session_state.fila.append(paciente)
    salvar_fila_em_arquivos(st.session_state.fila)
    st.success(f"Paciente {nome} Cadastrado com Sucesso")

# Aba de visualização

with st.expander("Ver fila (Ordenada)"):
    if not st.session_state.fila:
        st.warning("Fila de espera vazia")
    else:
        triagem_buble_s(st.session_state.fila)
        st.write("Fila de atendimento")
        for c in st.session_state.fila:
            st.write(f"Paciente {c['id']}: Prioridade: {c['prioridade']} - Nome: {c['nome']} - Sintomas: {c['sintoma']} ")
            
#Aba de busca

with st.expander("Busca Paciente"):
    nome_busca = st.text_input("Digite o nome do paciente para buscar")
    if st.button("Buscar"):
        p = busca_paciente(st.session_state.fila,nome_busca)
        if p:
            st.success(f"Encontrado ID: {p['id']} - Prioridade: {p['prioridade']} - Idade: {p['idade']}")
        else:
            st.error("Paciente não encontrado")

