import random


player_dict = {}

players_count = int(input('Введите количество игроков: '))
for i in range(players_count):
    print(f'Введите данные игрока {i+1}:')
    name = input('Имя: ')
    health = int(input('Здоровье: '))
    damage = int(input('Урон: '))
    player_name = 'player_' + str(i+1)
    player_dict[player_name] = {'name': name, 'health': health, 'damage': damage}


def attack(players):
    count = 1
    player_list = list(players.keys())
    dead_player = []
    win_name = ''

    while len(player_list) > 1:
        print(f'Ход {count}')
        for item in range(len(player_list)):
            n = 0 if item == len(player_list) - 1 else item + 1
            if players[player_list[item]]['health'] > 0:
                print(f"Бьёт {players[player_list[item]]['name']}")
                attack_damage = players[player_list[item]]['damage'] + random.randint(-10, 10)
                print(f"Урон составил {attack_damage} единиц")
                round_damage = players[player_list[n]]['health'] - attack_damage
                players[player_list[n]]['health'] = round_damage
                if round_damage <= 0:
                    print(f"Игрок {players[player_list[n]]['name']} повержен")
                    dead_player.append(player_list[n])
                else:
                    print(f"У игрока {players[player_list[n]]['name']} здоровья осталось {round_damage}")
        if len(dead_player) != 0:
            for item in range(len(dead_player)):
                player_list.remove(dead_player[item])
            dead_player = []
        win_name = players[player_list[0]]['name']
        count += 1
    print(f'Победил {win_name}')


attack(player_dict)
