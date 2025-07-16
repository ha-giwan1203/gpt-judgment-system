# intent_parser.py
def parse_intent(user_input):
    user_input = user_input.lower()
    intent = {
        "include_judgement": "정산" in user_input or "판단" in user_input,
        "include_reflection": "회고" in user_input,
        "include_report": "보고" in user_input or "전송" in user_input,
        "include_sorting": "정리" in user_input,
    }
    return intent
