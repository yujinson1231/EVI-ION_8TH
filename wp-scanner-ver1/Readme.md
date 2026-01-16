1. 기술 스택 및 환경
사용 기술
Docker / Docker Desktop
Python 3.11
정규식 기반 PHP 정적 분석
(확장 가능성 고려) tree-sitter 구조 파서


2. 디렉터리 구조
wp-scanner-ver1/

├─ Dockerfile 

├─ Readme - 이 파일

├─ requirements.txt

├─ scanner_broken_access_control.py

├─ analyzer.py 

└─ plugins/ 

       └─ vulnerable-plugin/ 
       
              └─ vuln.php 

​

3. 함수 기능 및 설명
(1) scanner_broken_access_control.py
scan_plugins()  : /app/plugins 하위 디렉터리 목록 획득하여 각 디렉터리를 하나의 플러그인으로 하여 php 파일 분석하여 결과를 json 형태로 출력

(2) Dockerfile
Python 3.11 기반의 경량(Linux slim) 이미지 사용, WordPress 플러그인 스캐너는 Python으로 작성됨
WORKDIR /app  : 컨테이너 내부에서 작업이 이루어질 기본 디렉터리 설정
스캐너 실행 시 필요한 디렉터리 생성
의존성 목록 파일, 파이썬 패키지  복사, 프로젝트 전체 파일 복사
컨테이너 실행 시 python scanner_broken_access_control.py 실행​

(3) analyzer.py
analyze_php_file(path, plugin_name)  : 단일 PHP 파일을 대상으로 WordPress AJAX / POST 핸들러를 분석하여
권한 검증 누락(Broken Access Control) 가능성을 탐지

탐지 대상:

    - add_action('wp_ajax_*', 'callback')

    - add_action('admin_post_*', 'callback')

탐지 방식:

    - 정규식을 이용한 정적 분석 (regex-based static analysis)

    - 콜백 함수 정의 존재 여부 확인

    - current_user_can() / user_can() 호출 여부 확인

Risk / Confidence 기준
risk: 실제 악용 시 관리자 권한 기능 수행 가능
confidence: 정규식 기반 탐지->false positive 가능

​

4. Docker 기반 실행 환경

실행 명령
docker build -t wp-scanner-ver1.  

docker run --rm wp-scanner-ver1


5. vulnerable-plugin/vuln.php 예제

먼저 분석 대상은 의도적으로 취약한 플러그인이다.
wp_ajax_update_setting은 로그인 사용자라면 호출 가능
current_user_can('manage_options') 등 권한 검증이 전혀 없음
관리자 설정값(siteurl) 변경 가능

-실행 결과

<img width="652" height="378" alt="vuln php 결과" src="https://github.com/user-attachments/assets/d104e79e-c637-4b88-80c6-1d9e3893e7aa" />

관리자 기능에 대한 권한 검증 누락 탐지 성공
위험도 High → 실제 공격 시 영향도 큼
신뢰도 Medium → 정적 분석 특성상 구조 분석 미완전(추후에 확장 버전으로 confidence = High로 바꾸고자 함)

​

