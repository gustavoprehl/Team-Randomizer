from randomizer.data_handler import load_players, save_teams
from randomizer.team_randomizer import TeamRandomizer, validate_team_count

def main():
    players = load_players("data/players.csv")

    while True:
        try:
            num_teams = int(input("Digite o número de times (entre 3 e 4): "))
            if num_teams < 3 or num_teams > 4:
                print("Erro: O número de times deve ser entre 3 e 4. Tente novamente.")
                continue
            break
        except ValueError:
            print("Por favor, insira um número válido.")

    week_identifier = input("Digite o identificador da semana (exemplo: 'week_47_2024'): ")

    randomizer = TeamRandomizer(players, num_teams, week_identifier)

    if not validate_team_count(players):
        return

    teams = randomizer.generate_teams()

    save_teams("data/previous_teams.json", week_identifier, teams)

    print("Generated Teams:")
    for i, team in enumerate(teams, start=1):
        print(f"Team {i}: {', '.join(player['name'] for player in team)}")

if __name__ == "__main__":
    main()