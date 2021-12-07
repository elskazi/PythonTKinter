
with open ('C:\\Steam\\steamapps\\common\\dota 2 beta\\game\\dota\\bin\\win32\\client.dll', 'r') as f:
    #f = f.decode('ascii')
    old_data = f.read()

    new_data = old_data.replace('Maximum visible distance    1200', 'Maximum visible distance    1500')
    #f = f.encode('ascii')
with open ('C:\\Steam\\steamapps\\common\\dota 2 beta\\game\\dota\\bin\\win32\\client.dll', 'w') as f:
    f.write(new_data)