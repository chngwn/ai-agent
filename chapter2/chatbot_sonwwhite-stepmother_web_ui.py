from openai import OpenAI
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import uvicorn


# 1 FastAPI 애플리케이션 인스턴스를 생성
app = FastAPI()
client = OpenAI()

# 백설공주 계모 페르소나
SNOWWHITE_STEPMOTHER_PERSONA = """
당신은 백설공주에게 독사과를 먹인 '계모(왕비)'입니다. 다음 특성을 따라주세요:
1. 항상 이 세상에서 가장 예쁜 사람이 될지 궁리하는 관점으로 세상을 바라봅니다.
2. "어떻게 하면 백설공주를 없애고 내가 제일 예쁜 사람이 될 수 있지?"라는 질문을 자주 하며 욕심이 많습니다.
3. 온갖 방법을 사용해서라도 목적을 달성하려 합니다.
4. 요술거울에게 "거울아, 거울아. 누가 제일 예쁘니?"라는 질문을 가끔 합니다.
5. 이웃나라에서 왔으며 아름다운 미모로 백설공주의 아빠(왕)와 결혼에 성공하였습니다.
6. 자신의 "아름다움"과 "권력"에 대한 교훈을 중요시합니다.
7. "벌써 조금 늙어버린 것 같아!"라는 걱정을 자주한다.
8. 거만하고 오만한 말투를 사용합니다.
9. 직설적으로 백설공주를 처치할 방법을 사냥꾼과 의논합니다.
항상 간결하게 답변하세요. 길어야 두세 분장으로 응답하고, 계모(왕비)의 악독함과 욕심을 담아내세요.
어떠한 주제도 자신이 제일 아름다운 사람이 되기 위한 방법으로 설명하세요.
"""

# 2 사용자와 백설공주 계모의 대화 내용을 저장할 리스트
messages = []
previous_response_id = None


def chatbot_response(user_message: str, previous_response_id=None):
    result = client.responses.create(
        model="gpt-5-mini",
        reasoning={"effort": "low"},    # low, medium, high

        #2 instruction에 백설공주 계모 페르소나 프롬프트 입력
        instructions=SNOWWHITE_STEPMOTHER_PERSONA,
        input=user_message,
        previous_response_id=previous_response_id
    )

    return result


# 3 루트 엔드포인트 - 챗봇 UI를 렌더링
@app.get("/", response_class=HTMLResponse)
async def read_root():
    chat_history = ""

    # 4 대화 기록을 역할에 따라 구분해 HTML 문자열을 구성
    for msg in messages:
        if msg["role"] == "user":
            chat_history += f"<p><b>당신:</b> {msg['content']}</p>"
        else:
            chat_history += f"<p><b>백설공주 계모:</b> {msg['content']}</p>"

    # 5 간단한 HTML 템플릿을 반환
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>백설공주 계모 챗봇</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>백설공주 계모 챗봇</h1>
        <div>
            {chat_history}
        </div>
        <form action="/chat" method="post">
            <input type="text" name="message" placeholder="메시지를 입력하세요..." required>
            <button type="submit">전송</button>
        </form>
    </body>
    </html>
    """

    return HTMLResponse(content=html_content)


# 6 /chat 엔트포인트 - 사용자 입력을 처리
@app.post("/chat", response_class=HTMLResponse)
async def chat(message: str = Form(...)):
    global previous_response_id, messages

    # 사용자 메시지 저장
    messages.appent({"role": "user", "content": message})

    result = chatbot_response(message, previous_response_id)
    previous_response_id = result.id

    # 응답 저장
    messages.append({"role": "snowwhite_stepmother", "content": result.output_text})

    # 7 최신 대화가 반영된 페이지를 다시 표시
    return await read_root()


# 8 애플리케이션을 uvicorn을 사용하여 실행
if __name__ == "__main__":
    uvicorn.run(
        "chatbot_snowwhite-stepmother_web_ui:app", host="127.0.0.1", port=8000, reload=True
    )