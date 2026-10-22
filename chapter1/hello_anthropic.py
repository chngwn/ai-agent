import os
from dotenv import load_dotenv
import anthropic

#1 .env 파일에서 환경 변수 로드
load_dotenv()


#2 Anthropic API 키 가져오기
api_key = os.environ.get('ANTHROPIC_API_KEY')

client = anthropic.Anthropic()


#3 대화 기록을 저장할 리스트
conversation = []

# 사용자 입력 추가
conversation.append({"role": "user", "content": "안녕 나는 청관이야."})


#4 클로드 호출
response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=1000,
    messages=conversation
)


#5 응답 출력 및 대화 기록에 추가
assistant_message = response.content[0].text
print(assistant_message)
conversation.append({"role": "assistant", "content": assistant_message})


#6 다음 사용자 입력
conversation.append({"role": "user", "content": "내 이름이 뭐라고?"})

# 다시 클로드 호출
response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=1000,
    messages=conversation
)


#7 두 번째 응답 출력
print(response.content[0].text)