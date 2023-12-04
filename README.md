# Sistema de login com interface gráfica utilizando TkInter no Python
![image](https://github.com/iagomauricioo/Projeto_Lab2/assets/118476701/98bea3ba-6f8e-4b18-b47c-15473c80359b)



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


CRUD
C - CREATE (criar)
R - READ (selecionar/ler)
U - UPDATE (alterar)
D - DELETE (apagar)

![image](https://github.com/iagomauricioo/Projeto_Lab2/assets/118476701/d9f0c891-acbb-4fc9-9af3-39701f0bc78d)
Função CREATE (if not exists) para registrar os usuários. Nesse printscreen você pode observar um 'toplevel' da tela principal (root).

![image](https://github.com/iagomauricioo/Projeto_Lab2/assets/118476701/f0753b1e-d88a-4242-b2fe-48fde2391cd2)
Função READ do código ao clicar no botão 'ver usuários'. Podemos observar os nicknames dos usuários cadastrados.

![image](https://github.com/iagomauricioo/Projeto_Lab2/assets/118476701/8de11eb3-c628-47ce-b860-eb57d63e51ba)
Função UPDATE do código, alterando o apelido do usuário caso digite a senha correta.

![image](https://github.com/iagomauricioo/Projeto_Lab2/assets/118476701/1f54c721-c2b6-4021-9195-45c0d9ff9ad2)
Função DELETE do código, deletando o usuário escolhido do banco de dados.

![image](https://github.com/iagomauricioo/Projeto_Lab2/assets/118476701/11aaaaa5-6d51-4dc7-adf5-a45073a79254)
Conceitos de orientação à objetos 👆




