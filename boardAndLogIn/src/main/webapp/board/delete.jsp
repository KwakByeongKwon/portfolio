<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="board.*"%>

<jsp:useBean id="dao" class="board.BoardDao"/>

<%
	int num = Integer.parseInt(request.getParameter("num"));
	dao.Delete(num);
	
%>

<%
response.sendRedirect(request.getContextPath() + "/board/list.jsp");
%>