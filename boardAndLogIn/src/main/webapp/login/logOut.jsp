<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="createAccount.*"%>

<%
	boolean idCookieExists = true;
	Cookie[] cookies = request.getCookies();
	String id = "";
	if(cookies != null && cookies.length > 0){
		for(Cookie cookie:cookies){
			if(cookie.getName().equals("id")){
				idCookieExists = false;
				cookie.setMaxAge(0); // 유효시간을 0으로 만들어서 저장함 그러면 생성되자마자 사라짐
				cookie.setPath("/");
				response.addCookie(cookie);
				response.sendRedirect("loginForm.jsp");
			}
		}
	}
%>

