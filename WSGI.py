# 파이썬을 위한 웹프로그램의 통신 규약

# 웹프로그램은 사용자가 보낸 요청과 요청을 처리한 결과를 웹서버를 경유해서 주고받는다.
# 이때 웹서버와 웹프로그램간의 메시지를 주고 받기위한 약속이 필요한데 이약속을 CGI규약이라고 한다.

# CGI(Common Gateway Interface) : CGI 프로그래밍을 하기위한 언어는 환경변수나 표준 입출력을
#           다룰수 있는 언어라면 모두 사용가능하지만, 실행 속도나 개발 편의성을 고려하여 2000년대 초
#           까지는 대부분 펄(Perl) 언어를 사용하였다.

# 소스 코드의 보안성을 위해 C, C++, 델파이와 같은 언어를 사용하는 경우도 있는데, 이 언어들은
#           웹에 특화된 언어가 아니기에 유지보수나 프로그램작성에 어려움이 있다.


# 파이썬은 cgi모듈을 통해 CGI 환경변수와 CGI 표준 입출력 에 직접 액세스해서 웹프로그램을 작성할 수
# 있다.

# 웹프로그램은 웹서버와는 독립적이어야 하는데 파이썬은 WSGI 표준을 지켜 이독립성을 구현해준다.
# ( WSGI 표준을 따르면 웹서버의 종류와는 상관없이 동작이 된다.)

# ** Flask는 Werkzeug(벡자이그)기반으로 작성된다.
# 벡자이그는 WSGI 코어와 URL 라우팅을  지원하고 있다. 
