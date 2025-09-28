# Flask 웹 관련 모듈 import
from flask import Flask, render_template, request  # Flask 앱 생성, HTML 렌더링, HTTP 요청 처리
import sqlite3  # SQLite 데이터베이스 연동

# Flask 앱 객체 생성
app = Flask(__name__)

# SQLite 데이터베이스 파일 경로 지정
DATABASE = 'messages.db'

# DB 연결 함수
def get_db(): #SQLite 데이터베이스에 연결하여 Connection 객체를 반환 매번 DB 연결 시 사용
    conn = sqlite3.connect(DATABASE)  # DB 파일 연결(세션을 만듦)
    return conn  # 연결 객체 반환

# DB 초기화 함수
def init_db():
    conn = get_db()  # DB 연결
    cur = conn.cursor()  # 커서 객체 생성(명령을 보내고 결과를 읽는 작업자 기능을 하는 객체)
    """ #멀티라인 문자열로 여러줄의 주석을 보기 편하게 달때 유용
    messages 테이블이 없으면 생성
    id: 자동 증가 기본키
    name: 작성자 이름
    message: 방명록 내용
    """
    # 테이블 생성 (이미 존재하면 생성하지 않음)
    cur.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()  # 변경 사항 저장
    conn.close()  # DB 연결 종료

# 메인페이지 라우트
@app.route('/')
def index():
    """
    메인 페이지
    - 방명록 작성 폼
    - 검색 폼
    - 모든 방명록 출력
    """
    conn = get_db()  # DB 연결
    cur = conn.cursor()  # 커서 객체
    cur.execute("SELECT * FROM messages")  # 모든 메시지 조회()
    messages = cur.fetchall()  # 결과 가져오기
    conn.close()  # DB 연결 종료
    # index.html 템플릿 렌더링, messages 전달
    return render_template('index.html', messages=messages)#가져온 결과 보려면 massage적어주기

app.py
# 검색 기능 라우트
@app.route('/search')
def search():
    """
    검색 기능
    GET 방식으로 query string 'q'를 받아 메시지를 검색
    Reflected XSS 취약점 존재: 입력값 필터링하지 않고 HTML 출력
    """
    query = request.args.get('q', '')  # GET 파라미터 'q' 가져오기, 없으면 빈 문자열
    return f"검색결과: {query}"

# 방명록 작성 라우트
@app.route('/write', methods=['POST'])
def write():
    """
    방명록 작성 기능
    POST 방식으로 이름과 메시지 받아 DB 저장
    Stored XSS 취약점 존재: 메시지를 필터링하지 않고 출력
    """
    # 폼 데이터 가져오기
    name = request.form.get('name', '')  # 작성자 이름
    message = request.form.get('message', '')  # 메시지 내용

    conn = get_db()  # DB 연결
    cur = conn.cursor()  # 커서 생성
    # DB에 데이터 삽입, SQL Injection 방지 위해 ? 사용
    cur.execute("INSERT INTO messages (name, message) VALUES (?, ?)", (name, message))
    conn.commit()  # 변경 사항 저장
    conn.close()  # DB 연결 종료

    # 작성 후 메인페이지로 이동 (모든 방명록 출력)
    return index()  #  

# Flask 서버 실행
if __name__ == '__main__':
    init_db()  # 서버 시작 전에 DB 초기화
    app.run(debug=True)  # 디버그 모드로 서버 실행 (자동 재시작, 에러 상세 표시)