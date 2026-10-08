# FastAPI 학습 프로젝트

[유튜브 강의](https://youtu.be/KMNeGiMceyQ?si=7Uq_3HSbE80A9g0j)를 따라 만들며 FastAPI의 기본 개념을 학습한 프로젝트입니다.
상품(Item)을 등록하고 조회, 수정, 삭제하는 간단한 REST API를 구현했습니다.

## 사용한 라이브러리

| 라이브러리 | 용도 |
| --- | --- |
| [FastAPI](https://fastapi.tiangolo.com/) | API 서버와 라우팅 구현 |
| [Pydantic](https://docs.pydantic.dev/) | 요청 데이터 모델 정의와 유효성 검사 |
| [nanoid](https://github.com/puyuan/py-nanoid) | 상품 ID 생성 |
| [HTTPie](https://httpie.io/) | 터미널에서 API 요청 테스트 |
| [Ruff](https://docs.astral.sh/ruff/) | Python 코드 린트와 포맷 검사 |
| [uv](https://docs.astral.sh/uv/) | Python 환경과 의존성 관리 |

## 학습 내용

- FastAPI 앱과 라우트 작성
- 경로 매개변수와 HTTP 메서드 사용
- Pydantic 모델과 요청 데이터 검증
- `ItemBase`와 `Item` 모델 분리
- `Enum`을 이용한 상품 색상 제한
- `HTTPException`을 이용한 404, 400 에러 처리
- HTTP 상태 코드 사용
- `nanoid`를 이용한 상품 ID 자동 생성
- CRUD API 구현

## API

| 메서드 | 경로 | 설명 |
| --- | --- | --- |
| `GET` | `/` | 서버 상태 확인 |
| `GET` | `/items/{item_id}` | 상품 조회 |
| `POST` | `/items` | 상품 등록 |
| `PUT` | `/items/{item_id}` | 상품 수정 |
| `DELETE` | `/items/{item_id}` | 상품 삭제 |

## 실행 방법

Python 3.14 이상과 [uv](https://docs.astral.sh/uv/)가 필요합니다.

```bash
uv sync
uv run fastapi dev main.py
```

서버가 실행되면 다음 주소에서 API 문서를 확인할 수 있습니다.

- Swagger UI: <http://127.0.0.1:8000/docs>
- ReDoc: <http://127.0.0.1:8000/redoc>

## 요청 예시

HTTPie를 사용하는 경우:

```bash
uv run http POST :8000/items name=ballpen color=red
uv run http GET :8000/items/gege
```

## 현재 구조

상품 데이터는 데이터베이스가 아닌 Python 딕셔너리(`temp_items`)에 저장됩니다.
따라서 서버를 재시작하면 등록하거나 수정한 데이터가 초기화됩니다.
이 프로젝트는 데이터베이스 연동 전 단계의 학습용 프로젝트입니다.