from promptflow import tool
from langchain import LLMMathChain
import openai
from langchain.llms import AzureOpenAI
from promptflow.connections import AzureOpenAIConnection
from promptflow.core.langchain_handler import get_langchain_callback_manager

@tool
def call_llm_math(question: str, conn: AzureOpenAIConnection) -> str:
  openai.api_type = "azure"
  openai.api_version = conn.api_version
  openai.api_key = conn.api_key
  openai.api_base = conn.api_base

  llm = AzureOpenAI(temperature=0, deployment_name="text-davinci-003",openai_api_key=conn.api_key)
  callback = get_langchain_callback_manager()
  llm_math = LLMMathChain(llm=llm, verbose=True, callback_manager=callback)

  return llm_math(question)