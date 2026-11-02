from openai import OpenAI


client = OpenAI()

#1 백설공주 계모 페르소나 프롬프트
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


if __name__ == "__main__":
    # 여기서 사용자 메시지를 입력받고 응답을 출력한다.
    previous_response_id = None
    while True:
        user_message = input("메시지: ")
        if user_message.lower() == "exit":
            print("대화를 종료합니다.")
            break

        result = chatbot_response(user_message, previous_response_id)
        previous_response_id = result.id
        print("백설공주 계모 : ", result.output_text)