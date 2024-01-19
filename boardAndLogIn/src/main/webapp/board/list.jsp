<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="board.*, java.util.List"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>


<%
    BoardDao dao = new BoardDao();
    List<BoardVo> ls = dao.selectAll();
    pageContext.setAttribute("ls", ls);

    // 총페이지수
    int totalLength =ls.size(); 

    // 페이지 번호 파라미터 처리
    String pageParam = request.getParameter("page");
    int pages = (pageParam != null) ? Integer.parseInt(pageParam) : 1;

    // 페이지당 표시할 항목 수
    int itemsPerPage = 8;

    // 시작 인덱스 계산
    int startIndex = (pages - 1) * itemsPerPage;
    
    // 리스트 슬라이싱
  	int endIndex = Math.min(startIndex + itemsPerPage, totalLength);
    
%>

<%@ include file="boardHeader.jsp" %>
<title>게시판</title>
<%@ include file="/navbar.jsp" %>

	<% if(!idCookieExists) {
		response.sendRedirect("/boardPractice/login/loginForm.jsp"); 
	}
	%>

<div class="container text-center" style="font-size:23px">
    <div class="d-flex justify-content-between align-items-center">
        <h1></h1>
        <h1>게시판</h1>
        <a href="registForm.jsp" class="btn btn-primary">글등록</a>
    </div>
    <table class="table table-striped">
        <tr>
            <th>번호</th>
            <th>제목</th>
            <th>작성자</th>
            <th>작성일</th>
            <th colspan="2">기타</th>
        </tr>
        <%
            for(int i = startIndex; i < endIndex; i++){
                BoardVo vo = ls.get(i);
                int number = totalLength - startIndex - (i - startIndex);
        %>
                <tr>
                    <td><%= number %></td>
                    <td>
                        <a href="boardDetail.jsp?num=<%= vo.getNum() %>&number=<%= number %>">
                            <%= vo.getTitle() %>
                        </a>
                        <span class="badge bg-primary rounded-pill"><%= vo.getCnt() %></span> 
                    </td>
                    <td><%= vo.getWriter() %></td>
                    <td><%= vo.getRegdate() %></td>
        <%
        	if(vo.getWriter().equals(id)){
        %>
	            <td>
                    <a href="editForm.jsp?num=<%= vo.getNum() %>&number=<%= number %>" class="btn btn-primary">수정</a>
                </td>
                <td>
                    <a href="deleteForm.jsp?num=<%= vo.getNum() %>" class="btn btn-danger">삭제</a>
                </td>
        <%		
        	} else{
        %>
        		<td> </td>
        		<td> </td>
        <%
        	}
        %>

                </tr>
        <%
                number++;
            }
        %>
    </table>

    <!-- 페이지네이션 링크 -->
    <div>
        <%
            int totalPages = (int) Math.ceil((double) ls.size() / itemsPerPage);
        %>
        	<a href="?page=1">처음</a>
        <%
        	if(pages != 1){
        %>
        		<a href="?page=<%= (pages - 1) %>">이전</a>
        <%
        	} else if (pages == 1) {
        %>
        		<a href="?page=1" >이전</a>
        <%
        	}
            for(int p = 1; p <= totalPages; p++) {
                if(p == pages) {
        %>
        			<b>
        				<a href="?page=<%= p %>"><%= p %></a>
        			</b>
        <%
                } else {
        %>
        				<a href="?page=<%= p %>"><%= p %></a>
        <%
                }
            }
        %>
        <%
        	if(pages != totalPages){
        %>		
		        <a href="?page=<%= (pages + 1) %>">다음</a>
        <%
        	} else if (pages == totalPages) {
        %>
        		<a href="?page=<%= totalPages %>">다음</a>
        <%
        	}
        %>
        	<a href="?page=<%= totalPages %>">끝</a>
    </div>
</div>
</body>
</html>