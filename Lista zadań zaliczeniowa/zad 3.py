from Question import Question
question = [
    "Ile megabajtów w gigabajtach?\n(a) 1020 \n(b)1024/1000 \n(c)10000\nPodaj swoją odpowiedź: ",
    "Jaką bibliotekę należy zaimportować, aby pracować z kalendarzem? \n(a) calendar\n(b) time\n(c) datatime\nPodaj swoją odpowiedź: ",
    "Co jest większe 2 gigabajty lub 2 megabajty?\n(a)Це одне і те саме!!! \n(b)2Mb \n(c)2Gb\nPodaj swoją odpowiedź: ",
    "Jakiego języka programowania uczysz się teraz?\n(a)Python \n(b)C# \n(c)PHP\nPodaj swoją odpowiedź: ",
    "Który język programowania jest najpopularniejszy?\n(a)HTNL \n(b)PHP \n(c)JavaScript\nPodaj swoją odpowiedź: ",
    "Ile mniej więcej istnieje języków programowania?\n(a)<5000 \n(b)1000-10k \n(c)>10k\nPodaj swoją odpowiedź: ",
    "Python-język, który jest ...?\n(a)Interpretowany \n(b)Żadna z opcji nie jest słuszna! \n(c)Kompilowany\nPodaj swoją odpowiedź: ",
    "Jakie znasz zasady programowania?\n(a)Refleksja \n(b)Introspektywna \n(c)Introspektywna, Refleksja\nPodaj swoją odpowiedź: ",
    "Lubisz koty?\n(a)Tak!!!\nPodaj swoją odpowiedź: "
]

questions = [
    Question(question[0], "b"),
    Question(question[1], "a"),
    Question(question[2], "c"),
    Question(question[3], "a"),
    Question(question[4], "c"),
    Question(question[5], "b"),
    Question(question[6], "a"),
    Question(question[7], "c"),
    Question(question[8], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        odpowiedź = input(question.pytanie)
        if odpowiedź == question.odpowiedź:
            score += 1
    print("Masz " + str(score) + " punkt/punktów/punkty z " + str(len(questions)) + " punktów!")


run_test(questions)