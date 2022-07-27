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
    event_signal_dict = {}
    all_signals_set = set()
    result_dict, new_signals = {}, []
    for day in days:
        all_signals_set.update(day[0])
        if len(day[0]) == 1:
            result_dict[day[0][0]] = day[1][0]
            new_signals.append(day[0][0])
            continue
        for event in day[1]:
            event_signal_dict.setdefault(event, set())
            event_signal_dict[event].update(day[0])
    
    while True:
        for signal in result_dict.keys():
            for event in event_signal_dict.keys():
                event_signal_dict[event].discard(signal)
        for event_1 in event_signal_dict.keys():
            result_set = event_signal_dict[event_1]
            for event_2 in event_signal_dict.keys():
                if event_2 != event_1 and event_signal_dict[event_1].issuperset(event_signal_dict[event_2]):
                    result_set = result_set - event_signal_dict[event_2]
                    print(event_1, result_set)
          #  if len(result_set) > 0:
          #      for signal in result_set:
          #          result_dict[signal] = event_1
          #      break
        del event_signal_dict[event_1]
        break
    print(all_signals_set, len(all_signals_set))
    print(result_dict)
    print(event_signal_dict)
    return result_dict
            
    

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
    print(decode_smoke_signals(days))
    print('should equal')
    print(result)
    
    
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
    