from abc import ABC, abstractmethod

from app.consult.domain.consult_session import ConsultSession


class AICounselorPort(ABC):
    """AI 상담사 포트 인터페이스"""

    @abstractmethod
    def generate_response(self, session: ConsultSession, user_message: str) -> str:
        """
        사용자 메시지에 대한 AI 응답을 생성한다.

        Args:
            session: 상담 세션 (MBTI, Gender, 대화 히스토리 포함)
            user_message: 사용자가 보낸 메시지

        Returns:
            AI 응답 메시지
        """
        pass
