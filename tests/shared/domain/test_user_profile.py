import pytest
from app.shared.domain.user_profile import UserProfile
from app.shared.domain.gender import Gender
from app.shared.domain.mbti import MBTI


def test_user_profile_creates_with_valid_gender_and_mbti():
    """유효한 Gender와 MBTI로 UserProfile을 생성할 수 있다"""
    # Given: 유효한 Gender와 MBTI 객체
    gender = Gender("MALE")
    mbti = MBTI("INTJ")

    # When: UserProfile 객체를 생성하면
    profile = UserProfile(gender=gender, mbti=mbti)

    # Then: 정상적으로 생성되고 값을 조회할 수 있다
    assert profile.gender == gender
    assert profile.mbti == mbti
    assert profile.gender.value == "MALE"
    assert profile.mbti.value == "INTJ"


def test_user_profile_rejects_none_gender():
    """Gender가 None이면 생성을 거부한다"""
    # Given: None인 Gender
    mbti = MBTI("INTJ")

    # When & Then: UserProfile 생성 시 ValueError가 발생한다
    with pytest.raises(ValueError, match="Gender는 필수입니다"):
        UserProfile(gender=None, mbti=mbti)


def test_user_profile_rejects_none_mbti():
    """MBTI가 None이면 생성을 거부한다"""
    # Given: None인 MBTI
    gender = Gender("FEMALE")

    # When & Then: UserProfile 생성 시 ValueError가 발생한다
    with pytest.raises(ValueError, match="MBTI는 필수입니다"):
        UserProfile(gender=gender, mbti=None)


def test_user_profile_rejects_invalid_gender_type():
    """Gender 타입이 아니면 생성을 거부한다"""
    # Given: 잘못된 타입의 gender
    mbti = MBTI("INTJ")

    # When & Then: UserProfile 생성 시 ValueError가 발생한다
    with pytest.raises(ValueError, match="Gender 타입이어야 합니다"):
        UserProfile(gender="MALE", mbti=mbti)


def test_user_profile_rejects_invalid_mbti_type():
    """MBTI 타입이 아니면 생성을 거부한다"""
    # Given: 잘못된 타입의 mbti
    gender = Gender("MALE")

    # When & Then: UserProfile 생성 시 ValueError가 발생한다
    with pytest.raises(ValueError, match="MBTI 타입이어야 합니다"):
        UserProfile(gender=gender, mbti="INTJ")
