-Comandos GIT

Criar um repositório Git: git init
Clonar um repositório Git existente: git clone <url_repositorio>
Verificar o status dos arquivos: git status
Adicionar arquivos para o commit: git add <nome_arquivo> 
                               ou git add . 
Commitar mudanças: git commit -m "Mensagem explicando as mudanças"
Ver log de commits: git log
Ver diferenças entre commits: git diff
Atualizar local com github: git pull
Enviar mudanças para github: git push
Ver as Versões Anteriores dos Arquivos: git checkout <hash_commit>


-Configurar GIT

git config user.name "Nome do Aluno"
git config user.email "email@exemplo.com"

Limpar as Credenciais: git config --global credential.helper ""

Excluir a configuração local

git config --unset user.name
git config --unset user.email