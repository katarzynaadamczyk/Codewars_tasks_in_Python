def displayInventory(inventory):
    print('Inwentarz:')
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(f'{k.capitalize()}: {v}')
    print(f'Całkowita liczba przedmiotów: {item_total}')

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    

def main():
    data = {'lina': 1,
            'złote monety': 42,
            'strzały': 12,
            'pochodnia': 6,
            'sztylet': 1
            }
    displayInventory(data)
    dragonLoot = ['złote monety', 'sztylet', 'złote monety', 'złote monety', 'rubin']
    addToInventory(data, dragonLoot)
    displayInventory(data)
    

if __name__ == '__main__':
    main()