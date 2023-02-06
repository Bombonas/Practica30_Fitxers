def save_dict(lines):
    dic = {}
    for line in lines:
        data = line.split("; ")
        dict_aux = {"brand": data[0], "model": data[1], "CPU": data[2], "speed": int(data[3]), "price": float(data[4][:-1])}
        dic.update({data[0][:3] + "-" + data[1]: dict_aux})
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

