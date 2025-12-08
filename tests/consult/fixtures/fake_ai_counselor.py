from app.consult.application.port.ai_counselor_port import AICounselorPort
from app.consult.domain.consult_session import ConsultSession


class FakeAICounselor(AICounselorPort):
    """테스트용 Fake AI 상담사"""

    def __init__(self, response: str = "AI 응답입니다"):
        self._response = response

    def generate_response(self, session: ConsultSession, user_message: str) -> str:
        return self._response

    def set_response(self, response: str) -> None:
        """테스트용: 응답 설정"""
        self._response = response
