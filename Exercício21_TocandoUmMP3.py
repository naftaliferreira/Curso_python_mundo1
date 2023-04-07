""" Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3. 
 É necessário inserir o arquivo de áudio na mesma pasta onde o arquivo .py está armazenado 
 Para saber o local de origem basta usar: """


# bilbiotecas
import pygame
import os

# iniciando o programa e informando a localização do arquivo de áudio

pygame.init()
pygame.mixer.init()

# carregando a música, caso mude de pasta é necessário mudar o endereço abaixo
projeto_dir = 'C:\Apenas Projetos de Programação\Curso_python_mundo1'
musica_dir = os.path.join(projeto_dir, projeto_dir)
nome_musica = 'pink_floyd.mp3'
caminho_musica = os.path.join(musica_dir, nome_musica)

# iniciando a música
pygame.mixer.music.load(caminho_musica)
pygame.mixer.music.play()


# encerrar biblioteca
while pygame.mixer.music.get_busy():
    pass

pygame.quit()

