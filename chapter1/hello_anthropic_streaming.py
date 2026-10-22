import os
import anthropic
import rich

# Anthropic API 키 가져오기
api_key = os.environ.get('ANTHROPIC_API_KEY')

client = anthropic.Anthropic()

prompt = "anthropic 발음은 앤트로픽이 맞나요? 앤스로픽이 맞나요?"

with client.messages.stream(    #1 컨텍스트 매니저를 사용한 스트리밍 세션 생성
    max_tokens=1024,
    messages=[{"role": "user", "content": prompt}],
    model="claude-haiku-5-5",
) as stream:
    for event in stream:
        if event.type == "text":    #2 텍스트 타입 이벤트만 처리
            print(event.text, end="")
    print()
    #3 최종 응답 출력
    rich.print(stream.get_final_message())