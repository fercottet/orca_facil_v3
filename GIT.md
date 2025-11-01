## Iniciar novo repositório
> git init


## Esse comando mostra se o seu repositório local está conectado ao GitHub.
> git remote -v

Você deve ver algo como: \
origin https://github.com/seu-usuario/nome-do-repositorio.git (fetch) \
origin https://github.com/seu-usuario/nome-do-repositorio.git (push)


## Para o primeiro envio, utilize:
> git push -u origin main

Substitua 'main' por 'master' ou pelo nome do branch \
O parâmetro -u cria o vínculo entre o branch local e o remoto.


## Para enviar um commit (alteração) ao GitHub (histórico de mudanças):
> git add . \
> git commit -m " Uma frase que resuma das mudanças " \
> git pull --rebase origin main \
> git push origin main

O '--rebase' mantém o histórico linear e evita “commits de merge” desnecessários.


## Automatizar o 'rebase' (Assim, git pull usará automaticamente --rebase)
> git config --global pull.rebase true


## Para baixar o código do GitHub (baixar a versão mais atual):
> git pull


## Visualizar histórico de commits (cópias dos métodos e módulos):
Lista simples:
> git log --oneline

Lista completa:
> git log


## Descartar mudanças não commitadas:
Em um arquivo específico:
> git restore nome_do_arquivo

Em todos os módulos:
> git restore .


## Restaurar um commit (substitua <hash> pelo hash do commit):
Visualizar como estava no momento do commit (sem mudar nada):
> git checkout <hash>

Fazer o reset para o momento do commit (descarta código atual):
> git reset --hard <hash>>

⚠️ **Esse comando é destrutivo: apaga tudo o que veio depois do hash.**


## Criar nova Branch (ramificação):
> git checkout -b <nome da nova ramificação>

⚠️ **Tudo que for feito (commits, alterações, testes) vai só nessa branch.**

## Mesclar uma Branch com o código principal:
> git checkout main \
> git merge <nome da nova ramificação>


## Clonar um repositório:
> git clone https://github.com/fercottet/orca_facil.git

## Em caso de erro: fatal: refusing to merge unrelated histories
> git pull origin main --allow-unrelated-histories


## Apagar histórico de commits localmente 
No Power Shell, dentro da pasta raiz do projeto:
> rmdir -Force -Recurse .git 
