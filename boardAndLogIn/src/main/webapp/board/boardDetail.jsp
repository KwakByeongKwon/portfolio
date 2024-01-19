<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="board.*"%>

<jsp:useBean id="dao" class="board.BoardDao"/>

<%
	int number = Integer.parseInt(request.getParameter("number"));
	int num = Integer.parseInt(request.getParameter("num"));
	BoardVo vo = dao.selectOne(num);
	pageContext.setAttribute("vo", vo);
	dao.UpdateCnt(num);
%>

<%@ include file="boardHeader.jsp" %>
<title><%= vo.getTitle() %></title>
<%@ include file="/navbar.jsp" %><body>
<div class="container text-center">
	<table class="table table-striped">
		<tr>
			<th>
				번호
			</th>
			
			<th>
				제목
			</th>
			
			<th>
				작성자
			</th>
			
			<th>
				작성일
			</th>
			
			<th>
				조회수
			</th>
		</tr>
		<tr>
			<td>
				<%= number %>
			</td>
			<td>
				<%= vo.getTitle() %>
			</td>
			<td>
				<%= vo.getWriter() %>
			</td>
			<td>
				<%= vo.getRegdate() %>
			</td>
			<td>
				<%= vo.getCnt() %>
			</td>
		</tr>
		<tr>
			<th colspan="5">
				내용
			</th>
		</tr>
		<tr>
			<td colspan="5">
				<%= vo.getContent() %>
			</td>
		</tr>
	</table>
	<% if(id.equals(vo.getWriter())){ %>
		<div class="d-flex justify-content-between">
			<a href="editForm.jsp?num=<%= vo.getNum() %>&number=<%= number %>" class="btn btn-primary">수정</a>
			<a href="list.jsp" class="btn btn-primary">목록으로</a>
			<a href="deleteForm.jsp?num=<%= vo.getNum() %>&number=<%= number %>" class="btn btn-danger">삭제</a>
		</div>
	<% } else { %>
		<div class="d-flex justify-content-between">
			<a></a>
			<a href="list.jsp" class="btn btn-primary">목록으로</a>
			<a></a>
		</div>
	<% } %>
</div>

</body>
</html>