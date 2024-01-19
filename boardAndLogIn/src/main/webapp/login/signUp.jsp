<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="createAccount.*"%>

<jsp:useBean id="dao" class="createAccount.CreateAccountDao"/>
<jsp:useBean id="vo" class="createAccount.CreateAccountVo"/>
<jsp:setProperty name="vo" property="*"/>

<%
	String pw = request.getParameter("pw");
	String pwCk = request.getParameter("pwCk");
%>

<% if(!pw.equals(pwCk)){
%>
      <script>
          alert("비밀번호가 일치하지 않습니다.");
          window.location.href = "signUpForm.jsp";
       </script>
<%	
	} else if(pw.equals(pwCk)){
		dao.signUp(vo);
		Cookie cookie = new Cookie("id",request.getParameter("id"));
		cookie.setPath("/");
		response.addCookie(cookie);
		response.sendRedirect("/boardPractice/board/list.jsp");
	}
%>


