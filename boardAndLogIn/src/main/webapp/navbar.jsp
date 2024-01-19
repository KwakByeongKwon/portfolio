<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
   
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
%>
</head>
<body>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">JSP 게시판 웹사이트</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link" href="/boardPractice/board/list.jsp">게시판</a>
            </li>
            <li class="nav-item">
            	<a class="nav-link disabled" aria-disabled="true"><%= id %></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/boardPractice/login/logOut.jsp" style="color:red;">로그아웃</a>
            </li>
          </ul>
          <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                더보기	
              </a>
              <ul class="dropdown-menu dropdown-menu-end">
              <% if(id == null){ %>
          	    <li class="active">
                	<a class="dropdown-item" href="/boardPractice/login/loginForm.jsp">로그인</a>
                </li>
                <li>
                	<a class="dropdown-item" href="/boardPractice/login/signUpForm.jsp">회원가입</a>
               	</li>
			<% } else { %>
				<li>
					<a class="dropdown-item" href="#"><%= id %></a>
				</li>
			    <li>
			        <a class="dropdown-item" href="#">회원정보</a>
			    </li>
			    <li>
			        <a class="dropdown-item" href="/boardPractice/login/logOut.jsp">로그아웃</a>
			    </li>
			<% } %>

             </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <br>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
