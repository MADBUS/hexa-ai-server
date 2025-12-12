"""
상담 세션 테이블에 분석 결과 컬럼 추가

실행 방법:
python migrations/add_analysis_to_consult_sessions.py
"""

from sqlalchemy import text
from config.database import engine


def migrate():
    """consult_sessions 테이블에 is_completed, analysis_json 컬럼 추가"""
    with engine.connect() as conn:
        # is_completed 컬럼 추가
        try:
            conn.execute(text("""
                ALTER TABLE consult_sessions
                ADD COLUMN is_completed BOOLEAN DEFAULT FALSE NOT NULL
            """))
            print("✅ is_completed 컬럼 추가 완료")
        except Exception as e:
            if "Duplicate column" in str(e) or "already exists" in str(e):
                print("⏭️ is_completed 컬럼이 이미 존재합니다")
            else:
                raise e

        # analysis_json 컬럼 추가
        try:
            conn.execute(text("""
                ALTER TABLE consult_sessions
                ADD COLUMN analysis_json TEXT NULL
            """))
            print("✅ analysis_json 컬럼 추가 완료")
        except Exception as e:
            if "Duplicate column" in str(e) or "already exists" in str(e):
                print("⏭️ analysis_json 컬럼이 이미 존재합니다")
            else:
                raise e

        conn.commit()
        print("✅ 마이그레이션 완료!")


if __name__ == "__main__":
    migrate()