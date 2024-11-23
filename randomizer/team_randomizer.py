import random
from collections import defaultdict

class TeamRandomizer:
    def __init__(self, players, num_teams, week_identifier):
        self.players = players
        self.num_teams = num_teams
        self.week_identifier = week_identifier

    def generate_teams(self):
        women = [p for p in self.players if p["gender"] == "F"]
        men = [p for p in self.players if p["gender"] == "M"]

        if len(women) < self.num_teams:
            print("Not enough women for each team; some teams will be all men.")
            print("Lembre-se, o código foi desenvolvido no intuito de ajudar e facilitar nosso lado, trazendo mais conforto e menos intrigas para que possamos aproveitar melhor nosso vôlei.")

        teams = [[] for _ in range(self.num_teams)]
       
        for i, woman in enumerate(women):
            teams[i % self.num_teams].append(woman)

        random.shuffle(men)
        for i, man in enumerate(men):
            teams[i % self.num_teams].append(man)

        return self.balance_teams(teams)

    def balance_teams(self, teams):
        avg_levels = [sum(player["level"] for player in team) / len(team) for team in teams]
        balanced = sorted(teams, key=lambda t: sum(player["level"] for player in t))
        return balanced

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