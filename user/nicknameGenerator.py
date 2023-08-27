import random

class Nickname_generator():
    adjectives = [
        "친절한", "밝은", "온화한", "낙천적인", "쾌활한", "활기찬", "긍정적인",
        "열정적인", "자신감 있는", "사려깊은", "따뜻한", "관대한", "유쾌한", 
        "참을성 있는", "남다른", "진취적인", "끈기 있는", "협조적인","고요한", 
        "창의적인", "영감을 주는", "온정적인", "겸손한","자상한", "격려하는",
        "희망적인", "화합하는", "자유로운", "낭만적인", "사랑스러운", "포용력 있는", "귀여운",
        "용기 있는", "진실된", "확신하는", "고마워하는", "웃음이 많은",
        "경쾌한", "열렬한", "믿음직한", "생기있는", "미소가 매력적인", "인기 있는",
        "충실한", "사교적인", "즐거운", "독립적인", "용감한", "대담한", "자유분방한", "흥겨운", "솔직한",
        "협동하는", "다정한", "자발적인", "존중하는", "품위 있는", "헌신적인", "성실한", "건강한"
    ]

    animals = [
        "호랑이", "사자", "코끼리", "기린", "코뿔소",
        "원숭이", "하마", "악어", "뱀", "원앙",
        "펭귄", "고릴라", "토끼", "쥐", "강아지",
        "고양이", "말", "소", "양", "돼지",
        "오리", "칠면조", "닭", "타조", "물개",
        "돌고래", "상어", "고래", "참치", "해파리",
        "문어", "새우", "거북이", "앵무새", "다람쥐",
        "너구리", "북극곰", "캥거루", "코알라", "판다"
    ]

    def set_4_digit_code():
        random_code = "000" + str(random.randint(1, 9999))
        return random_code[-4:]

    def roll_the_dice():
        random_adjective = random.choice(Nickname_generator.adjectives)
        random_animal = random.choice(Nickname_generator.animals)
        random_code = Nickname_generator.set_4_digit_code()

        nickname = random_adjective + " " + random_animal + "#" + random_code

        return nickname