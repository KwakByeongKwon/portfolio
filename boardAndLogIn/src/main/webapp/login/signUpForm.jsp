<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<%@ include file="/board/boardHeader.jsp"%>
<title>회원가입</title>
</head>
<body>
<nav class="navbar navbar-expand-lg bg-body-tertiary">
	<br>
	<br>
</nav>
<div class="container text-center">
  <div class="row">
   	<div class="col mb-4"></div>
	<div class="col mb-4" style="padding-top:20px;">
		<form action="signUp.jsp" method="post">
			<h3>회원가입</h3>
			<div class="form-group">
				<div class="input-group mb-3">
					<span class="input-group-text">ID</span>
					<input type="text" class="form-control" placeholder="아이디" name="id" maxlength="20" required>
					<a href="#"><span class="input-group-text">중복확인</span></a>
				</div>
			</div>
			<div class="form-group">
				<div class="input-group mb-3">
					<span class="input-group-text">PW</span>
					<input type="password" class="form-control" placeholder="•••••••••••" name="pw" maxlength="20" required>
				</div>
				<div class="input-group mb-3">
					<span class="input-group-text">확인</span>
					<input type="password" class="form-control" placeholder="•••••••••••" name="pwCk" maxlength="20" required>
				</div>
			</div>
			<button class="btn btn-success form-control">회원가입</button>
			<br>
			<div>
			<span>이미 계정이 있습니까?</span>
				<a href="logInForm.jsp" >로그인</a>
			</div>
		</form>
    </div>
    <div class="col mb-4"></div>
  </div>
</div>
</body>
</html>