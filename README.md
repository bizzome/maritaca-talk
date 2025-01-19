# Maritaca Talk

**Maritaca Talk** é um projeto criado para testar e explorar as funcionalidades do modelo de linguagem **Maritaca**. Ele é gerenciado utilizando o **uv**, uma ferramenta eficiente para controle de ambientes Python e execução de scripts.

## Pré-requisitos

Antes de começar, certifique-se de que o seguinte está instalado em sua máquina:

- Python 3.8 ou superior
- `uv` (Universal Virtualenv) - para instalar, execute:
  ```bash
  pip install uv
  ```
- Git (opcional, caso você queira clonar este repositório)

## Instalação

1. Clone o repositório (se aplicável):
   ```bash
   git clone https://github.com/bizzome/maritaca-talk.git
   cd maritaca-talk
   ```

2. Inicialize o ambiente usando o **uv**:
   ```bash
   uv init
   ```

## Uso

### Executando o projeto

Após configurar o ambiente, você pode iniciar o Maritaca Talk executando o comando abaixo:

```bash
uv run main.py
```

Certifique-se de que o arquivo `main.py` contém o código principal para interagir com o modelo Maritaca.

### Scripts úteis

- **Exportar dependências para requirements:**
  ```bash
  uv pip freeze > requirements.txt
  ```


## Contribuindo

Se você deseja contribuir para o desenvolvimento do Maritaca Talk:

1. Faça um fork deste repositório.
2. Crie um branch para sua feature/bugfix:
   ```bash
   git checkout -b minha-feature
   ```
3. Envie suas alterações:
   ```bash
   git commit -m "Descrição das alterações"
   git push origin minha-feature
   ```
4. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença [MIT](LICENSE).
