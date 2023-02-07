def save_dict(lines):
    dic = {}
    for line in lines:
        data = line.split(";")
        data_clean = []
        for word in data:
            word = word.replace(" ", "")
            data_clean.append(word)
        dict_aux = {"brand": data_clean[0], "model": data_clean[1], "CPU": data_clean[2], "speed": int(data_clean[3]), "price": float(data_clean[4][:-1])}
        print(dict_aux)
        dic.update({data_clean[0][:3] + "-" + data_clean[1]: dict_aux})
    return dic

def tabletsBarats (nomf1, nomf2, p):
    f = open(nomf1, "r")
    lines = f.readlines()
    f.close()
    data_dic = save_dict(lines)
    txt = ""
    for id in data_dic:
        if data_dic[id]["price"] < p:
            txt += id + " "
            if data_dic[id]["speed"] < 500:
                txt += "Baixa\n"
            elif 500 <= data_dic[id]["speed"] <= 900:
                txt += "Mitjana\n"
            elif data_dic[id]["speed"] > 900:
                txt += "Alta\n"
    f = open(nomf2, "w")
    f.write(txt)
    f.close()

tabletsBarats("tablets.txt", "barats.txt", 100)

