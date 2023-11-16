# Sistema de login com interface gráfica utilizando TkInter no Python
![image](https://github.com/iagomauricioo/Projeto_Lab2/assets/118476701/122bc570-1adc-4a20-a458-889927fb9992)


O sistema conta com uma integração com o Google authenticator (utilizando uma lib chamada "pyotp") 💻

![image](https://github.com/iagomauricioo/Projeto_Lab2/assets/118476701/6f4843f0-875e-4039-9b8f-33c5e156ecc2)

Quando o usuário entra como administrador, gera um Qr Code que quando escaneado irá gerar uma 'sala' no aplicativo "Google authenticator".
Já no aplicativo você poderá pegar o código que foi gerado e logar como administrador do sistema, assim, poderemos ter uma verificação de 2 etapas.

Neste projeto não utilizei banco de dados, os usuários serão salvos em arquivos .txt, porém, em breve irei atualizar esse programa fazendo com que haja uma interação com um banco de dados.

##📘 Nesse projeto abordei assuntos importantes de programação, como:
- Tratamento de exceções
- Trabalhar com interfaces gráficas
- Autenticar usuários
- Modularização de aplicações
- Uso de bibliotecas importantes (os, json, tkinter...)

![image](https://github.com/iagomauricioo/Projeto_Lab2/assets/118476701/d9f0c891-acbb-4fc9-9af3-39701f0bc78d)

Nessa tela você pode observar um 'toplevel' da tela principal (root) para registrar os usuários.

