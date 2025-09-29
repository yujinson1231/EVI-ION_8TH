<?php 
//db 연결 
$db_host="localhost"; 
$db_user = "root"; 
$db_pass=""; 
$db_name="my_db"; 
$db_port = 3306; 
$conn=new mysqli($db_host, $db_user, $db_pass, $db_name, $db_port);

if($conn->connect_error){
    die("데이터베이스 연결 실패: " . $conn->connect_error); // connect_error로 수정
}

//login.html에서 POST 방식으로 보낸 데이터 받기 
$username=$_POST['username']; 
$password=$_POST['password'];

$sql = "SELECT * FROM users WHERE username = ? AND password = ? LIMIT 1";// ?는 값을 안전하게 바인딩하기 위한 자리표시자

// prepare() 호출 — SQL 템플릿을 DB에 전달하여 준비
$stmt = $conn->prepare($sql);

// prepare 실패 가능성 체크
if (!$stmt) {
    // prepare가 실패하면 에러 로그 남기고 사용자에게 일반적인 에러 알림
    die("DB 오류 (prepare 실패): " . $conn->error);
}

// bind_param: 자리표시자(?)에 실제 변수를 바인딩
// 'ss'는 두 개의 문자열(string) 타입이라는 의미 ('s' = string)
// 첫번째 ? <- $username, 두번째 ? <- $password
$stmt->bind_param('ss', $username, $password);

// 쿼리 실행하면 SQL의 ? 자리에 값이 안전하게 들어가서 실행됨
$exec_ok = $stmt->execute();
if ($exec_ok === false) {
    // 실행 실패 처리
    $stmt->close();
    $conn->close();
    die("DB 오류 (execute 실패)");
}

// 결과 저장 (num_rows 사용하려면 store_result 필요)
$stmt->store_result();

// 결과 확인 
if($stmt->num_rows > 0){ // num_rows로 수정
    //일치하는 사용자가 있으면(결과 행이 1개 이상이면)
    echo "<h1>로그인 성공!</h1>";
    echo "<p>'$username'님, 환영합니다.</p>";
}else{
    echo "<h1>로그인 실패</h1>";
    echo "<p>아이디 또는 비밀번호가 올바르지 않습니다.</p>";
    echo '<a href="login.html">다시 시도하기</a>';
}

//DB 연결 종료 
$conn->close(); 
?>

