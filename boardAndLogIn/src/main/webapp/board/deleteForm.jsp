<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="board.*"%>
    
    
<jsp:useBean id="dao" class="board.BoardDao"/>
<%
	int num = Integer.parseInt(request.getParameter("num"));
%>
<%@ include file="boardHeader.jsp" %>
<title>삭제</title>
<%@ include file="/navbar.jsp" %>
<div class="container text-center" style="width:600px">
	<div class="card border-dark">
		<div class="card-body">
			<h1>삭제하시겠습니까?</h1>
			<br>
		<div class="card-footer">
			<a href="delete.jsp?num=<%= num %>" class="btn btn-danger">
				예
			</a>
			&nbsp &nbsp &nbsp &nbsp &nbsp	
			<a href="list.jsp" class="btn btn-primary">
				아니오 
			</a>
		</div>
		</div>
	</div>
</div>
</body>
</html>