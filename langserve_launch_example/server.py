from fastapi import FastAPI
from langserve import add_routes

import os
from langchain.chains import LLMChain

from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_id = os.environ['HUGGINGFACEHUB_REPO_ID']
tokenizer = AutoTokenizer.from_pretrained(model_id, device_map="auto")
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
hf = HuggingFacePipeline(pipeline=pipe)

app = FastAPI(title="LangServe Launch Example")

add_routes(app, hf)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
