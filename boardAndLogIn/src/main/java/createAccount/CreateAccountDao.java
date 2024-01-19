package createAccount;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import board.BoardVo;
import common.JdbcUtil;

public class CreateAccountDao {
	private JdbcUtil ju;

	public CreateAccountDao() {
		ju = JdbcUtil.getInstance();
	}
	

	// 회원가입(삽입[C])
	public int signUp(CreateAccountVo vo) {
		Connection con = null;
		PreparedStatement pstmt = null;
		String query = "Insert into \"ACCOUNT\" (\"NUM\",\"ID\",\"PASSWORD\",\"NICKNAME\") values (\"BOARD_SEQ\".nextval, ?,?,?)";
		int ret = -1;
		try {
			con = ju.getConnection();
			pstmt = con.prepareStatement(query);
			pstmt.setString(1, vo.getId());
			pstmt.setString(2, vo.getPw());
			pstmt.setString(3, vo.getNickName());
			ret = pstmt.executeUpdate();
		} catch(SQLException e) {
			e.printStackTrace();
		} finally {
			if(con != null) {
				try {
					con.close();
				} catch(SQLException e) {
					e.printStackTrace();
				}
			}
			if(pstmt != null) {
				try {
					pstmt.close();
				} catch(SQLException e) {
					e.printStackTrace();
				}
			}
		} 
		
		
		return ret;
	}
	// 로그인([R])
	public CreateAccountVo logIn(CreateAccountVo vo) {
		Connection con = null;
		PreparedStatement pstmt = null;
		String query = "select \"ID\",\"PASSWORD\" from \"ACCOUNT\" WHERE \"ID\"=? AND \"PASSWORD\"=?";
		ResultSet rs = null;
		CreateAccountVo cVo = null;
		try {
			con = ju.getConnection();
			pstmt = con.prepareStatement(query);
			pstmt.setString(1, vo.getId());
			pstmt.setString(2, vo.getPw());
			rs = pstmt.executeQuery();
			if(rs.next()) {
				cVo = new CreateAccountVo(rs.getString(1),
										rs.getString(2));
			}
		} catch(SQLException e) {
			e.printStackTrace();
		} finally {
			if(con != null) {
				try {
					con.close();
				} catch(SQLException e) {
					e.printStackTrace();
				}
			}
			if(pstmt != null) {
				try {
					pstmt.close();
				} catch(SQLException e) {
					e.printStackTrace();
				}
			}
			if(rs != null) {
				try {
					rs.close();
				} catch(SQLException e) {
					e.printStackTrace();
				}
			}
		}
		return cVo;
	}

}
