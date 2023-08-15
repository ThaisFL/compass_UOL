# **COMANDOS FUNDAMENTAIS LINUX**
> Devido ao tamanho do curso Linux e a diversidade de comandos e detalhes, criei este documento para um resumo completo sobre os comandos fundamentais do Linux, com mais detalhes que o resumo no README.

- __`ls`__ - informa os diretórios/arquivos e seus conteúdos;
    * __`ls -l`__: mostra todos os arquivos e pastas em detalhes;
    * __`ls -a`__: arquivos ocultos;
    * __`ls -lh`__: tamanho dos arquivos;
    * __`ls -ltr`__ : data de modificação do arquivo;
    * __`ls - l /<diretório/`__: lista arquivos do diret;
    * __`ls -lr /<diretório>/`__: lista arq. em ordem decrescente;
    * __`l -R `__: todos os diretórios e seus arq.;

- __`cd <diretório>`__ - mudar de diretório;
    * __`cd /`__: informa todos os diretórios disponíveis na raiz;
    * __`cd /diretorio1/ /diretorio2/`__: passa para outro diretório;
    * __`cd ..`__: volta ao diretório anterior; ou ‘_cd .. / .. /_’ para voltar mais diretórios
    * __`cd -`__: voltar o último diretório;

- __`clear`__ : limpa a tela do terminal;

- __`cat`__ : conteúdo de um arquivo;
    * __`cat -n `__: conteúdo com linhas numeradas;

- __`touch`__ : muda a hora de atualização do arquivo e/ou criar arquivo vazio;

- __`man <nome do comando>`__ : manual de um comando;


## __*GERENCIAR ARQUIVOS E DIRETÓRIOS:*__

- __`mkdir <nome do diret.>`__ : criar novo diretório;
    * __`mkdir -v`__: específica o que está acontecendo no comando;
    * __`mkdir -p <dir1>/<dir2>/<dir3>`__: criar diretório dentro de outro diretório;

- __`rm`__: remove diretórios ou (vários) arquivos;
    * __`rm -dv`__: remove diretório vazio;
    * __`rm -rfv`__: remove diretórios com arquivos dentro;

- __`rmdir`__: remove apenas diretórios do sistema;

- __`cp <diret.>`__ : copiar diretórios;
    * __`cp <arq> <diret.>`__: copia o arquivo na pasta selecionada;

- __`mv <arq> <diret.>`__: mudar o arquivo de diretório ou renomear;

- __`pwd`__: informa o diretório onde você está;


## __*GERENCIAMENTO DE PACOTES:*__

- __`sudo apt upgrade`__:  atualiza todos os repositórios de app; fazendo o comando pela 2 vez ele atualiza os pacotes;

- __`sudo apt install <nome app>`__: install aplicativo na máquina;

- __`sudo apt purge <nome app>`__: remove aplicativo;

- __`sudo apt dist-upgrade`__: atualiza para a última versão;
obs.: não recomendável usar pois o pc pode não acompanhar a atualização;

-__`sudo apt autoremove`__: limpar pacotes/aplicativos desnecessários;

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

- __`tar__`: comando para compactar arquivos
   * __`tar -c`__ - criar arquivo;
   * __`tar -czv`__ -  mostra o progresso da compressão ;
   * __`tar -czvf`__ - especificar o nome do arquivo;
   * __`tar -czvf <arquivo>.tar.gz <diretorio>`__ - compactar
   * __`tar -xzvf <arquivo>.tar.gz`__ - descompactar.  

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