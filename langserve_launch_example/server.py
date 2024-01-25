from fastapi import FastAPI
from langserve import add_routes

import os
from langchain_community.llms import HuggingFaceHub
from langchain_community.chat_models.huggingface import ChatHuggingFace

llm = HuggingFaceHub(repo_id=os.environ['HUGGINGFACEHUB_REPO_ID'])
model = ChatHuggingFace(llm=llm)
app = FastAPI(title="LangServe Launch Example")

add_routes(app, model)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
