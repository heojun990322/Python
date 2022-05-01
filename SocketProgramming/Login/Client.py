from socket import *
serverAddress = '127.0.0.1' # 서버 주소, 루프백 사용
serverPort = 9999 # 서버 포트 번호
clientSocket = socket(AF_INET, SOCK_STREAM) # 클라이언트 소켓 생성, IPv4 사용, TCP 사용
clientSocket.connect((serverAddress, serverPort)) # 서버 연결 시도

# ID와 PW를 입력 후 서버에 전송
id = input("ID : ")
pw = input("PW : ")
clientSocket.send(id.encode())
clientSocket.send(pw.encode())
