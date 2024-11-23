# TeamRandomizer

Este projeto visa criar times de forma aleatória, balanceada e com base em algumas regras, como garantir que cada time tenha pelo menos uma mulher, exceto em situações específicas. O sistema também permite a geração de times de acordo com o número de jogadores e um identificador de semana, e evita a repetição de jogadores nos times de semanas subsequentes.

# Funcionalidades
Gerar times aleatórios: O sistema gera entre 3 e 4 times com jogadores disponíveis, considerando a necessidade de ter pelo menos uma mulher em cada time (exceto quando o número de mulheres for menor que 4).
Validação do número de jogadores: O número de jogadores é validado para garantir que seja suficiente para formar os times.
Armazenamento de times gerados: Todos os times gerados são salvos em um arquivo JSON com um identificador único para cada semana, garantindo que os times de semanas anteriores não se repitam.
Entrada interativa: O número de times e o identificador da semana são definidos de forma interativa pelo usuário.

# Tecnologias Usadas
Python 3.x

# Bibliotecas:
random: Para embaralhar os jogadores e formar os times aleatoriamente.
csv: Para carregar os dados dos jogadores a partir de um arquivo CSV.
json: Para salvar os times gerados em um arquivo JSON.

# Estrutura do projeto
team-randomizer/
│
├── data/
│   ├── players.csv             # Arquivo com os dados dos jogadores
│   └── previous_teams.json     # Arquivo para armazenar os times gerados
│
├── randomizer/
│   ├── __init__.py
│   ├── team_randomizer.py      # Contém as classes e funções principais para gerar os times
│   └── utils.py                # Funções auxiliares, como validação de jogadores e armazenamento dos times
│
├── main.py                     # Arquivo principal para executar o programa
└── README.md                   # Documentação do projeto

#Como usar:

Clone este repositório para o seu computador:
git clone https://github.com/usuario/team-randomizer.git

Navegue até o diretório do projeto:
cd team-randomizer

Instale as dependências necessárias:

Caso você ainda não tenha o Python 3.x e as bibliotecas necessárias instaladas, crie um ambiente virtual e instale as dependências:
python3 -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
pip install -r requirements.txt

Prepare o arquivo players.csv:

O arquivo players.csv deve conter as informações dos jogadores, incluindo nome, gênero e nível. Um exemplo de formato:
name,gender,level
Ana,F,5
João,M,3
Maria,F,4
Pedro,M,2
Gustavo,M,5
...

Execute o programa:

Após configurar o arquivo players.csv com os dados dos jogadores, basta executar o arquivo main.py:
python main.py
O programa irá pedir para você inserir o número de times (entre 3 e 4) e o identificador da semana (exemplo: week_47_2024), e, em seguida, gerará os times e os salvará no arquivo previous_teams.json.

# Como funciona
Carregar jogadores: O sistema carrega os jogadores a partir de um arquivo CSV.
Validar o número de jogadores: O número de jogadores é validado para garantir que seja suficiente para formar entre 3 e 4 times.
Gerar os times: O sistema gera os times de forma balanceada, considerando a presença de mulheres em cada time.
Salvar os times: Os times gerados são salvos em um arquivo JSON, com o identificador da semana como parte do nome, para evitar repetições de times nas semanas subsequentes.

# Contribuições
Se você deseja contribuir com este projeto, siga estas etapas:

Faça um fork do repositório.
Crie uma branch para sua alteração (git checkout -b feature/nome-da-feature).
Faça o commit das suas alterações (git commit -am 'Adiciona nova funcionalidade').
Envie para o repositório original (git push origin feature/nome-da-feature).
Abra um Pull Request.

# Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.
