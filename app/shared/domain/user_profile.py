from app.shared.domain.gender import Gender
from app.shared.domain.mbti import MBTI


class UserProfile:
    """UserProfile 값 객체 - Gender와 MBTI 조합"""

    def __init__(self, gender: Gender, mbti: MBTI):
        self._validate(gender, mbti)
        self.gender = gender
        self.mbti = mbti

    def _validate(self, gender, mbti) -> None:
        """UserProfile의 유효성을 검증한다"""
        if gender is None:
            raise ValueError("Gender는 필수입니다")

        if mbti is None:
            raise ValueError("MBTI는 필수입니다")

        if not isinstance(gender, Gender):
            raise ValueError("Gender 타입이어야 합니다")

        if not isinstance(mbti, MBTI):
            raise ValueError("MBTI 타입이어야 합니다")
