from multiprocessing.dummy import connection
from socket import *
serverAddress = '127.0.0.1' # 서버 주소, 루프백 사용
serverPort = 9999 # 서버 포트 번호
serverSocket = socket(AF_INET, SOCK_STREAM) # 클라이언트 소켓 생성, IPv4 사용, TCP 사용
serverSocket.bind((serverAddress, serverPort)) # 포트를 서버 소켓에 바인딩
serverSocket.listen(1) # 클라이언트 요청 대기, 최대 연결 가능 수 = 1
print("Server is ready to receive")

loginData = {} # id와 pw 정보 데이터
loginCode = {1:'Success', 2:'WrongId', 3:'WrongPw', 4:'Login', 5:'Register'} # login과 관련된 메시지에 매핑된 코드

def CheckLoginData(connectionSocket, inputId, inputPw): # id와 pw 확인
    try:
        if inputPw == loginData[inputId]: # 입력한 id가 데이터에 존재하고 pw가 일치하는 경우
            connectionSocket.send(loginCode[1].encode())
            connectionSocket.close()
        else: # 입력한 id가 데이터에 존재하지만 pw가 일치하지 않는 경우
            connectionSocket.send(loginCode[3].encode())
    except KeyError as e: # 입력한 id가 데이터에 존재하지 않는 경우
        connectionSocket.send(loginCode[2].encode())


while True:
    connectionSocket, address = serverSocket.accept() # 연결 요청이 들어오면 연결 소켓을 생성하고 주소를 리턴

    # 로그인과 등록 중 선택
    msg = connectionSocket.recv(1024).decode()
    if msg == 'Login': # 로그인인 경우
        inputId = connectionSocket.recv(1024).decode() # 입력한 id 수신
        inputPw = connectionSocket.recv(1024).decode() # 입력한 pw 수신
        CheckLoginData(connectionSocket, inputId, inputPw) # id와 pw 확인
    # elif msg == 'Register':


