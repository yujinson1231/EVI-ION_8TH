# Reversing Basic Challenge #0

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


- 풀이

sub_140001000(v4)가 true가 나오기 위해 함수 정의를 살펴봤을때
 strcmp(a1, "Compar3_the_str1ng") == 0를 반환하는 함수라서 전달받은 v4가 Compar3_the_str1ng라는 것을 알 수 있었고
이는 사용자가 입력한 문자배열이므로 입력값을 검증할 수 있었다.

