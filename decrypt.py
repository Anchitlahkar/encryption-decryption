import pandas as pd
import os
import time

encryptionkey = pd.read_csv(r"Encrypted keys\decodekeynew.csv",
                            sep=',', names=['Character', 'Byte'], header=None, skiprows=[0])

df = pd.DataFrame(data=encryptionkey)

df['Character'] = df['Character'].astype(str)
df['Byte'] = df['Byte'].astype(str)


def decode_message(message):
    new_word = ''
    decoded_message = []

    for i in range(0, len(message), 2):
        j = message[i:i + 2]
        index_nb = df[df.eq(j).any(1)]

        df2 = index_nb['Character'].tolist()

        s = [str(x) for x in df2]

        decoded_message = decoded_message + s

    new_word = ''.join(decoded_message)

    return new_word


def Decrypt(coded_message):
    try:
        coded_message_str = str(coded_message)
    except:
        coded_message_str = coded_message
        pass

    return decode_message(coded_message_str)
