from functools import lru_cache
from redis import Redis

from config.settings import get_settings


def create_redis_client() -> Redis:
    """Redis 클라이언트 생성"""
    settings = get_settings()
    return Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB,
        password=settings.REDIS_PASSWORD,
        decode_responses=True,
    )


@lru_cache()
def get_redis_client() -> Redis:
    """Redis 클라이언트 싱글톤 반환 (캐싱)"""
    return create_redis_client()