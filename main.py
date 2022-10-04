
import speech_recognition as sr
from PyQt5 import uic, QtWidgets

from sqlalchemy import true

# Função - Gravação de audio e conversão para texto

def reconhecer_fala():

    microfone = sr.Recognizer() # Habilita o microfone

    with sr.Microphone() as source:  

        microfone.adjust_for_ambient_noise(source) # Reducão de ruido disponível na speech_recognition        
        print("Você já pode começar a falar!")     
        audio = microfone.listen(source) # Guarda o audio gravado na variavel 'audio', o audio é finalizado nas pausas grandes

        try:
            frase = microfone.recognize_google(audio,language='pt-BR') # Audio sera interpretado na lingua portuguesa                    
        except:
            print("Não entendi o que você disse!")
        return frase

# Função Botão Gravar

def botao_gravar():

    # Abre arquivo dados.txt para escrita
    
    with open("dados", "a") as arquivo:
        txt_frase = reconhecer_fala().capitalize() + "."
        tela.txt_audio.setText(txt_frase)
        arquivo.write(txt_frase + "\n")

    # Abre arquivo dados.txt para leitura

    with open("dados", "r") as texto:
        dados = texto.read()
        tela.txt_texto.setText(dados)

# Função Botão Limpar

def botao_limpar():

    # Abre arquivo dados.txt para limpar

    with open("dados", "w") as arquivo:
        pass    
    tela.txt_texto.setText("")       

app = QtWidgets.QApplication([])
tela = uic.loadUi("audio_texto.ui")
tela.setFixedSize(400,432) # Tamanho fixo para não aparecer o botão maximizar
tela.bt_gravar.clicked.connect(botao_gravar)
tela.bt_limpar.clicked.connect(botao_limpar)
tela.show()
app.exec()
