# Flask로 Reflected XSS, Stored XSS 취약점이 있는 방명록 시스템 구현

## 기능
- 메인페이지('/') : 검색 폼 + 방명록 작성 폼 + 모든 방명록 출력
- 검색 기능('/search') : 메시지 검색, 검색어를 필터링하지 않아 Reflected XSS 가능
- 방명록 작성('/write') : 이름과 메시지를 DB에 저장, 메시지를 필터링하지 않아 Stored XSS 가능

## XSS취약점
-Reflected XSS
사용자가 입력한 데이터가 서버에 저장되지 않고, 요청 시 즉시 HTML에 반영되어 브라우저에서 스크립트가 실행됨
테스트 방법: 브라우저 주소창에 <script>alert(1)</script>를 포함한 URL 입력 → 팝업 확인

-Stored XSS
사용자가 보낸 입력(예: 방명록 메시지)을 서버(DB)에 저장 → 이후 페이지 렌더링 시 저장된 스크립트가 사용자 브라우저에서 실행됨

## 실행방법
python app.py

## 파일구조
week1/
├── app.py              # Flask 애플리케이션
├── templates/
│   └── index.html      # 메인 페이지 템플릿
└── README.md           # 이 파일
