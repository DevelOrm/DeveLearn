# DeveLearn

- 팀명: DeveLorm
- 주제(서비스명): 온라인 학습 플랫폼
  - 클래스를 운영하는 선생님과, 원하는 클래스를 수강하는 학생 간의 교육이 이루어지는 온라인 학습 플랫폼입니다.
- REPO 주소: https://github.com/DevelOrm/DeveLearn

<img width="2048" src="https://github.com/FutureMaker0/DRF_webex_final/assets/120623320/c04c8f3f-feac-48d2-9e5e-6036a6ca66e0">

# 개발 기간

- 23.8.17 ~ 23.09.04

# DataBase Structure

<img width="2048" src="https://github.com/FutureMaker0/DRF_webex_final/assets/120623320/ef6ae05e-57b3-437d-9501-16dd91d4b21d">

# 배포 URL

- FE: http://develearn.co.kr/
- BE: http://52.79.53.117/
- 테스트용 계정
  - id: user1
  - pw: pw1

# 배포 서버 구조

<img width="2048" src="https://github.com/FutureMaker0/DRF_webex_final/assets/120623320/fe6b7858-b548-4883-a107-ccd5813fe61c">

# API 명세 자동화

> drf-spectacular 적용

- http://52.79.53.117/api/swagger (swagger-ui)
- http://52.79.53.117/api/redoc (redoc-ui)
- 테스트용 관리자 계정 (관리자 계정만 접근할 수 있습니다.)
  - id: test
  - pw: test

# Index

