<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="board.*"%>

<jsp:useBean id="dao" class="board.BoardDao" />
<%
	int num = Integer.parseInt(request.getParameter("num"));
	int number = Integer.parseInt(request.getParameter("number"));
	BoardVo vo = dao.selectOne(num);
%>
<%@ include file="boardHeader.jsp" %>

<title>글수정</title>
<%@ include file="/navbar.jsp" %>
<form action="edit.jsp?num=<%= vo.getNum() %>&number=<%= number %>" method="post">
	<div class="container text-center" style="width:500px">
		<div class="card border-dark mb-3">
			<h1>수정하기</h1>
			<div class="card-body">
				<div class="input-group mb-3">
					<span class="input-group-text">제목</span>
					<input type="text" class="form-control" name="title" value="<%= vo.getTitle() %>" placeholder="제목" required>
				</div>
				<div class="input-group mb-3">
					<span class="input-group-text">작성자</span>
					<input type="text" class="form-control" name="writer" value="<%= vo.getWriter() %>" readonly>
				</div>
				<div class="input-group">
					<span class="input-group-text">내용</span>
					<textarea class="form-control" name="content" placeholder="내용을 입력하세요."><%= vo.getContent() %></textarea>
				</div>
				<div class="card-footer">
					<input type="submit" value="확인" class="btn btn-primary">
				</div>
			</div>
		</div>
	</div>
</form>
</body>
</html>