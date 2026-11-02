from openai import OpenAI

client = OpenAI()


def chatbot_response(user_message: str):
    #1 OpenAI의 gpt-5-mini 모델을 사용하여 응답 생성
    result = client.responses.create(model="gpt-5-mini", input=user_message)

    return result


if __name__ == "__main__":
    #2 사용자 메시지를 입력받고 응답을 출력한다.
    while True:
        #3 사용자에게 메시지 입력받기
        user_message = input("메시지: ")

        #4 'exit' 입력 시 대화 종료
        if user_message.lower() == "exit":
            print("대화를 종료합니다.")
            break

        #5 챗봇 응답받아오기
        result = chatbot_response(user_message)
        print("챗봇 :" + result.output_text)