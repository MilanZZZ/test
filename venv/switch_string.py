

pass3 = "koe"
password = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
pass_list = list(password)
password_reveal= ", ".join(pass_list)
#print(pass_list)
password_reveal1=(password_reveal.replace('k','-').replace('k','m').replace('-','m'))
password_reveal2=(password_reveal1.replace('o','-').replace('o','q').replace('-','q'))
password_reveal3=(password_reveal2.replace('e','-').replace('e','g').replace('-','g'))
password_reveal4=(password_reveal3.replace('k','-').replace('k','m').replace('-','m'))
password_reveal5=(password_reveal4.replace('o','-').replace('o','q').replace('-','q'))
password_reveal6=(password_reveal5.replace('e','-').replace('e','g').replace('-','g').split(", "))

print(str(password_reveal6))

def listaUstring(lista):
    string = "";
    for i in lista:
        string += i
    print(string)
    return string

listaUstring(password_reveal6)