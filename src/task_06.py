# Разработать методы для программы Камень-Ножницы-Бумага. При реализации
# обработки исключений важно не использовать встроенные классы ошибок с
# передачей им сообщения, а разработать классы с представленными ниже
# названиями.
# Метод rps_game_winner должен принимать на вход массив следующей структуры
# [ ["player1", "P"], ["player2", "S"] ], где P — бумага, S — ножницы, R — камень, и
# функционировать следующим образом:
#   • если количество игроков больше 2 необходимо вызывать исключение
#   WrongNumberOfPlayersError
#   • если ход игроков отличается от ‘R’, ‘P’ или ‘S’ необходимо вызывать
#   исключение NoSuchStrategyError
#   • в иных случаях необходимо вернуть имя и ход победителя, если оба
#   игрока походили одинаково - выигрывает первый игрок.

from typing import List


class WrongNumberOfPlayersError(ValueError):
    pass


class NoSuchStrategyError(ValueError):
    pass


strats = ("R", "S", "P")


def format_winner(winner: List[str]) -> str:
    return f"{winner[0]} {winner[1]}"


def rps_game_winner(players: List[List[str]]) -> str:
    if len(players) == 0 or len(players) > 2:  # raise exception if we have more then two players
        raise WrongNumberOfPlayersError("Number of players should be 1 or 2")

    first_player = players[0]
    if first_player[1] not in strats:  # check first player's startegy
        raise NoSuchStrategyError(
            "First player tried to use non existing strategy")
    if len(players) == 1:  # if we have only one player, it's a winner
        return format_winner(first_player)

    second_player = players[1]  # get payer 2 and check he's startegy
    if second_player[1] not in strats:
        raise NoSuchStrategyError(
            "Second player tried to use non existing strategy")

    # normal check which player should win
    fp_start_ind = strats.index(first_player[1])
    sp_start_ind = strats.index(second_player[1])

    if (fp_start_ind == sp_start_ind) or ((fp_start_ind + 1) % 3 == sp_start_ind):
        return format_winner(first_player)
    return format_winner(second_player)
