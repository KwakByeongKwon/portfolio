<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="createAccount.*"%>

<jsp:useBean id="dao" class="createAccount.CreateAccountDao"/>

<%
String id = request.getParameter("id");
String pw = request.getParameter("pw");
CreateAccountVo vo = new CreateAccountVo();
vo.setId(id);
vo.setPw(pw);

CreateAccountVo result = dao.logIn(vo); // logIn 메소드가 사용자 정보를 반환하도록 가정

if(result != null) {
	Cookie cookie = new Cookie("id", id);
	cookie.setPath("/");
	response.addCookie(cookie);
	response.sendRedirect("/boardPractice/board/list.jsp");
} else {
%>
      <script>
          alert("아이디 또는 비밀번호가 틀렸습니다.");
          window.location.href = "loginForm.jsp";
       </script>
<%
}
%>
