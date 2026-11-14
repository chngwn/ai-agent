from langchain.chat_models import init_chat_model

model = init_chat_model("claude-sonnet-5-5", model_provider="anthropic") # 1 모델 초기화
result = model.invoke("랭체인이 뭔가요?")
print(result.content)