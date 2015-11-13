# coding: utf-8

import cryptlib
from collections import defaultdict

def exec_form(ctype, form):
    answer = ""
    other_params = {}

    if ctype == "classic":
        return exec_classic(form)
    elif ctype == "aes":
        return exec_aes(form)

    return form, other_params

def exec_classic(form):
    other_params = {}

    key1 = int(form.key1.data)
    key2 = int(form.key2.data)

    if form.encrypt.data:
        text = form.text.data
        form.text.data = ""
        form.cipher.data = cryptlib.encrypt_affine(text, key1, key2)

    elif form.decrypt.data:
        cipher = form.cipher.data
        form.cipher.data = ""
        form.text.data = cryptlib.decrypt_affine(cipher, key1, key2)

    elif form.stat.data:                                                    # 统计原文/密文中各字符的出现次数
        text = form.text.data.lower()
        cipher = cryptlib.encrypt_affine(text, key1, key2)
        form.cipher.data = cipher

        freq_dict = defaultdict(lambda: [0, 0])
        count = 0
        for c in text:
            if 97<=ord(c)<=122:
                freq_dict[c][0] += 1
                count += 1
        for c in cipher:
            if 97<=ord(c)<=122:
                freq_dict[c][1] += 1
        freq_list = [(x[0].upper(),
                            round(float(x[1][0])/count, 4),
                            round(float(x[1][1])/count, 4))
                         for x in freq_dict.items()]
        other_params["freq_list"] = freq_list

    return form, other_params

def exec_aes(form):
    key = form.key.data
    pc = cryptlib.AESCrypt(key)
    other_params = {}
    if form.encrypt.data:
        text = form.text.data
        form.cipher.data = text

    elif form.decrypt.data:
        cipher = form.cipher.data
        form.text.data = cipher

    return form, other_params
