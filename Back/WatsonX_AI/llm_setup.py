import streamlit as st
from langchain import LLMChain
from langchain.llms import IBMWatsonX
import yaml

@st.cache_resource
def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

@st.cache_resource
def get_llm():
    config = load_config()
    return IBMWatsonX(
        model_id=config["watsonx"]["model_id"],
        credentials={
            "apikey": st.secrets["WATSONX_API_KEY"],
            "url": st.secrets["WATSONX_URL"]
        },
        project_id=st.secrets["WATSONX_PROJECT_ID"],
        max_tokens=config["llm"]["max_tokens"],
        temperature=config["llm"]["temperature"]
    )

def create_chain(prompt):
    llm = get_llm()
    return LLMChain(llm=llm, prompt=prompt)