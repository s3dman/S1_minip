import local_dh

curr_username,curr_password = None,None
def Login(username,password):
    database = local_dh.ReadDB('DATABASE.DB')
    if username in database['users']:
        if password == Decoder(database['users'][username]):
            global curr_username,curr_password
            curr_username,curr_password=username,database['users'][username]
            return 0
        return -1
    return -2

def Register(username,password):
    database = local_dh.ReadDB('DATABASE.DB')
    if username in database['users']:
        return -1
    database['users'][username] = Encoder(password)
    local_dh.WriteDB(database,"DATABASE.DB")
    return 0

# function to hash/encode password
def Encoder(x):
    y = ''
    for i in x:
        y += str(ord(i))[::-1] + '�'
    return y[::-1]

# function to unhash/decode password
def Decoder(x):
    x = x[::-1].split('�')
    y = ''
    for i in x[:-1]:
        y += chr(int(i[::-1]))
    return y