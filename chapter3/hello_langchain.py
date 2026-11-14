from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-5-mini", model_provider="openai")  # 1 LLM 초기화
result = model.invoke("랭체인이 뭔가요?")   # 2 모델 실행
print(type(result))     # 3 AIMessage 타입
print(result.content)   # 4 결괏값