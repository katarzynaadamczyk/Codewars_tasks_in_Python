'''
my solution to task: https://www.codewars.com/kata/62a3855fcaec090025ed2a9a
'''

# days is a tuple containing the smoke signals and the events that occured
# on a single day. Ex.
# days = [
#   (["4","5.1"],["Ambush in the jungle","Orange army retreats"]),
#   (["4","5.1","3.2.1"],["Tanks deployed","Orange army retreats","Ambush in the jungle"]),
#   (["5.1"],["Orange army retreats"])
#]

def decode_smoke_signals(days):
    ret_dict, days_to_delete, signals_to_delete = {}, [], []
    for i in range(len(days)):
        days[i] = [set(days[i][0]), days[i][1], set(days[i][1])]
        if len(days[i][2]) == 1:
            days_to_delete.append(i)
            for signal in days[i][0]:
                signals_to_delete.append(signal)
                days_to_delete.append(i)
                ret_dict[signal] = list(days[i][0])[0]
    while True:
        for i in sorted(days_to_delete, reverse=True):
            del days[i]
        for signal in signals_to_delete:
            for i in range(len(days)):
                if signal in days[i][0]:
                    days[i][0].discord(signal)
                    days[i][1].remove(ret_dict[signal])
                    days[i][2] = set(days[i][1])
                    # todo
        days_to_delete, signals_to_delete = [], []
        for i1 in range(len(days)):
            for i2 in range(len(days)):
                if i1 == i2:
                    continue
                if len(days[i1][2] & days[i2][2]) == 1:
                    common_event = list(days[i1][2] & days[i2][2])[0]
                    common_signals = list(days[i1][0] & days[i2][0])
                    for signal in common_signals:
                        ret_dict[signal] = common_event
                        # todo
        break
    print(days)
    return ret_dict
            
    

def tests():
    '''
    print('first test:')
    print(decode_smoke_signals([(["2"],["Convoy attacked"])]))
    print('should equal: {"2": "Convoy attacked"}')
    print()
    '''
    print('second test:')
    print(decode_smoke_signals([(["4","5.1"],["Ambush in the jungle","Orange army retreats"]),
            (["4","5.1","3.2.1"],["Tanks deployed","Orange army retreats","Ambush in the jungle"]),
            (["5.1"],["Orange army retreats"])]))
    print('should equal: {"5.1": "Orange army retreats",\
            "4": "Ambush in the jungle",\
            "3.2.1": "Tanks deployed"}')
    print()
    print('third test:')
    print(decode_smoke_signals([(["8.2.1","4.3.4","1"],["Ambush in the jungle","General assassinated","Ambush in the jungle"]),
            (["1","2.2","9.3"],["Ambush in the jungle","Orange army retreats","Push into the mountains"]),
            (["4.3.4","6"],["Ambush in the jungle","Orange general goes on vacation"]),
            (["8.2.1","9.3","1"],["Ambush in the jungle","General assassinated","Push into the mountains"])]))
    print('should equal: {"4.3.4": "Ambush in the jungle",\
            "6": "Orange general goes on vacation",\
            "1": "Ambush in the jungle",\
            "8.2.1": "General assassinated",\
            "9.3": "Push into the mountains",\
            "2.2": "Orange army retreats"}')
    print()
    print('4th test')
    print(decode_smoke_signals([(['9.9.2', '5.6.6', '2.6', '8.2'], 
                                 ['Medical helicopters spotted', 'Pizza delivery spotted', 'Orange army charges', 'Infantry spotted']), 
                                (['2.6', '8.9.3', '9', '9.9.2', '5.2.3', '8.2'], 
                                 ['Ceasefire called', 'Infantry spotted', 'Medical helicopters spotted', 'Tanks spotted', 'Ceasefire called', 'Orange army charges']), 
                                (['9', '9.9.2', '8.9.3', '8.2', '8.3'], 
                                 ['Ceasefire called', 'Ambush in the jungle', 'Orange army charges', 'Ceasefire called', 'Infantry spotted']), 
                                (['2.6', '5.6.6', '5.2.3', '8.2'], 
                                 ['Pizza delivery spotted', 'Medical helicopters spotted', 'Orange army charges', 'Tanks spotted'])]))
    print("should equal {'8.2': 'Orange army charges', '8.3': 'Ambush in the jungle', '9': \
        'Ceasefire called', '8.9.3': 'Ceasefire called', '5.2.3': 'Tanks spotted', \
        '2.6': 'Medical helicopters spotted', '5.6.6': 'Pizza delivery spotted', '9.9.2': 'Infantry spotted'}")

def new_test():
    days = [
            (['8', '4.4.4', '2', '6', '1.7', '2.7.9'], ['Orange army retreats', 'Medical helicopters spotted', 'Ceasefire called', 'Ceasefire called', 'Orange army charges', 'Orange army charges']), 
            (['9.9.6', '4.4.4', '6', '5.1.6', '2', '9'], ['Orange army charges', 'Infantry spotted', 'Orange army charges', 'Infantry spotted', 'Ceasefire called', 'Missile launchers spotted']), 
            (['8', '6.1.5', '1.7', '6', '4.4.4'], ['Missile launchers spotted', 'Orange army retreats', 'Orange army charges', 'Medical helicopters spotted', 'Ceasefire called']), 
            (['4.6.9', '4.4.4', '6', '9'], ['Orange army charges', 'Infantry spotted', 'Ceasefire called', 'Missile launchers spotted']), 
            (['2', '9.9.6', '6.1.5', '9'], ['Infantry spotted', 'Missile launchers spotted', 'Infantry spotted', 'Orange army charges']), 
            (['2', '4.6.9', '1.7', '4.4.4'], ['Missile launchers spotted', 'Orange army charges', 'Medical helicopters spotted', 'Ceasefire called'])
           ]
    result = {'6': 'Orange army charges', '1.7': 'Medical helicopters spotted', 
              '4.6.9': 'Missile launchers spotted', '2.7.9': 'Ceasefire called', '9.9.6': 'Infantry spotted', 
              '6.1.5': 'Missile launchers spotted', '4.4.4': 'Ceasefire called', '9': 'Infantry spotted', 
              '5.1.6': 'Missile launchers spotted', '2': 'Orange army charges', '8': 'Orange army retreats'}
    print('5th test')
    solution = decode_smoke_signals(days)
    for signal in sorted(solution.keys()):
        print(f'{signal}:\t{solution[signal]}')
    print('should equal')
    for signal in sorted(result.keys()):
        print(f'{signal}:\t{result[signal]}')
    
    
if __name__ == '__main__':
    # tests()
    # days = [(['9.9.2', '5.6.6', '2.6', '8.2'], ['Medical helicopters spotted', 'Pizza delivery spotted', 'Orange army charges', 'Infantry spotted']), 
    #        (['2.6', '8.9.3', '9', '9.9.2', '5.2.3', '8.2'], 
    #         ['Ceasefire called', 'Infantry spotted', 'Medical helicopters spotted', 'Tanks spotted', 'Ceasefire called', 'Orange army charges']), 
    #        (['9', '9.9.2', '8.9.3', '8.2', '8.3'], 
    #         ['Ceasefire called', 'Ambush in the jungle', 'Orange army charges', 'Ceasefire called', 'Infantry spotted']), 
    #        (['2.6', '5.6.6', '5.2.3', '8.2'], 
    #         ['Pizza delivery spotted', 'Medical helicopters spotted', 'Orange army charges', 'Tanks spotted'])]
    # print(find_common_signals(days))
    # print(decode_smoke_signals(days))
    new_test()
    