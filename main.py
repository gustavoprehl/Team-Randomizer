from randomizer.data_handler import load_players, save_teams
from randomizer.team_randomizer import TeamRandomizer, validate_team_count


def get_num_teams():
    """
    Solicita ao usuário o número de times e valida a entrada.

    Returns:
        int: Número de times.
    """
    while True:
        try:
            num_teams = int(input("Digite o número de times (entre 3 e 4): "))
            if 3 <= num_teams <= 4:
                return num_teams
            print("Erro: O número de times deve ser entre 3 e 4. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")


def get_week_identifier():
    """
    Solicita ao usuário o identificador da semana.

    Returns:
        str: Identificador da semana.
    """
    return input("Digite o identificador da semana (exemplo: 'DD/MM/YYYY'): ")


def display_teams(teams):
    """
    Exibe os times gerados no terminal.

    Args:
        teams (list): Lista de times gerados.
    """
    print("Times Gerados:")
    for i, team in enumerate(teams, start=1):
        print(f"Time {i}: {', '.join(player['name'] for player in team)} | Level Total: {sum(player['level'] for player in team)}")


def main():
    """
    Função principal que executa o fluxo completo do programa.
    """
    players = load_players("data/players.csv")

    num_teams = get_num_teams()
    week_identifier = get_week_identifier()

    randomizer = TeamRandomizer(players, num_teams, week_identifier)

    if not validate_team_count(players):
        print("Erro: Número insuficiente de jogadores para formar os times.")
        return

    teams = randomizer.generate_teams()

    save_teams("data/previous_teams.json", week_identifier, teams)
    display_teams(teams)


if __name__ == "__main__":
    main()
