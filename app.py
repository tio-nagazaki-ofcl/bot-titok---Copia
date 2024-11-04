#-passos-manuais-em-sequencia,-dps-tonar-cada-passo- em-um-codigo-python
#quais-são-os-passo-manuas
#1- navegar-ate-o-site-tiktiok = "https://www.tiktok.com/@achados.shopee.hirosh?lang=en"
import webbrowser, pyautogui
from time import sleep
webbrowser.open("https://www.tiktok.com/foryou?lang=pt-BR")
sleep(5)
#2- clicar-em-login
pyautogui.click(1833,139,duration=2)
sleep(3)
#3- cliacar-em-logar-com-email
pyautogui.click(1465,513,duration=3)
sleep(3)
#4- clicar-em-logar-com/usarname
pyautogui.click(1468,455,duration=2)
sleep(3)
#5- digitar-email/usarname-e-senha
pyautogui.click(1339,469,duration=2)
pyautogui.write('raphael2007.99@gmail.com')
sleep(4)
pyautogui.click(1406,519,duration=2)
pyautogui.write('K<hyx8,.&]B*^j;')
sleep(4)
#6- clicar-em-login
pyautogui.click(1330,575,duration=2)
sleep(5)
#7- navegar-ate-a-pagina = "https://www.tiktok.com/@achados.shopee.hirosh?lang=en"
webbrowser.open('https://www.tiktok.com/@keniapimentapatroa3642')
sleep(5)
#8- clicar na postagem mais recente
pyautogui.click(1213,533,duration=2)
sleep(5)
#9- verificar se o videos foi curtido
for video in range(10):
    imagem = pyautogui.ImageNotFoundException('curtida.png')
    if imagem:
        #pule para o proximo video
        pyautogui.click(1584,288,duration=2)
        sleep(5)
        pyautogui.click(1530,577,duration=2)
    else:
        # codigo para curtir o videos
        sleep(5)
        pyautogui.click(1530,577,duration=2)
        pyautogui.click(1587,293,duration=2)
#se foi curtido passar para o proximo video
#se não foi curtido, curtir este video e passar para o proximo video
#10- repitir por quantas vezes quiser