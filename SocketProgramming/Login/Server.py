from multiprocessing.dummy import connection
from socket import *
serverAddress = '127.0.0.1' # 서버 주소, 루프백 사용
serverPort = 9999 # 서버 포트 번호
serverSocket = socket(AF_INET, SOCK_STREAM) # 클라이언트 소켓 생성, IPv4 사용, TCP 사용
serverSocket.bind((serverAddress, serverPort)) # 포트를 서버 소켓에 바인딩
serverSocket.listen(1) # 클라이언트 요청 대기, 최대 연결 가능 수 = 1
print("Server is ready to receive")

loginData = {} # id와 pw 정보 데이터
code = {1:'Success', 2:'WrongId', 3:'WrongPw'} # id와 pw 검색 후 클라이언트에게 전달할 메시지에 대한 코드

while True:
    connectionSocket, address = serverSocket.accept() # 연결 요청이 들어오면 연결 소켓을 생성하고 주소를 리턴
    # id와 pw를 클라이언트로부터 수신
    inputId = connectionSocket.recv(1024).decode()
    inputPw = connectionSocket.recv(1024).decode()

    # id와 pw 확인
    try:
        if inputPw == loginData[inputId]: # 입력한 id가 데이터에 존재하고 pw가 일치하는 경우
            connectionSocket.send(code[1].encode)
        else: # 입력한 id가 데이터에 존재하지만 pw가 일치하지 않는 경우
            connectionSocket.send(code[3].encode)
    except KeyError as e: # 입력한 id가 데이터에 존재하지 않는 경우
        connectionSocket.send(code[2].encode)
    