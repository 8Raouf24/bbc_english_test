

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
