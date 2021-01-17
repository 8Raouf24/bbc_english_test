from playsound import playsound
corpus = {"Compréhension Orale":
                [{"F:\\Raouf\\BBC\\07 - YOLO.mp3":("Listen to the audio and choose the right answer",[("1-Gims",1),("2-Booba",0),("3-La fouine",0),("4-Dinos",1)])}],
        "Compréhension de l'écrit":
                [{"Adel is a student is a First year Master Student in IA ":("What does adel study at College ?",[("1-Biology",0),("2-IA",1),("3-Geology",0),("4-Psychology",0)])}],
        "Structure de langue":
                [{"We .... go check if the exam's results are out":("Fill the gap with the corresponding word",[("1-should",1),("2-could",0),("3-would",0)
        ,("4-want",1)])}]}

def test(corpus):
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
                                #playsound(list(j.items())[0][0])
                        else:
                                print(list(j.items())[0][0])
                        print(list(j.items())[0][1][0])
                        for k in list(j.items())[0][1][1]:
                                print(k[0])
                        answer = input()
                        cpt_tr += list(j.items())[0][1][1][int(answer)-1][1]
                        cpt +=1
        print(f"Votre score est de {cpt_tr}/{cpt}")





test(corpus)


        