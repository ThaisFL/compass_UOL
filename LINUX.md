**COMANDOS FUNDAMENTAIS LINUX**

- __ls__ - informa os diretórios/arquivos e seus conteúdos;
- __ls -l__ : mostra todos os arquivos e pastas em detalhes;
ls -a : arquivos ocultos;
ls -lh : tamanho dos arquivos;
ls -ltr : data de modificação do arquivo;
ls - l /<diretório/: lista arquivos do diret;
ls -lr /<diretório>/: lista arq. em ordem decrescente;
l -R : todos os diretórios e seus arq.;

cd <diretório> - mudar de diretório;
cd / : informa todos os diretórios disponíveis na raiz;
cd /diretorio1/ /diretorio2/: passa para outro diretório;
cd .. : volta ao diretório anterior; ou ‘cd .. / .. /’ para voltar mais diretórios
cd - : voltar o último diretório;

clear : limpa a tela do terminal;
cat  : conteúdo de um arquivo;
cat -n  : conteúdo com linhas numeradas;

touch : muda a hora de atualização do arquivo e/ou criar arquivo vazio; 
man : manual de um comando;


Gerenciar arquivos e diretórios:
mkdir <nome do diret.>: criar novo diretório; 
mkdir -v: específica o que está acontecendo no comando;
mkdir -p <dir1>/<dir2>/<dir3>: criar diretório dentro de outro diretório;

rm: remove diretórios ou (vários) arquivos;
rm -dv: remove diretório vazio;
rm -rfv: remove diretórios com arquivos dentro;

rmdir: remove apenas diretórios do sistema;

cp <dir>: copiar diretórios;
cp <arq> <dir>: cópia arquivo na pasta selecionada;

mv <arq> <dir>: mudar o arquivo de diretório ou renomear;

pwd: informa o diretório onde você está;


Gerenciamento de pacotes: 
sudo apt upgrade:  atualiza todos os repositórios de app; fazendo o comando pela 2 vez ele atualiza os pacotes;
sudo apt install <nome app>: install aplicativo na máquina;

sudo apt purge <nome app>: remove aplicativo;

sudo apt dist-upgrade: atualiza para a última versão;
obs.: não recomendável usar pois o pc pode não acompanhar a atualização;

sudo apt autoremove: limpar pacotes/aplicativos desnecessários;

apt-cache search <nome do pacote>: pesquisar por pacotes/aplicativos;





Principais diretórios do sistema Linux: diretório = pasta.
bin - pasta com arquivos binários; executa o shell;
boot - arquivos que auxiliam na inicialização do sistema;
dev - representa todos os dispositivos de entrada e saída do sistema; usb;
etc - arquivos de configuração;
home - diretório de todos os usuários;
lib - arquivos de bibliotecas;
média - responsável por apresentar as pastas;
opt -  arquivos para aplicações não oficiais;
sbin - arquivos binários de inicialização do sistema;
tmp - arquivos descartáveis;
usr - arquivos no modo leitura; não é editável;
var - arquivos de log (erro); arq variáveis;


