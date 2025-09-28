# EVI$ION_8TH
## Week 2: Flask SQL Injection 발생하는 부분 패치하기

-<이전코드>
$username=$_POST['username']; 
$password=$_POST['password'];

$sql = "SELECT * FROM users WHERE username = '$username' AND password='$password'";

이전 코드는 웹애플리케이션의 입력 필드를 통해 악의적인 SQL쿼리를 삽입하여 데이터를 조작하는 공격에 취약한 코드였음

SQL Injection을 막으려면 직접 변수값을 SQL문에 붙여 넣지 않고 준비된문(prepared statement)을 사용해야 함
Prepared Statement 사용 ($conn->prepare() + bind_param) — SQL Injection 원천 차단.

$sql = "SELECT * FROM users WHERE username = ? AND password = ? "; ,  DB 드라이버/서버는 SQL 구조와 값을 분리해서 처리하므로, 사용자가 악의적 SQL을 입력해도 쿼리 구조가 변조되지 않아 SQL Injection을 방지
