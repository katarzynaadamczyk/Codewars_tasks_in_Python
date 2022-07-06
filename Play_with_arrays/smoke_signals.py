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



from numpy import sign


def common_signal(lst1, lst2):
    return set(lst1) & set(lst2)

def common_event(lst1, lst2):
    for event in lst1:
        if event in lst2:
            return event
    return None

def decode_smoke_signals(days):
    ret_dict = dict()
    signals_to_check = set()
    signals_to_remove = []
    # list the signals to check & start filling the result dictionary
    for line_number in range(len(days)):
        if len(days[line_number][0]) == 1:
            ret_dict.setdefault(days[line_number][0][0], days[line_number][1][0])
            signals_to_check.discard(days[line_number][0][0])
            signals_to_remove.append(days[line_number][0][0])
        else:
            for elem in days[line_number][0]:
                if elem not in ret_dict.keys():
                    signals_to_check.add(elem)
    while len(signals_to_check) > 0:
        # shorten days of signals that are already in the dictionary
        for signal in signals_to_remove:
            for line in days:
                if signal in line[0]:
                    line[0].remove(signal)
                    line[1].remove(ret_dict[signal])
        signals_to_remove = []
        # sprawdź czy są 'jedynki', jeśli tak to usuń pierwszą jedynkę z setu
        # jeśli nie to szukaj takich co mają tylko jeden wspólny z innym wspólnym
        # to co udało się znaleźć usuń z setu
        break
    
    return ret_dict

def tests():
    print('first test:')
    print(decode_smoke_signals([(["2"],["Convoy attacked"])]))
    print('should equal: {"2": "Convoy attacked"}')
    print()
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
    



if __name__ == '__main__':
    tests()
    print(common_signal(['abs', 'abc', 'dfg'], ['abs', 'bcd', 'aab']))
    