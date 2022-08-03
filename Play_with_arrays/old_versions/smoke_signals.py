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


def delete_events(events_dict, events_to_delete):
    for event in events_to_delete:
        del events_dict[event]
        
def find_unique_smoke_signals(sgnls_dict):
    sgnl_event_dict = {}
    for signal_1 in sgnls_dict.keys():
        if len(sgnls_dict[signal_1].keys()) == 1:
            sgnl_event_dict.setdefault(signal_1, list(sgnls_dict[signal_1].keys())[0])
            continue
        for signal_2 in sgnls_dict.keys():
            if signal_2 == signal_1 or abs(len(sgnls_dict[signal_1]) - len(sgnls_dict[signal_2])) > 1:
                continue
            events_results = []
            for event, event_count in sgnls_dict[signal_1].items():
                if (event in sgnls_dict[signal_2].keys() and event_count > sgnls_dict[signal_2][event]) \
                    or event not in sgnls_dict[signal_2].keys():
                        events_results.append(event)
            if len(events_results) == 1:
                sgnl_event_dict[signal_1] = events_results[0] 
    return sgnl_event_dict


def decode_smoke_signals(days):
    ret_dict, sgnls_dict = dict(), dict()
    # new attempt
    # add add the events that may be the result of a smoke signal to a dict
    # example: {'4.3.2': {'Ambush in the jungle': 1, 'Orange army retreat': 2}}
    # while any of the signals have len(sgnls_dict[signal].keys()) > 1, 
    # substract the count in the dict when any other has a line of len 1
    
    # prepare a dict sgnls_dict
    for line in days:
        event_dict = {}
        for event in line[1]:
            event_dict.setdefault(event, 0)
            event_dict[event] += 1
        for signal in line[0]:
            if signal not in sgnls_dict.keys():
                sgnls_dict.setdefault(signal, event_dict.copy())
            else:
                events_to_delete = []
                for event in sgnls_dict[signal].keys():
                    if event not in line[1]:
                        sgnls_dict[signal][event] -= 1
                        if sgnls_dict[signal][event] <= 0:
                            events_to_delete.append(event)
                delete_events(sgnls_dict[signal], events_to_delete)
    
    print(sgnls_dict)
    
    # work on ret_dict
    while len(sgnls_dict) > 0:
        # (1) find all ones
        new_ones_dict = find_unique_smoke_signals(sgnls_dict)
        # (2) add them to ret_dict
        ret_dict = ret_dict | new_ones_dict
        # (3) reduce all other dicts
        # (4) delete them from event_dicts
        for signal, event in new_ones_dict.items():
            del sgnls_dict[signal]  
            for new_signal in sgnls_dict.keys():
                if event in sgnls_dict[new_signal].keys():
                  #  sgnls_dict[new_signal][event] -= 1
                  #  if sgnls_dict[new_signal][event] <= 0:
                    del sgnls_dict[new_signal][event]
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
    