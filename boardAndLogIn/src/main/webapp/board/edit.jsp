<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="board.*"%>

<% request.setCharacterEncoding("UTF-8"); %>

<jsp:useBean id="dao" class="board.BoardDao"/>
<jsp:useBean id="vo" class="board.BoardVo"/>
<jsp:setProperty name="vo" property="*"/>


<%
	int num = Integer.parseInt(request.getParameter("num"));
	int number = Integer.parseInt(request.getParameter("number"));
	dao.Update(vo);
%>

<%
	response.sendRedirect(request.getContextPath() + "/board/boardDetail.jsp?num=" +  vo.getNum() + "&number=" + number);
%>