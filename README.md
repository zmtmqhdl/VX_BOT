<p align="center">
  <img src="https://github.com/user-attachments/assets/ca63fcd5-5f26-4cdd-b0eb-93d7a4d93b3c" width="40%">
</p>

<h1 align="center" style="font-family: 'Gungsuh', sans-serif;"> VX BOT </h1>
<h3 align="center" style="font-family: 'Gungsuh', sans-serif;"> NEXON이 개발 및 운영한 온라인 게임 Veiled Experts 웹페이지에서 제공하는 API를 통해 유저들의 정보를 가져와 BOT을 사용하는 DISCORD 채널에서 사용자가 검색한 유저의 전적을 제공하는 BOT 프로그램 </h3>

<br>

## 📁 파일 설명 및 사용법
- [**VX_BOT.py**](https://github.com/zmtmqhdl/VX_BOT/blob/main/VX_BOT.py)  
  Veiled Experts 웹페이지에서 제공하는 API를 이용해 유저 프로필과 전적 정보를 가져옵니다. Discord 채널에 BOT이 추가되면, 사용자는 특정 명령어와 닉네임을 입력해 검색하고 싶은 유저의 전적을 확인할 수 있습니다. BOT은 Veiled Experts의 유저 검색 페이지에 POST 요청을 보내 닉네임을 전달하고, API로부터 유저 정보를 받아옵니다. 받은 JSON 데이터를 가공해 필요한 정보와 이미지를 Discord 채널에 이미지 형태로 아래와 같이 출력하여 사용자가 유저 전적을 확인할 수 있도록 합니다.


  <img src="https://github.com/user-attachments/assets/418361da-42c0-4bfb-8977-9d9db2e89a94" width="40%">

- [**BOT_Keep_Alive.py**](https://github.com/zmtmqhdl/VX_BOT/blob/main/BOT_Keep_Alive.py)  
  Replit 환경에서 Flask를 사용해 VX_BOT이 작동되도록 합니다. 이후, Ping 서비스를 제공하는 웹페이지에서 Replit의 URL로 주기적으로 Ping을 보내 BOT이 종료되지 않도록 유지합니다. 이를 통해 BOT을 안정적으로 24시간 실행시킬 수 있습니다.

<br>

| 명령어                 | 기능                                                                                  |
| ---                    | ---                                                                                   |
| /전적 [닉네임]          | 검색한 [닉네임]을 가진 유저의 전적을 Discord 채널에서 이미지로 제공합니다.                                       |

<br>

## 🛠️ 사용 기술
[![My Skills](https://skillicons.dev/icons?i=discord,flask,python,replit)](https://skillicons.dev)
