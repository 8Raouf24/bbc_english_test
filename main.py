from playsound import playsound
import random

corpus = {"Compréhension Orale":
          [{"F:\\Raouf\\BBC\\07 - YOLO.mp3": ("Listen to the audio and choose the right answer", [
              ("1-Gims", 1), ("2-Booba", 0), ("3-La fouine", 0), ("4-Dinos", 1)])},
           {"F:\\Raouf\\BBC\\07 - YOLO.mp3": ("Listen to the audio and choose the right answer", [
               ("1-ziak", 1), ("2-auz", 0), ("3-freeze", 0), ("4-hamza", 1)])},
           {"F:\\Raouf\\BBC\\07 - YOLO.mp3": ("Listen to the audio and choose the right answer", [
               ("1-kaaris", 1), ("2-XVbabar", 0), ("3-ninho", 0), ("4-SCH", 1)])}],
          "Compréhension de l'écrit":
          [{"Adel is a student is a First year Master Student in IA ": ("What does adel study at College ?", [
              ("1-Biology", 0), ("2-IA", 1), ("3-Geology", 0), ("4-Psychology", 0)])},
           {"Ahmed is a student is a First year Master Student in IA ": ("What does adel study at College ?", [
               ("1-stat", 0), ("2-math", 1), ("3-algebre", 0), ("4-Bio", 0)])},
           {"raouf is a student is a First year Master Student in IA ": ("What does adel study at College ?", [
               ("1-Bio", 0), ("2-stat", 1), ("3-info", 0), ("4-Psychology", 0)])}],
          "Structure de langue":
          [{"We .... go check if the exam's results are out": ("Fill the gap with the corresponding word", [("1-should", 1), ("2-could", 0), ("3-would", 0), ("4-want", 1)])},
           {"We .... to go check on her tomorrow, she will be abroad after that for a while": (
               "Fill the gap with the corresponding word", [("1-have", 1), ("2-could", 0), ("3-would", 0), ("4-want", 1)])},
           {"wait, where is my phone i'm sure i .... it here ": ("Fill the gap with the corresponding word", [("1-left", 1), ("2-right", 0), ("3-ate", 0), ("4-went", 1)])}]
          }


""" def test(corpus):
    print("\nWelcome to your english level test!\n Please before starting, identify yourself\n#########\n")
    # print("ID :")
    # ID = input()
    # print("Password:")
    # password = input()
    print(f"\n   you are ready to start your test. Let's dive in !\n ")
    cpt_tr = 0
    cpt = 0
    for i in corpus.keys():
        print(f"######## {i} ########\n")
        for j in corpus[i]:
            if i == "Compréhension Orale":
                pass
                # playsound(list(j.items())[0][0])
            else:
                print(list(j.items())[0][0])
            print(list(j.items())[0][1][0])
            for k in list(j.items())[0][1][1]:
                print(k[0])
            answer = input()
            cpt_tr += list(j.items())[0][1][1][int(answer)-1][1]
            cpt += 1
    print(f"Votre score est de {cpt_tr}/{cpt}") """


def fetch_questions(corpus, Number):  # returns a reduced dic with the same structure
    _corpus = {list(corpus.keys())[i]: random.sample(
        corpus[list(corpus.keys())[i]], k=Number) for i in range(3)}
    return _corpus

# returns the score of one question that it takes as input.


def answer_question(question):
    key = list(question.keys())[0]
    quest = question[key][0]
    answers = question[key][1]
    print(key)
    print(quest)
    """ if i == "Compréhension Orale":
        pass """
    print('possible answers : ')
    for i in answers:
        print(i[0])
    # wait
    answer = input("what's is your answer: ")
    return answers[int(answer)-1][1]


def module_Answers(module):
    questions = list(module.values())[0]
    score = 0
    for i in questions:
        score = score + answer_question(i)
    return score


def run_exam(corpus):
    for i in list(corpus.keys()):
        _temp = {i: corpus[i]}
        module_Answers(_temp)


question = {'F:\\Raouf\\BBC\\07 - YOLO.mp3': ('Listen to the audio and choose the right answer', [
    ('1-ziak', 0), ('2-azur', 0), ('3-freeze', 0), ('4-hamza', 1)])}
module = {"Compréhension Orale":
          [{"F:\\Raouf\\BBC\\07 - YOLO.mp3": ("Listen to the audio and choose the right answer", [
              ("1-Gims", 1), ("2-Booba", 0), ("3-La fouine", 0), ("4-Dinos", 1)])},
           {"F:\\Raouf\\BBC\\07 - YOLO.mp3": ("Listen to the audio and choose the right answer", [
               ("1-ziak", 1), ("2-auz", 0), ("3-freeze", 0), ("4-hamza", 1)])},
           {"F:\\Raouf\\BBC\\07 - YOLO.mp3": ("Listen to the audio and choose the right answer", [
               ("1-kaaris", 1), ("2-XVbabar", 0), ("3-ninho", 0), ("4-SCH", 1)])}]}
# print(fetch_questions(corpus, 2))
# print(answer_question(question))
# run_exam(corpus)
