def chain_spell_solve(field, spellpower):
    strike_power = 25 * spellpower
    player = []
    opponent = []
    i = 0 # number of units hit
    for unit in field:
    	if unit and unit['resistance'] < 100:
    		damage = strike_power * (1 - unit['resistance'] / 100)
    		strike_power /= 2
    		how_many_killed = damage // unit['hitpoints']
    		how_many_killed = unit['number'] if how_many_killed > unit['number'] else how_many_killed
    		if how_many_killed:
    			result = f'{int(how_many_killed)} {unit["type"]}{"s" if how_many_killed > 1 else ""}'
    			if unit['owner'] == 'player':
    				player.append(result)
    			else:
    				opponent.append(result)
    		i += 1
    	if i >= 4:
    		break

    return [player, opponent]

def main():
    type, owner, hitpoints, number, resistance = "type", "owner", "hitpoints", "number", "resistance"
    arr = [
            None,
            { type: "Mage", owner: 'player', hitpoints: 30, number: 9, resistance: 0},
            None,
            { type: "Steel Golem", owner: 'opponent', hitpoints: 35, number: 60, resistance: 50 },
            None,
            None,
            { type: "Roc", owner: 'player', hitpoints: 40, number: 30, resistance: 0 },
            { type: "Sprite", owner: 'opponent', hitpoints: 2, number: 120, resistance: 0 }
        ]
    power = 100
    answer = [['9 Mages', '15 Rocs'], ['17 Steel Golems', '120 Sprites']]
    print(answer)
    answer = chain_spell_solve(arr, power)
    print(answer)
    

if __name__ == '__main__':
    main()