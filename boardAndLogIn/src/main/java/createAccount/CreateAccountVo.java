package createAccount;

public class CreateAccountVo {
	private int num;
	private String id;
	private String pw;
	private String nickName;
	
	

	public CreateAccountVo() {}
	public CreateAccountVo(String id, String pw) {
		super();
		this.id = id;
		this.pw = pw;
	}
	
	public CreateAccountVo(int num, String id, String pw, String nickName) {
		super();
		this.num = num;
		this.id = id;
		this.pw = pw;
		this.nickName = nickName;
	}
	
	public int getNum() {
		return num;
	}
	public void setNum(int num) {
		this.num = num;
	}
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getPw() {
		return pw;
	}
	public void setPw(String pw) {
		this.pw = pw;
	}
	public String getNickName() {
		return nickName;
	}
	public void setNickName(String nickName) {
		this.nickName = nickName;
	}
	
	
	@Override
	public String toString() {
		return "CreateAccountVo [num=" + num + ", id=" + id + ", pw=" + pw + ", nickName=" + nickName + "]";
	}
}
