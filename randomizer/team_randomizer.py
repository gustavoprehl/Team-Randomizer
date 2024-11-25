import random
from collections import defaultdict

class TeamRandomizer:
    def __init__(self, players, num_teams, week_identifier):
        self.players = players
        self.num_teams = num_teams
        self.week_identifier = week_identifier

    def generate_teams(self):
        """
        Gera times onde cada time tem uma mulher (se possível), os níveis são balanceados,
        e os jogadores extras são colocados no último time, se necessário.
        """
        random.seed()

        # Separar jogadores por gênero e classificar por nível
        women = sorted([player for player in self.players if player['gender'] == 'F'], key=lambda x: -x['level'])
        men = sorted([player for player in self.players if player['gender'] == 'M'], key=lambda x: -x['level'])

        # Total de jogadores e times
        total_players = len(self.players)
        self.num_teams = 4

        # Configuração inicial dos times
        teams = [[] for _ in range(self.num_teams)]

        # Determinar número de jogadores por time
        if total_players == 16:
            base_team_size = 4
            extra_players = 0
        else:
            base_team_size = 4
            extra_players = total_players - (3 * base_team_size)

        # Adicionar uma mulher em cada time, se possível
        for i in range(3):  # Garantir mulheres nos 3 primeiros times
            if women:
                teams[i].append(women.pop(0))

        # Combinar homens e mulheres restantes
        remaining_players = men + women
        random.shuffle(remaining_players)

        # Preencher os 3 primeiros times com jogadores restantes
        for i in range(3):
            while len(teams[i]) < base_team_size:
                if remaining_players:
                    teams[i].append(remaining_players.pop(0))

        # Colocar os jogadores restantes no último time
        while remaining_players:
            teams[3].append(remaining_players.pop(0))

        # Depuração: Exibir a composição dos times e níveis totais
        # for i, team in enumerate(teams, start=1):
        #     print(f"Time {i}: {[player['name'] for player in team]} | Level Total: {sum(player['level'] for player in team)}")

        return teams

    def balance_teams(self, teams):
        """
        Ajusta os times para que a diferença no número de jogadores entre eles seja no máximo 1.

        Args:
            teams (list): Lista de times para ajustar.
        """
        all_players = [player for team in teams for player in team]
        random.shuffle(all_players)

        num_players = len(all_players)
        num_full_teams = num_players // self.num_teams
        extra_players = num_players % self.num_teams

        for i in range(self.num_teams):
            teams[i] = all_players[:num_full_teams + (1 if i < extra_players else 0)]
            all_players = all_players[len(teams[i]):]


def validate_team_count(players):
        """
        Valida se o número de jogadores é suficiente para formar entre 3 e 4 times.

        Args:
            players (list): Lista de jogadores disponíveis.

        Returns:
            bool: True se o número de jogadores for suficiente, False caso contrário.
        """
        num_players = len(players)
        if num_players < 12:
            print(f"Erro: Apenas {num_players} jogadores disponíveis. É necessário pelo menos 12 para formar 3 times.")
            return False
    
        elif num_players > 16:
            print(f"Erro: {num_players} jogadores disponíveis. Máximo permitido é 16 para formar 4 times.")
            return False
    
        print("Número de jogadores válido!")
        return True 

def validate_team_size(teams):
    """
    Valida se a diferença no número de jogadores entre os times é aceitável.

    Args:
        teams (list): Lista de times.

    Returns:
        bool: True se os times estão balanceados, False caso contrário.
    """
    sizes = [len(team) for team in teams]
    if max(sizes) - min(sizes) > 1:
        print("Erro: A diferença no tamanho dos times é maior que 1.")
        return False
    return True

