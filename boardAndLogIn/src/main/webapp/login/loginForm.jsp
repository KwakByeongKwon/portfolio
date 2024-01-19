<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="/board/boardHeader.jsp" %>
<title>로그인</title>
</head>
<body>
<%
	boolean idCookieExists = false;
	Cookie[] cookies = request.getCookies();
	String id = "";
	if(cookies != null && cookies.length > 0){
		for(Cookie cookie:cookies){
			if(cookie.getName().equals("id")){
				id = cookie.getValue();
				idCookieExists = true;
			}
		}
	}
	if(idCookieExists){
		response.sendRedirect("/boardPractice/board/list.jsp");
	}
%>

<nav class="navbar navbar-expand-lg bg-body-tertiary">
	<br>
	<br>
</nav>
<div class="container text-center">
  <div class="row">
   	<div class="col mb-4"></div>
	<div class="col mb-4" style="padding-top:20px;">
		<form action="login.jsp" method="post">
			<h3>로그인 화면</h3>
			<div class="form-group">
				<input type="text" class="form-control" placeholder="ID" name="id" maxlength="20" required>
			</div>
			<div class="form-group">
				<input type="password" class="form-control" placeholder="•••••••••••" name="pw" maxlength="20" required>
			</div>
			<button class="btn btn-success form-control">로그인</button>
			<br>
			<div>
				<a href="signUpForm.jsp" class="btn btn-primary form-control">회원가입</a>
			</div>
		</form>
    </div>
    <div class="col mb-4"></div>
  </div>
</div>
</body>
</html>