def ozelKarakterVarmi(string, secim):
    ozelKarakterler = "~`!#$%^&*()+=}{[]|\/:;\"'<>,.?"
    ozelKarakterler2 = "~`!@#$%^&*()-_+=}{[]|\/:;\"'<>,?"
    ozelKarakterler3 = "~`!@#$%^&*()-_+=}{[]|\/:;\"'<>.,?"
    if secim == 1:
        for i in range(len(string)):
            for j in range(len(ozelKarakterler)):
                if string[i] == ozelKarakterler[j]:
                    return True
    elif secim == 2:
        for i in range(len(string)):
            for j in range(len(ozelKarakterler2)):
                if string[i] == ozelKarakterler2[j]:
                    return True
    elif secim == 3:
        for i in range(len(string)):
            for j in range(len(ozelKarakterler3)):
                if string[i] == ozelKarakterler3[j]:
                    return True

    return False

def mailDogrula(email, uzunluk):
    if '@' not in email:
        return False
    elif email.count('@') > 1:
        return False
    elif len(email.split('@')[0]) == 0:
        return False
    elif len(email.split('@')[1]) == 0:
        return False
    elif len(email.split('.')[1]) != uzunluk:
        return False
    elif ozelKarakterVarmi(email.split('@')[0], 1):
        return False
    elif ozelKarakterVarmi(email.split('@')[1], 2):
        return False
    elif ozelKarakterVarmi(email[-1], 3):
        return False
    elif email.count('.') > 2:
        return False
    elif uzunluk > 3:
        return False
    
    return True

uzanti_u = int(input("Uzantinin uzunlugu: "))
mail = input("Mail adresi: ")

if mailDogrula(mail, uzanti_u):
    print('Mail adresiniz dogrudur.')
else:
    print('Mail adresiniz yanlistir.')