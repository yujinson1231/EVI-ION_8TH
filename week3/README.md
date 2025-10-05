# 과제1 Reversing Basic Challenge #0

이 문제는 사용자에게 문자열 입력을 받아 정해진 방법으로 입력값을 검증하여 correct 또는 wrong이 주어지며 해당 바이너리를 분석하여 correct를 출력하는 입력값을 찾는 문제이다.

- IDA를 이용하여 반환한 의사코드  

```markdown
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char v4[256]; // [rsp+20h] [rbp-118h] BYREF
  memset(v4, 0, sizeof(v4));
  sub_140001190("Input : ", argv, envp);
  sub_1400011F0("%256s", v4);
  if ( (unsigned int)sub_140001000(v4) )
    puts("Correct");
  else
    puts("Wrong");
  return 0;
}  
```
<img width="763" height="458" alt="스크린샷 2025-10-02 235934" src="https://github.com/user-attachments/assets/571226df-6dbe-41d8-ae60-b55cdb5ad379" />

<img width="981" height="199" alt="스크린샷 2025-10-02 235958" src="https://github.com/user-attachments/assets/9a817eb0-ef8c-4ab4-9964-d036adb5e9b5" />

- 풀이

sub_140001000(v4)가 true가 나오기 위해 함수 정의를 살펴봤을때
 strcmp(a1, "Compar3_the_str1ng") == 0를 반환하는 함수라서 전달받은 v4가 Compar3_the_str1ng라는 것을 알 수 있었고
이는 사용자가 입력한 문자배열이므로 입력값을 검증할 수 있었다.

# 과제2 Reversing 

#include <stdio.h>
```markdown
int main() {
    int a = 8;      // 원래는 5였던 값, 8로 변경
    int b = a - 3;  // 뺄셈 연산 추가

    if (a != b) {
        a = 0;          // FAIL 부분
    } else {
        a = a + 12;     // ADD 부분 (10에서 12로 바꿈)
    }

    printf("Result: %d\n", a);
    return 0;
}
```

## 어셈블리 흐름 (IDA에서 볼 때)

int a = 8; → MOV dword ptr [esp+1Ch], 8  

int b = a - 3; → MOV eax, [esp+1Ch] → SUB eax, 3  

if (a != b) → CMP eax,  [esp+1Ch]+ JNE FAIL  

a = a + 12; → ADD [esp+1Ch], 12  

FAIL: → MOV [esp+1Ch], 0  

마지막 → printf 호출  

## 의사코드
```markdown
int __cdecl main(int argc, const char **argv, const char **envp)
{
  __main();
  printf("Result: %d\n", 0);
  return 0;
}

int __main()
{
  int result; // eax

  result = dword_407028;
  if ( !dword_407028 )
  {
    dword_407028 = 1;
    return __do_global_ctors();
  }
  return result;
}
```

