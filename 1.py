#!/python/python3.4/bin/python3

def translate(phrase):
    trantab = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
    translation = phrase.translate(trantab)
    return translation


if __name__ == "__main__":
    phrase = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

    print(translate(phrase))
    print("For next go to http://www.pythonchallenge.com/pc/def/%s.html" % translate("map"))

