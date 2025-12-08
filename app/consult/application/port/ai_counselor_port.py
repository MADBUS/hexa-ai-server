from abc import ABC, abstractmethod

from app.shared.vo.mbti import MBTI
from app.shared.vo.gender import Gender


class AICounselorPort(ABC):
    """AI 상담사 포트 인터페이스"""

    @abstractmethod
    def generate_greeting(self, mbti: MBTI, gender: Gender) -> str:
        """
        사용자의 MBTI와 성별에 맞는 인사말을 생성한다.

        Args:
            mbti: 사용자의 MBTI
            gender: 사용자의 성별

        Returns:
            AI가 생성한 인사말
        """
        pass