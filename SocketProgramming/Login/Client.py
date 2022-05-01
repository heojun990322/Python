from socket import *
serverAddress = '127.0.0.1' # 서버 주소, 루프백 사용
serverPort = 9999 # 서버 포트 번호
clientSocket = socket(AF_INET, SOCK_STREAM) # 클라이언트 소켓 생성, IPv4 사용, TCP 사용
clientSocket.connect((serverAddress, serverPort)) # 서버 연결 시도
loginMsg = '' # 로그인 관련 메시지

# ID와 PW를 입력 후 서버에 전송
def Login(clientSocket):
    id = input("ID : ")
    pw = input("PW : ")
    clientSocket.send(id.encode())
    clientSocket.send(pw.encode())
    loginMsg = clientSocket.recv(1024).decode # Login 결과에 대한 메시지 수신
    return loginMsg

# 로그인과 등록 중 하나 선택
print("1. Login\n2. Register")
num = input("Input number : ")

if num == '1' : # 로그인을 선택한 경우
    loginMsg = 'Login'
    clientSocket.send(loginMsg.encode())
    loginMsg = Login(clientSocket)
elif num == '2' : # 등록을 선택한 경우
    loginMsg = 'Register'

while True:
    if loginMsg == 'Success': # 로그인 성공
        print("login success!")
        clientSocket.close()
        break
    elif loginMsg == 'WrongId' : # 입력한 id가 데이터에 없을 때
        print("Wrogn ID!")
        
        # 재입력과 등록 중 선택
        print("1. Reinput\n2. Register")
        num = input("Input num : ")

        # 로그인을 선택한 경우
        if (num == '1'):
            loginMsg = 'Login'
            clientSocket.send(loginMsg.encode())
            loginMsg = Login(clientSocket)
    elif loginMsg == 'WrongPw' : # 입력한 pw가 데이터에 없을 때
    


