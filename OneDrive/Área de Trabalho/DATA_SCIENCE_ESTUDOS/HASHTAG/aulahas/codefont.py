
import pyautogui
import time
import pandas 
from plyer import notification


pyautogui.PAUSE = 0.5

# Step 1: Open the Company system
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3) # Wait 3 seconds


# Step 2: Login
pyautogui.click(x=635, y=521)
pyautogui.write("joanatrindade@gmail.com")
time.sleep(2)
pyautogui.press("tab")
pyautogui.write("12345678")
pyautogui.press("tab")
pyautogui.press("enter")


# Passo 3: Import the products database 
pandas.read_csv("produtos.csv")
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=693, y=375)
    
    # Product code
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    
    # Product brand
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    
    # Product type
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    
    # Product category
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    
    # Product unit price 
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    
    # Product cost
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    
    # Observations
    obs = str(tabela.loc[linha, 'obs']) 
    if obs != "nan": # If observation is not empty
        pyautogui.write(obs) # Write the observation
    pyautogui.press('tab')

    # Save
    pyautogui.press('enter')
    pyautogui.scroll(1000) # Scroll down
    

