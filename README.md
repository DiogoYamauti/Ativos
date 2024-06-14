# Sistema de Inventário de Ativos de TI

Este projeto é um sistema de inventário de ativos de TI que permite gerenciar informações de funcionários e seus ativos. Ele utiliza Flask como framework web e MongoDB como banco de dados. As operações principais incluem a adição, listagem, consulta, atualização e exclusão de funcionários e seus respectivos ativos.

## Pré-requisitos

Antes de começar, certifique-se de ter o Python e o MongoDB instalados na sua máquina.

- Python
- MongoDB

## Instruções para Instalação e Execução

1. Clone o repositório:
    ```sh
    git clone https://github.com/DiogoYamauti/Ativos
    ```

2. Navegue até o diretório do projeto:
    ```sh
    cd inventario-ti
    ```

3. Crie e ative um ambiente virtual:
    ```sh
    python -m venv venv
    ```

    - No Windows:
        ```sh
        venv\Scripts\activate
        ```

    - No Linux/macOS:
        ```sh
        source venv/bin/activate
        ```

4. Instale as dependências:
    ```sh
    pip install flask pymongo requests
    ```

5. Execute o app.py:
    ```sh
    python app.py
    ```

6. Abra outro terminal e execute o menu:
    ```sh
    python menu.py
    ```

## Estrutura do Projeto

- **app.py**: Servidor Flask que gerencia as rotas da API.
- **db.py**: Conexão com o banco de dados.
- **menu.py**: Script do menu de terminal para interagir com o sistema.

---

Este README deve fornecer uma orientação clara sobre como configurar e executar o seu projeto. Certifique-se de que todos os comandos e instruções estejam corretos e adequados ao ambiente do seu sistema.