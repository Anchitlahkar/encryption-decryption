import pandas as pd
import os

encryptionkey = pd.read_csv(r"Encrypted keys\decodekeynew.csv",
                            sep=',', names=['Character', 'Byte'], header=None, skiprows=[0])

df = pd.DataFrame(data=encryptionkey)

df['Character'] = df['Character'].astype(str)
df['Byte'] = df['Byte'].astype(str)

def split(message):
    return [char for char in message]

def code_message(message_split):
    coded_message = ""

    for i in range(len(message_split)):
        j = message_split[i]
        try:
            coded_char = encryptionkey.loc[encryptionkey['Character'] == j, 'Byte'].iloc[0]
            # print(type(coded_char))

        # To handle if character is not in our decryption list
        except:
            print('unrecognized character')
            coded_char = '@@@'

        coded_message = coded_message + coded_char
    return coded_message


def Encrypt(message):
    message_split = split(message)
    
    coded_message = code_message(message_split)
    encrypt_message = str(coded_message)
    
    return encrypt_message
