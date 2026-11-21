import random
from langchain.chat_models import init_chat_model

if random.random() < 0.5:   #1 50%의 확률로 gpt-5-mini를 선택
    print("gpt-5-mini selected")
    model = init_chat_model("gpt-5-mini", model_provider="openai")

else:
    print("claude-sonnet-4-20250514 selected")
    model = init_chat_model("claude-sonnet-4-20250514", model_provider="anthropic") #2 모델 생성

result = model.invoke("RAG가 뭔가요?")
print(result.content)