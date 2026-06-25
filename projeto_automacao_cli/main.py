import os
from datetime import datetime

#Limpar a tela
os.system("cls") #clear screen

print(datetime.now())
hora = datetime.now().hour

if hora < 12:
    mensagem = "Bom dia!"

elif hora < 18:
    mensagem = "Boa tarde!"

else:
    mensagem = "Boa noite!"

os.system(f"Start cmd /k echo {mensagem}")