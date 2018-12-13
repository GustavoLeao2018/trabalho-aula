# Git comandos básicos

Os comandos básicos para a criação e manutenção de um repositório git são os  seguintes:

## Comandos básicos
### Comandos de configuração
#### Adicionando um email e usuário
Para adicionar um email global ao usuário git use o comando abaixo:
```bash
git config --global user.email "seu_email@servidor.com"
```
Para adicionar um nome ao seu usuário git use o comando:
```bash
git config --global user.name "seu_nome"
```
#### Saídas do git coloridas
Para todas as informações que são resultados dos comandos serem mostradas coloridas faça como abaixo:
```bash
git config color.ui true
```


### Inicializando o repositório
Sempre que formos inicializar o repositório local em nossa máquina executamos o comando abaixo:
```bash
git init
```

### Visualizando o status
Sempre que queremos ver como nosso repositório local está, vemos executar:
```bash
git status
```

### Adicionando os arquivos
#### Informando ao Git
Sempre que adicionarmos algum arquivo, ou mais, para que o git saiba que foram adicionados, digite o comando:
```bash
git add .
```
> Caso seja adicionar apenas um arquivo, digite `git add nome_do_arqivo.extensão`.
> Tabém pode ser utilizado no lugar do __.__ o __*__ ficando `git add *`.

#### Salvando os arquivos
Para salvarmos os arquivos devemos digitar:
```bash
git commit -m "Texto a ser salvo!"
```
> O texto em aspas deve se referir ao que foi adicionado, ou alterado nos arquivos.

### Enviando para o repositório remoto
#### Adicionando o repositório
Para adicionarmos o repositório:
```bash
git remote add origin http://github.com/seu_usuario/repositorio.git
```
#### Enviando os arqivos para os programas
Para enviarmos e sincronizar o repositório, digite:
```bash
git push -u origin master
```
## Comandos avançados
### Atualizar o repositório
Para atualizar o repositório local (e mesclar) deve ser executado o comando:
```bash
git pull
```

### Mesclar o repositório
Para mesclar de um branch específico ou do principal (master), execute:
```bash
git merge master
```

### Clonando um repositório
Para clonar e baixar devemos digitar:
```bash
git clone http://github.com/seu_usuario/repositorio.git
```

### Arquivo de ignoração
Para criar um arquivo para ignorar arquivos que **não** serão enviados para o repositório e deve ser chamado:

**.gitignore**
