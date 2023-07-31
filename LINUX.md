# **COMANDOS FUNDAMENTAIS LINUX**
Devido ao tamanho do curso Linux e a diversidade de comandos e detalhes, criei este documento para um resumo completo sobre os comandos fundamentais do Linux, com mais detalhes que o resumo no README.

- `__ls__` - informa os diretórios/arquivos e seus conteúdos;
    * `__ls -l__ `: mostra todos os arquivos e pastas em detalhes;
    * `__ls -a__ `: arquivos ocultos;
    * `__ls -lh__`: tamanho dos arquivos;
    * `__ls -ltr__` : data de modificação do arquivo;
    * `__ls - l /<diretório/__`: lista arquivos do diret;
    * `__ls -lr /<diretório>/__`: lista arq. em ordem decrescente;
    * `__l -R__ `: todos os diretórios e seus arq.;

- `__cd <diretório>__` - mudar de diretório;
    * `__cd /__ `: informa todos os diretórios disponíveis na raiz;
    * `__cd /diretorio1/ /diretorio2/__`: passa para outro diretório;
    * `__cd ..__`: volta ao diretório anterior; ou ‘_cd .. / .. /_’ para voltar mais diretórios
    * `__cd -__`: voltar o último diretório;

- `__clear__` : limpa a tela do terminal;

- `__cat__` : conteúdo de um arquivo;
    * `__cat -n__ `: conteúdo com linhas numeradas;

- `__touch__` : muda a hora de atualização do arquivo e/ou criar arquivo vazio;

- `__man <nome do comando>__` : manual de um comando;


## __*GERENCIAR ARQUIVOS E DIRETÓRIOS:*__

- `__mkdir <nome do diret.>__` : criar novo diretório;
    * `__mkdir -v__`: específica o que está acontecendo no comando;
    * `__mkdir -p <dir1>/<dir2>/<dir3>__`: criar diretório dentro de outro diretório;

- `__rm__`: remove diretórios ou (vários) arquivos;
    * `__rm -dv__`: remove diretório vazio;
    * `__rm -rfv__`: remove diretórios com arquivos dentro;

- `__rmdir__`: remove apenas diretórios do sistema;

- `__cp <diret.>__` : copiar diretórios;
    * `__cp <arq> <diret.>__`: copia o arquivo na pasta selecionada;

- `__mv <arq> <diret.>__`: mudar o arquivo de diretório ou renomear;

- `__pwd__`: informa o diretório onde você está;


## __*GERENCIAMENTO DE PACOTES:*__

- `__sudo apt upgrade__`:  atualiza todos os repositórios de app; fazendo o comando pela 2 vez ele atualiza os pacotes;

- `__sudo apt install <nome app>__`: install aplicativo na máquina;

- `__sudo apt purge <nome app>__`: remove aplicativo;

- `__sudo apt dist-upgrade__`: atualiza para a última versão;
obs.: não recomendável usar pois o pc pode não acompanhar a atualização;

-` __sudo apt autoremove__`: limpar pacotes/aplicativos desnecessários;

- `__apt-cache search <nome do pacote>__`: pesquisar por pacotes/aplicativos;


## __*GERENCIAMEMTO DE USUÁRIOS E GRUPOS*__
__criar usuário:__  *sudo adduser <usuario novo>*
   * *verificar os usuarios: *teste: ls /home/*

__deletar usuário:__ *sudo userdel --remove <usuario>*

__modificar nome:__ *sudo usermod -c ‘<novo nome>’ <antigo nome>*

__desabilitar usuário:__ *sudo usermod -L <usuário>*

__habilitar:__ *sudo usermod -u <usuário>*

__criar grupos:__ *sudo groupadd -g <número> <nome gr.>*
   * verificar grupos: *getent group*

__deletar grupos:__ *sudo groupdel <grupo>*

__adicionar ou mudar usuário:__ *sudo usermod -a -G <grupo> <usuário>*

__remover usuário:__ *sudo gpasswd -d <usuario> <grupo>*

__virar um super usuario (nao usar o sudo e vira root):__ *sudo su*

__trocar senha de usuário:__ *passwd*


### COMPACTANDO ARQUIVOS NO LINUX

- __tar__ : comando para compactar arquivos
   * __tar -c__ - criar arquivo;
   * __tar -czv__ -  mostra o progresso da compressão ;
   * __tar -czvf__ - especificar o nome do arquivo;
   * __tar -czvf <arquivo>.tar.gz <diretorio>__ - compactar
   * __tar -xzvf <arquivo>.tar.gz__ - descompactar.  

### COMPACTAÇÃO EM ZIP

- compactar: __*zip -r <arquivo>.zip <diretório>*__

- descompactar: __*unzip <arquivo>.zip -d <diretório>*__

# __*Principais diretórios do sistema Linux:*__ 
 diretório = pasta.

* __bin__ - pasta com arquivos binários; executa o shell;
* __boot__ - arquivos que auxiliam na inicialização do sistema;
* __dev__ - representa todos os dispositivos de entrada e saída do sistema; usb;
* __etc__ - arquivos de configuração;
* __home__ - diretório de todos os usuários;
* __lib__ - arquivos de bibliotecas;
* __média__ - responsável por apresentar as pastas;
* __opt__ -  arquivos para aplicações não oficiais;
* __sbin__ - arquivos binários de inicialização do sistema;
* __tmp__ - arquivos descartáveis;
* __usr__ - arquivos no modo leitura; não é editável;
* __var__ - arquivos de log (erro); arq variáveis;