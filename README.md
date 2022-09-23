<h1>JAVASCRIPT 기초문법</h1>

<변수 선원 키워드>

conset
let
var a,b,c;   (a,b,c라는 변수를 선언) -> var 키워드는 존재한다는 것만 이햐, 사용X


a = 10  ;
conset a = 10 ;    -> (a를 10으로 초기화는 2가지 방식)

conset naem = prompt("이름입력");
console.log(name, "님 안녕하세요"); -> (name이라는 변수는 prompt를 통해 이름을 받아고 console에 나타냄)

number 자료형 -> 숫자
string 자료형 -> 문자
boolean 자료형 -> true, false



conset a = 1
console.log(a,typeof(a));  ->  a라는 변수의 값과 자료형을 알 수 있다

javascript에서는 정수와 실수를 따로 구분 X
모두 number라는 자료형 이용

prompt로 입력된 숫자는 문자형으로 인식함

parsint   정수저장
parsfloat 실수저장

syntaxError -> 잘못된 문법이라서 발생하는 error


Escape Character   -> \  따옴표와 쌍따옴표를 사용 가능  
  conset a= "이렇게 \'사용이\' 가능"    -> 결과) 이렇게 '사용이' 가능
      < "\" 문자를 사용하고 싶다면 -> "\\" 쓰면된다

New line character  ->  \n 줄 바꾸기

object <객체>

<객체 접근 방법>

.다른 언어에서의 dictionary

conset man = { name:"김승재", age:25}

1, man.name  
2, man["name"] (대괄호를 사용할 경우 속성의 이름을 문자열로)
    
    키값을 my-name과 같이 사용하는 경우 (대쉬나 스페이스를 사용했을 경우 따옴표를 써야함)
    ->'my-name'
    
    참조 방법
    ->man['my-name']

undefined 와 null -> 값이 없다

undefined -> 정의하지 않은 변수, 속성
null -> null이라는 값이 없음을 의미하는 값을 지정한 것

<NaN>
  not a number
![chrome_4TD3TKqWfV](https://user-images.githubusercontent.com/113837393/191903120-70a60f80-7cbc-418c-bf61-0475d88e95c2.png)




-산술연산자

Arithmetic 산술 (산수 계산을 하는)
Operator 연산자 (게산하라는 기호)

math.pow(2,3); = 8 -> 2의 3승
math.sqrt(16); = 4 -> 제곱
math.readom(); -> 0과 1사이의 난수


function solution(a,b){
    conset sum = a+b
    console.log(sum);
    return sum;   
}

solution(a=1,b=2);


function solution(a,b){
    conset sum = a+b
    return sum;
}

console.log(solution(a=1,b=2));




관계연산자, 논리연산자
 
AND연산 &&
OR연산 ||

자바스크립트는 자동 형변환 기능을 가졌기 때문에 버그를 만든다.
===, !== 사용하기



