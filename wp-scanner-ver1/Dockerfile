# Python 기반 이미지
FROM python:3.11-slim

# 컨테이너 내부 작업 디렉토리
WORKDIR /app

# 필요한 디렉토리 생성
RUN mkdir -p /app/plugins /app/build

# 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 전체 코드 복사
COPY . .

# 컨테이너 실행 시 BAC 스캐너 실행
CMD ["python", "scanner_broken_access_control.py"]
