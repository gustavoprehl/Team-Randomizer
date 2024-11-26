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

        women = sorted([player for player in self.players if player['gender'] == 'F'], key=lambda x: -x['level'])
        men = sorted([player for player in self.players if player['gender'] == 'M'], key=lambda x: -x['level'])

        # Total de jogadores e times
        total_players = len(self.players)
        self.num_teams = 4

        # Configuração inicial dos times
        teams = [[] for _ in range(self.num_teams)]

        # Adicionar uma mulher em cada time, isso para fazer com que elas sejam chave dos times
        for i in range(min(self.num_teams, len(women))):
            teams[i].append(women.pop(0))

        remaining_players = men + women
        random.shuffle(remaining_players)

        # Função para calcular o nível total de um time
        def calculate_team_level(team):
            return sum(player['level'] for player in team)

        # Distribuir jogadores nos times garantindo as regras
        for player in remaining_players:
            # Tentar adicionar o jogador ao time com menor nível que respeite as regras
            added = False
            for team in teams:
                if len(team) < 4 and calculate_team_level(team) + player['level'] <= 9:
                    team.append(player)
                    added = True
                    break

            # Caso não seja possível adicionar respeitando as regras, adicionar ao time com menor nível (caso restrito)
            if not added:
                least_full_team = min(teams, key=lambda t: (len(t), calculate_team_level(t)))
                if len(least_full_team) < 4:
                    least_full_team.append(player)

        # Verificar consistência final
        for i, team in enumerate(teams):
            if len(team) > 4:
                raise ValueError(f"Erro: Time {i + 1} excedeu o limite de 4 jogadores.")
            if calculate_team_level(team) > 9:
                raise ValueError(f"Erro: Time {i + 1} excedeu o limite de nível total 9.")

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
    
        #print("Número de jogadores válido!")
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