# 임시 제목
  - 팀명: DeveLorm
  - 주제(서비스명): 온라인 학습 플랫폼(DeveLearn)
    - 클래스를 운영하는 선생님과, 원하는 클래스를 수강하는 학생 간의 교육이 이루어지는 온라인 학습 플랫폼입니다.
  - REPO 주소: https://github.com/DevelOrm/DeveLearn

# 개발 기간
  - 23.8.17 ~ 23.09.04

# DataBase Structure
  -

# API 명세
  -

# Index
  1. 기술스택 & 개발환경
  2. 팀원소개 및 역할
  3. 프로젝트 요약
  4. 주요 기능 소개
  5. 라이브 데모
  6. 개발 중 장애물 & 극복 방법
  7. 추가 및 리서치 하고 싶은 기능
  8. 프로젝트 소감 (어려웠던 점 & 배운점 & 향후 계획)
  9. Q & A

# 1. 기술 스택 & 개발 환경
<table>
    <thead align="center">
        <tr>
            <th><span>BE</span></th>
            <th><span>FE</span></th>
            <th><span>DB</span></th>
            <th><span>DESIGN</span></th>
            <th><span>DEPLOYMENT</span></th>
        </tr>
    </thead>
    <tbody>
          <td align="center">
              <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
              <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
          </td>
          <td align="center">
              <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
              <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white">
              <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
          </td>
          <td align="center">
              <img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white">
          </td>
          <td align="center">
              <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
          </td>
          <td align="center">
              <img src="https://img.shields.io/badge/amazon LightSail-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white">
              <img src="https://img.shields.io/badge/amazon s3-569A31?style=for-the-badge&logo=amazons3&logoColor=white">
              <img src="https://img.shields.io/badge/amazon RDS-527FFF?style=for-the-badge&logo=amazonrds&logoColor=white">
              <img src="https://img.shields.io/badge/nginx-009639?style=for-the-badge&logo=nginx&logoColor=white">
              <img src="https://img.shields.io/badge/gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white">
          </td>
    </tbody>
</table>
     
# 2. 팀원소개 및 역할
  |  | 팀원 | 역할 |
  |---|:---:|:---:|
  | 1 | 남궁범 | 유저, 인증 관련 개발 |
  | 2 | 이지섭 | 뉴스 CRUD 구현 |
  | 3 | 주기현 | 게시판 CRUD 구현 |
  | 4 | 김재현 | 코드 리팩토링, drf-spectacular |
  | 5 | 박종수 | s3 버킷 파일 업로드, Nginx 배포 |

# 3. 프로젝트 요약
  - 핵심요약1
  - 핵심요약2
      - 부가설명1
      - 부가설명2
   
# 4. 주요 기능 소개
  ## Classroom
      클래스룸 - 게시판 - 댓글 구조의 기본 CRUD 기능을 제공한다

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
  
  ## News
    GitHub Action을 이용하여 개발 관련 키워드를 검색하여 나온 뉴스 크롤링을 매일 진행한다. 크롤링된 뉴스 목록은 post로 `/news/bot/`의 URL로 전송하여 서버 DB에 저장한다.

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
    
  ## User
    로그인

    로그아웃
    
    회원정보
    
    중복체크
    
    비밀번호 변경
    
    비밀번호 초기화
    
    회원가입
    
    - 시리얼라이저 커스텀
    - validate 추가
    회원가입 이메일 확인
    소셜로그인 네이버
    - 
    
    랜덤 닉네임
    
    소셜 로그인 정보 넣기
    
    프론트단에서 할지 서버단에서 할지
    
    생각할 변수들이 너무 많다
    
    로깅
    기본 프로필
    이미지 변환 - 사진 리사이징, 메타 데이터 제거
    구현 후 서버 체크
    
    핸드폰 번호 인증
    
    - 보안 취약

  ## Spectacular
      - drf(django rest framwork)를 통해서 설계된 API를 OAS3.0 에 맞게 문서화를 도와주는 라이브러리
  - 배포 (서버구조)
      <img width="1796" alt="서버구조" src="https://github.com/FutureMaker0/DRF_webex_final/assets/120623320/c233f21d-3ed8-4107-aec1-1a064fafdee8">

# 5. 라이브 데모
|   | 이미지/데모 | 비고 |
|---|:--------:|:---:|
| Classroom |||
| News |||
| User |||
| spectacular |<img width="731" alt="swagger" src="https://github.com/FutureMaker0/DRF_webex_final/assets/120623320/9ebc11a4-e655-4062-9bae-a2d240e4d2ce">| swagger-ui |
|  |<img width="854" alt="redoc" src="https://github.com/FutureMaker0/DRF_webex_final/assets/120623320/71ad9542-cd88-4852-975c-14b8b2c38fda">| redoc-ui |

# 6. 개발 중 장애물 & 극복 방법
  - 장애물
    - drf-spectacular
      - 지금까지의 프로젝트에서 활용해본 적이 없는 새로운 개념으로 배경지식 부족
      - 활용법 미숙지로 인해 setting 및 적용하는 과정에서 장애 발생
      - spectacular ui 적용 후, 단순 적용에서 나아가 view layer수준 api doc 커스터마이징 과정에서 장애 발생
        - 전체 서비스 내 app별로 view 상속 레벨이 다른 경우, drf-spectacular가 매번 같은 형태로 적용하지 않으며 다른 방식을 취함
          - @extend_schema의 경우 메소드 단위 데코레이터로 하나의 메소드(path)에 해당하는 문서화 커스터마이징 시 사용하며 가장 보편적인 데코레이터
          - @extend_schema_view의 경우 클래스 단위 데코레이터로 하나의 ViewSet에 속한 메소드 문서화를 커스터마이징 하는데 활용
          - @extned_schema_serializer 시리얼라이져 자체의 스키마 커스텀 시 활용
            - 형태별 적용위치, 동시 적용 시 우선순위 등을 알지 못해 오적용 했을 시 에러 발생 (적용 우선순위: method > viewset > serializer)

  - 극복 방법 (Trouble shooting)
    - drf-spectacular
      - 공식문서 활용
      - 관련 내용을 다룬 기술 블로그 참조
    

# 7. 추가 및 리서치 하고 싶은 기능
  - drf-spectacular
    - View 클래스 내부 메소드 단위의 schema를 일괄적으로 적용한 것에 대한 아쉬움 존재
    - 단순 적용 및 담당 serializer를 request/response하여 api 동작을 확인하는 것에 추가로, 메소드별 커스터마이징 추가적용 희망
      - 커스터마이징 시 각 파라미터별 역할과 사용법을 좀 더 익혀 서비스 개발 시 협업에 큰 도움이 되는 drf-spectacular에 대한 이해도와 활용 스킬을 증진하고자 함


# 8. 프로젝트 소감 (어려웠던 점 & 배운점 & 향후 계획)
  - 어려웠던 점 (trouble shooting)
  - 배운점
  - 향후 계획
