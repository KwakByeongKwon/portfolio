<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="board.*"%>

<%@ include file="boardHeader.jsp" %>
<title>글등록</title>
<%@ include file="/navbar.jsp" %>

	<% if(!idCookieExists) {
		response.sendRedirect("/boardPractice/login/loginForm.jsp"); 
	}
	%>

<form action="regist.jsp" method="post" enctype="multipart/form-data">
	<div class="container text-center" style="width:500px">
		<div class="card border-dark mb-3" style="max-width: 50rem;">
			<h1>글등록</h1>
			<div class="card-body">
				<div class="input-group mb-3">
					<span class="input-group-text">제목</span>
					<input type="text" class="form-control" name="title" placeholder="제목"  required>
				</div>
					<input type="hidden" name="writer" value="<%= id %>">
				<div class="input-group">
					<span class="input-group-text">내용</span>
					<textarea class="form-control" placeholder="내용" aria-label="내용" name="content"></textarea>
				</div>
				<br>
				<div class="input-group mb-3">
					<input type="file" name="file" class="form-control">
				</div>
				<br>
				<div class="card-footer">
					<input type="submit" value="등록" class="btn btn-success">
				</div>
			</div>
		</div>
	</div>
</form>
</body>
</html>