[1. 기술스택 & 개발환경](#1-기술-스택--개발-환경)  
 [2. 팀원소개 및 역할](#2-팀원소개-및-역할)  
 [3. 프로젝트 요약](#3-프로젝트-요약)  
 [4. 주요 기능 소개](#4-주요-기능-소개)  
 [5. 라이브 데모](#5-기능app별-라이브-데모)  
 [6. 개발 중 장애물 & 극복 방법](#6-개발-중-장애물--극복-방법)  
 [7. 추가 및 리서치 하고 싶은 기능](#7-추가-및-리서치-하고-싶은-기능)  
 [8. 프로젝트 소감 (어려웠던 점 & 배운점 & 향후 계획)](#8-프로젝트-소감-어려웠던-점--배운점--향후-계획)  
 [9. Q & A](#)

# 1. 기술 스택 & 개발 환경

<table>
    <thead align="center">
        <tr>
            <th><span>BE</span></th>
            <th><span>FE</span></th>
            <th><span>DB</span></th>
            <th><span>DEPLOYMENT</span></th>
            <th><span>MANAGEMENT</span></th>
        </tr>
    </thead>
    <tbody>
          <td align="center">
              <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
              <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
          </td>
          <td align="center">
              <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
              <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
              <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
          </td>
          <td align="center">
              <img src="https://img.shields.io/badge/postgresql-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" width="250" height="30">
          </td>
          <td align="center">
              <img src="https://img.shields.io/badge/Amazon EC2-FF9900?style=for-the-badge&logo=Amazon EC2&logoColor=white">
              <img src="https://img.shields.io/badge/amazon s3-569A31?style=for-the-badge&logo=amazons3&logoColor=white">
              <img src="https://img.shields.io/badge/nginx-009639?style=for-the-badge&logo=nginx&logoColor=white">
              <img src="https://img.shields.io/badge/gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white">
          </td>
          <td align="center">
            <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
            <img src="https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white">
            <img src="https://img.shields.io/badge/discord-5865F2?style=for-the-badge&logo=discord&logoColor=white">
          </td>
    </tbody>
</table>
     
# 2. 팀원소개 및 역할
<table>
    <colgroup>
        <col style="width: 200px;">
        <col style="width: 200px;">
        <col style="width: 200px;">
        <col style="width: 200px;">
        <col style="width: 200px;">
    </colgroup>
    <thead align="center">
        <tr>
            <th>★남궁범★</th>
            <th>이지섭</th>
            <th>주기현</th>
            <th>김재현</th>
            <th>박종수</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">
                <img width="200px" src="https://avatars.githubusercontent.com/u/90359639?v=4"/>
            </td>
            <td align="center">
                <img width="200px" src="https://avatars.githubusercontent.com/u/89283288?v=4"/>
            </td>
            <td align="center">
                <img width="200px" src="https://avatars.githubusercontent.com/u/95518318?v=4"/>
            </td>
            <td align="center">
                <img width="170px" src="https://avatars.githubusercontent.com/u/120623320?v=4"/>
            </td>
            <td align="center">
                <img width="200px" src="https://avatars.githubusercontent.com/u/131739329?v=4"/>
            </td>
        </tr>
        <tr>
            <td align="center">
                <a href="https://github.com/tombeom">🔗tombeom</a>
            </td>
            <td align="center">
                <a href="https://github.com/vBORIv">🔗vBORIv</a>
            </td>
            <td align="center">
                <a href="https://github.com/rlguswn">🔗rlguswn</a>
            </td>
            <td align="center">
                <a href="https://github.com/FutureMaker0">🔗FutureMaker0</a>
            </td>
            <td align="center">
                <a href="https://github.com/jongsoo-P">🔗jongsoo-P</a>
            </td>
        </tr>
        <tr>
            <td align="center">유저</td>
            <td align="center">뉴스</td>
            <td align="center">클래스룸</td>
            <td align="center">API 문서화</td>
            <td align="center">배포</td>
        </tr>
        <tr>
            <td align="center">유저</td>
            <td align="center">뉴스</td>
            <td align="center">클래스룸</td>
            <td align="center">API 문서화</td>
            <td align="center">배포</td>
        </tr>
    </tbody>
</table>

# 3. 프로젝트 요약

- 서비스 전체 개요
  - 온라인 학습 플랫폼 DeveLearn은 선생님-학생 간 학습이 이루어지는 공간입니다.
  - 선생님은 기술스택 별 클래스를 개설하고 문제출제(문제게시판), 강의자료 게시(자료게시판), 질문대응(질문게시판)을 수행합니다.
  - 학생은 원하는 기술스택 클래스를 수강하며 문제 답변제출(문제게시판), 강의자료 다운로드(자료게시판), 질문등록(질문게시판)을 할 수 있습니다.
  - 선생님이 출제하고 학생이 제출한 문제 답변을 자동으로 채점하여 결과를 피드백합니다.
  - 사용자별(학생, 선생님) 클래스 구독 정보를 알 수 있습니다.
  - IT업계 동향을 파악할 수 있는 최신 뉴스를 홈페이지에서 보여줍니다.
- 서비스 개발 관점

  - drf-spectacular를 적용해 API 명세를 작성하여 협업 간 효율증진을 도모하였습니다.
  - 서비스를 실 배포하여(Lightsail, EC2활용) 추후 운영이 가능하도록 하였습니다.

- 협업
  - Notion 기반 프로젝트 일정관리 진행하였습니다.
  - 협업 효율 최적화를 위해 일 3회(9/13/16시) 정기회의를 진행하였습니다.

<table>
  <colgroup>
      <col style="width: 250px;">
      <col style="width: 250px;">
      <col style="width: 250px;">
  </colgroup>
  <thead align="center">
      <tr>
          <th>팀스페이스</th>
          <th>일정</th>
          <th>회의록</th>
      </tr>
  </thead>
  <tbody>
      <tr>
          <td align="center">
              <img height="400px" src="https://github.com/DevelOrm/DeveLearn/assets/89283288/f2473711-8cb4-4834-ad8c-8e13d114ec32"/>
          </td>
          <td align="center">
              <img height="400px" src="https://github.com/DevelOrm/DeveLearn/assets/89283288/8ad1b74a-05e3-4197-b32b-8740b8db08ea"/>
          </td>
          <td align="center">
              <img height="400px" src="https://github.com/DevelOrm/DeveLearn/assets/89283288/d5fdebdc-f460-43f6-a0fa-8c0166a16a92"/>
          </td>
      </tr>
  </tbody>
</table>

# 4. 주요 기능 소개

- Classroom

  > 클래스룸 - 게시판 - 댓글 구조의 기본 CRUD 기능을 제공한다

  - 클래스룸

  게시판의 종류는 문제 게시판, 강의자료 게시판, 질문 게시판 총 3가지가 있다
  선생님으로 지정된 유저가 클래스룸, 게시판을 생성할 수 있고 클래스룸을 구독한 유저들이 이를 자유롭게 이용 가능하다

  - 문제 게시판

  선생님으로 지정된 유저가 문제 게시글을 생성하면 각 유저들이 자유롭게 문제에 대한 댓글 혹은 답변 제출이 가능하다
  auto_score가 true인 문제 게시글에 유저가 답변을 제출하면 미리 지정된 문제 게시글의 solution필드와 비교해 채점하며 정답 여부가 answer_status필드에 저장된다

  ```python
  ## models.py
  class Test(models.Model):
      solution = ArrayField(models.CharField(max_length=50, blank=True), null=True, blank=True)
      auto_score = models.BooleanField()
      # ...

  ## views.py TestSubmitView
  def post(self, request):
      try:
          test_pk = request.data['test']
          test_obj = Test.objects.get(pk=test_pk)
          if request.user.is_authenticated:
              solution = test_obj.solution
              user_answer = request.data['user_answer']
              if test_obj.auto_score:
                  answer_status = user_answer in solution
              else:
                  answer_status = None
      # ...
  ```

  - 강의자료 게시판

  선생님으로 지정된 유저가 학습용 파일, 이미지, 텍스트를 게시글로 작성할 수 있고 유저들이 자유롭게 이용 가능하다

  - 질문 게시판

  클래스룸을 구독한 유저 모두가 이용 가능하며 이미지를 첨부해 게시글을 작성할 수 있다

  - 댓글

  로그인된 유저는 각 게시판의 게시글에 댓글을 작성할 수 있다

- News

  > GitHub Action을 이용하여 개발 관련 키워드를 검색하여 나온 뉴스 크롤링을 매일 진행한다. 크롤링된 뉴스 목록은 post로 `/news/bot/`의 URL로 전송하여 서버 DB에 저장한다.

  - 크롤링 봇 자동화

    ```yml
    ## .github/workflows/DeveLearnNewsBot.yml
    on:
      schedule:
        - cron: "0 21 * * *"

    jobs:
      build:
        # ...

        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            python -m pip install beautifulsoup4
            python -m pip install requests
        - name: run macro main.py file
          run: |
            python main.py
    ```

  GitHub Action을 이용하여 매일 `21:00 UTC` 에 Linux에 환경세팅 후 main.py 파일을 실행하도록 설정했다. main.py 파일에서 크롤링 함수를 실행하고 서버 URL에 뉴스 데이터를 담아 전송하면, 서버에서 데이터 확인 후 DB에 저장하게 된다.

  - 검색엔진 확장성

    ```python
    ## NewsBot.py
    def NaverNews(keyword):
        # ...

    def GoogleNews(keyword):
        # ...

    ## main.py
    import NewsBot

    NewsBot.NaverNews(keyword)
    # ...
    ```

  각 검색엔진에서 뉴스 리스트를 크롤링하는 기능을 하나의 함수로 구현하여 `main.py`에서 실행하도록 구조화하였다. 이를 통해 추후 크롤링할 검색엔진 추가 또는 페이지 구조 변경으로 인한 함수 수정 시 용이성을 높일 수 있었다.

  - 검색 키워드 확장성

    ```python
    ## keywords.txt
    keyword1 keyword2 ...

    ## main.py
    with open('keywords.txt', 'r') as keywords_file:
            keywords = keywords_file.read().split()

        for keyword in keywords:
            NewsBot.NaverNews(keyword)
            # ...
    ```

  검색에 사용할 키워드를 외부 파일에서 가져와 각 검색 엔진 크롤링 함수에 넣어 실행하였다. 이를 통해 추후 검색 키워드 추가 및 변동 시 용이성을 높일 수 있었다.

  - 중복 뉴스 처리

    ```python
    ## news/views.py
    for news_index in data:
        news = data[news_index]
        if News.objects.filter(title=news['title']).exists():
            continue
    ```

  크롤링된 뉴스 데이터가 서버로 전송되면 중복을 확인하여 DB에 없는 뉴스인 경우에만 새로 추가한다. 같은 뉴스이더라도 redirect되는 링크가 상이할 수 있기 때문에 기사 제목으로 중복 여부를 확인하였다.

  각 뉴스 데이터마다 DB 호출을 하여 확인해야 하기 때문에 다소 비효율적인 측면이 존재한다. 우선적으로 가장 서버 활성이 적을 것이라 예상되는 늦은 새벽 시간에 크롤링 및 서버 전송이 동작하도록 설정하여 과부하를 최소화하였다.

  - 오늘의 뉴스 기능

    ```python
    class NewsRecentView(generics.ListAPIView):
        queryset = News.objects.all().order_by('-written_at')[:6]
        serializer_class = NewsSerializer
    ```

  프론트엔드 메인페이지에 오늘의 뉴스를 출력하기 위해 최신 뉴스 출력 기능을 구현하였다. 화면에 6개의 뉴스 객체를 출력하기 때문에 가장 최근에 DB에 추가된 순서대로 6개의 뉴스 데이터를 담아 브라우저에 응답한다.

- User

  - ```AbstractBaseUser``` 상속 받아 불필요한 Field 제거 및 Custom Field 추가
    ```python
    class User(AbstractBaseUser):
        objects = UserManager()
        user_id = models.CharField(max_length=20, unique=True)
        nickname = models.CharField(max_length=20, unique=True)
        email = models.EmailField(max_length=128, unique=True)
        phone_number = models.CharField(max_length=14, unique=True)
        profile_image = models.ImageField(blank=True, null=True)
        joined_date = models.DateTimeField(auto_now_add=True)
        is_active = models.BooleanField(default=True)
        is_teacher = models.BooleanField(default=False)
        is_admin = models.BooleanField(default=False)
    
    class Meta:
        db_table = "user"
        verbose_name = "user"
        verbose_name_plural = "users"
    ```

  - JWT를 이용한 인증 방식 구현
  - 회원가입, 회원 정보 조회, 회원 정보 수정,  회원 삭제 등 기본적인 User Model CRUD 제공
  - 회원가입 시 60개의 긍정 형용사, 동물 40개, #0001~9999 범위의 랜덤한 수를 조합해 랜덤 닉네임 생성 ```열정적인 호랑이#1234```
  - 백엔드에서 회원가입, 회원정보 수정 시 사용하는 serializer 중복 체크 외에도 프론트엔드에서 사용할 수 있는 중복체크 API 지원으로 DB에 중복 에러 발생하지 않도록 이중으로 설계
  - OAuth2.0 (Naver 소셜 로그인) 지원 및 소셜 로그인 시 닉네임, 핸드폰 번호, 닉네임 등을 User Model에 업데이트 및 저장
  - 회원가입 및 비밀번호 초기화 시 이메일 인증 단계를 추가해 보안 강화


# 5. 기능(APP)별 라이브 데모

|       APP       |                                                                     이미지/데모                                                                      |     비고      |
| :-------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------: |
|    Classroom    |              ![클래스룸1](https://github.com/FutureMaker0/DRF_webex_final/assets/120623320/99e2bb3d-23c3-4cf8-a27e-69df46caa213)               | 클래스룸 동작 |
|      News       | <img width="1469" alt="뉴스 목록" src="https://github.com/FutureMaker0/DRF_webex_final/assets/120623320/bba85e7c-ee9b-49b7-bbda-bf2b749e8df6"> |  뉴스 크롤링  |
|      User       |          <img width="1470" alt="회원가입" src="https://github.com/DevelOrm/DeveLearn/assets/89283288/1034faac-41e8-4bca-84d3-183b65dcd105">          |   회원가입    |
|      User       |        <img width="1470" alt="회원가입예외" src="https://github.com/DevelOrm/DeveLearn/assets/89283288/0c4b92f3-3e56-4278-8fb0-a53f323ab997">        | 회원가입 예외 |
| drf-spectacular |                  ![swagger](https://github.com/FutureMaker0/DRF_webex_final/assets/120623320/d25104ca-50ce-4f28-a7e4-c7d35d329ca2)                   |  SWAGGER-UI   |
| drf-spectacular |                   ![redoc](https://github.com/FutureMaker0/DRF_webex_final/assets/120623320/ec15c63b-b9f4-4d02-93c0-7fdf6f0dc1d6)                    |   REDOC-UI    |

# 6. 개발 중 장애물 & 극복 방법

  <table>
    <thead align="center">
        <tr>
            <th><span>기능(APP)</span></th>
            <th><span>장애물</span></th>
            <th><span>극복방법</span></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center" rowspan="2">
                <a>Classroom</a>
            </td>
            <td align="center">
                <a>이미지 필드와 파일 필드의 업로드 문제</a>
            </td>
            <td>
                <a>- JSON raw 데이터로만 CRUD기능을 테스트하던 중, 이미지와 파일이 포함된 POST 요청을 보내는 방법을 숙지하지 못함 요청하는 데이터의 body를 raw 데이터가 아닌 form-data형식으로 요청하여 해결</a>
            </td>
        </tr>
        <tr>
            <td align="center">
                <a>업데이트뷰 작성시 부분 업데이트 에러 문제</a>
            </td>
            <td>
                <a>- serializer의 'partial=True' 옵션을 사용해 유효성 검사를 완화하여 검사에 실패한 필드가 있더라도 업데이트가 가능하도록 함</a>
            </td>
        </tr>
        <tr>
            <td align="center" rowspan="3">
                <a>drf-spectacular</a>
            </td>
            <td align="center">
                <a>지금까지의 프로젝트에서 활용해본 적이 없는 새로운 개념으로 배경지식 부족</a>
            </td>
            <td rowspan="2">
                <a>- 공식문서 활용 및 관련 내용을 다룬 기술 블로그 참조</a>
            </td>
        </tr>
        <tr>
            <td align="center">
                <a>활용법 미숙지로 인해 setting 및 적용하는 과정에서 장애 발생</a>
            </td>
        </tr>
        <tr>
            <td>
                <a>spectacular ui 적용 후, 단순 적용에서 나아가 view layer수준 api doc 커스터마이징 과정에서 장애 발생</a>
            </td>
            <td>
                <a>- 전체 서비스 내 app별로 view 상속 레벨이 다른 경우, drf-spectacular가 매번 같은 형태로 적용하지 않으며 다른 방식을 취함을 스터디 후 적용</a><br>
                <a>- @extend_schema / @extend_schema_view / @extned_schema_serializer 등이 있고 동시 적용 시 우선순위가 존재</a>
            </td>
        </tr>
        <tr>
            <td align="center" rowspan="3">
                User
            </td>
            <td>
                <a>라이브러리 사용 시 직접 설계한 것이 아니라 공식문서를 읽고 코드를 이해하는데 어려움</a>
            </td>
            <td>
                <a>직접 코드를 분석해보고 어떻게 동작하는지 확인하면서 이해하는 과정을 거침</a>
            </td>
        </tr>
        <tr>
            <td>
                <a>비정상적 API 요청에 대해 대비해야 할 경우의 수가 많다.</a>
            </td>
            <td>
                <a>직접 어떤 취약점이 있을까 직접 공략을 해보고 대비할 코드를 만들었다.</a>
            </td>
        </tr>
    </tbody>
</table>

# 7. 추가 및 리서치 하고 싶은 기능

<table>
    <thead align="center">
        <tr>
            <th><span>기능(APP)</span></th>
            <th><span>TO-BE</span></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">
                <a>Classroom</a>
            </td>
            <td>
                <a> - 게시글에 영상을 첨부해 재생할 수 있는 기능 </a> <br>
                <a> - 신고 기능(분탕 유저 신고 기능, 오타수정 제보 기능, 에러 제보 기능 등)) </a>
            </td>
        </tr>
        <tr>
            <td align="center">
                <a>News</a>
            </td>
            <td>
                <a> - 뉴스 중복 처리 효율성: 현재 코드는 모든 크롤링된 데이터에 대해서 한번씩 DB 호출을 통해 중복 여부를 확인하기 때문에 다소 비효율 적이다. 따라서 추후 서버 이용자 및 크롤링 데이터가 많아지는 상황에 대비하여 뉴스 중복 처리 과정에서 DB 호출을 줄일 수 있는 방법이 필요하다.</a> <br>
                <a> - 뉴스 추가 페이지 인증: 현재 크롤링된 뉴스 데이터는 `/news/bot/`로 POST 요청을 보내 서버로 전송된다. 이때 json 구조만 일치시키면 인증 과정 없어 서버 DB에 데이터가 추가될 수 있다. 따라서 GitHub Private Key에 인증 정보를 저장하고 서버의 views.py에서 인증 과정을 추가하여 DB 접근을 관리해야 할 것이다.</a> <br>
            </td>
        </tr>
        <tr>
            <td align="center">
                <a>User</a>
            </td>
            <td>
                <a> - Python logging 모듈을 사용해 로그를 남기고 유저 패턴 및 악의적인 요청 분석</a> <br>
                <a> - 핸드폰 번호 인증을 도입해 보안 강화</a> <br>
                <a> - 프로필 사진 업로드 시 저장되는 이미지를 변환(메타 데이터 삭제 및 리사이징)해서 개인정보 보호 및 서버 리소스 소모 감소</a> <br>
                <a> - CAPTCHA 등 봇 탐지 도입</a><br>
                <a> - 비정상적 요청이 많은 유저는 자동으로 차단할 수 있는 기능 추가</a><br>
                <a> - 1년 이상 미접속 사용자 휴면 계정 전환 기능 추가</a><br>
                <a> - 핸드폰 번호 인증을 도입해 보안 강화</a><br>
                <a> - 프로필 사진 업로드 시 저장되는 이미지를 변환(메타 데이터 삭제 및 리사이징)해서 개인정보 보호 및 서버 리소스 소모 감소</a><br>
            </td>
        </tr>
        <tr>
            <td align="center">
                <a>drf-spectacular</a>
            </td>
            <td>
                <a> - View 클래스 내부 메소드 단위의 schema를 일괄적으로 적용한 것에 대한 아쉬움 존재 </a> <br>
                <a> - 단순 적용 및 담당 serializer를 request/response하여 api 동작을 확인하는 것에 추가로, 메소드별 커스터마이징 추가적용 희망 </a> <br>
                <a> - 커스터마이징 시 각 파라미터별 역할과 사용법을 좀 더 익혀 서비스 개발 시 협업에 큰 도움이 되는 drf-spectacular에 대한 이해도와 활용 스킬을 증진하고자 함</a>
            </td>
        </tr>
        <tr>
            <td align="center">
                <a>배포</a>
            </td>
            <td>
                <a> - CI/CD: 베포 전 dev 브랜치를 기준으로 테스트 서버를 가동하여 백엔드 후반 작업 및 프론트엔드 연결을 진행하였다. 이때 새로운 feature를 dev 브랜치에 적용할 때마다 직접 서버에서 git pull 명령어로 업데이트하였다. GitHub Action을 이용하여 dev 브랜치에 push 발생을 기준으로 자동화 시스템을 구축할 수 있을 것이다.</a> <br>
            </td>
        </tr>
    </tbody>
</table>

# 8. 프로젝트 소감 (어려웠던 점 & 배운점 & 향후 계획)

- 어려웠던 점 (trouble shooting)
- 배운점
- 향후 계획

```

```
