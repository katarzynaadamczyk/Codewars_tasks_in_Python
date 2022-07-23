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


def common_signals(lst1, lst2):
    return list(set(lst1) & set(lst2))


def common_event(lst1, lst2):
    for event in lst1:
        if event in lst2:
            return event
    return None


# function that finds all lines of length equal to 1
def find_lines_len_one(days):
    lines = set()
    for line_number, line in enumerate(days):
        if len(set(line[0])) == 1:
            lines.add(line_number)
    return lines 


# function that finds first common signal within two lines
# here hides a mistake, please look carefully
# można jeszcze zrobić tak, że jak już nie ma pojedynczych wartosci to zrobić nowe days ->
# porobić wspolne z kazdej linii z kazda i wtedy może by coś wyszło dopiero z poniższego algorytmu
def find_first_common_signal(days):
    for index_1 in range(len(days)):
        for index_2 in range(index_1 + 1, len(days)):
            common_signals = common_signals(days[index_1][0], days[index_2][0])
            if len(common_signals) == 1:
                return [list(common_signals)[0], common_event(days[index_1][1], days[index_2][1])]
    return None


def find_common_signals(days):
    new_days = []
    for index_1 in range(len(days)):
        for index_2 in range(index_1 + 1, len(days)):
            signals = common_signals(days[index_1][0], days[index_2][0])
            if len(signals) > 0:
                events = []
                for event in days[index_1][1]:
                    if event in days[index_2][1]:
                        events.append(event)
                if len(events) == len(signals):
                    new_days.append((signals, events))
    return new_days


def decode_smoke_signals(days):
    ret_dict = dict()
    while len(days) > 0:
        # (1) sprawdź czy są 'jedynki', jeśli tak to usuń pierwszą jedynkę z setu
        signals_to_remove = set()
        lines_to_remove = find_lines_len_one(days)
        if len(lines_to_remove) > 0:
            for line in lines_to_remove:
                signals_to_remove.add(days[line][0][0])
                ret_dict.setdefault(days[line][0][0], days[line][1][0])
        else:
            # (2) jeśli nie to szukaj takich co mają tylko jeden wspólny z innym wspólnym
            # common_signal = find_first_common_signal(days)
            common_sgnls = find_common_signals(days)
            # (3) jeśli nie to break
            if len(common_sgnls) == 0:
                break
            print(days)
            print(common_sgnls)
            for line in range(len(common_sgnls)):
                if len(set(common_sgnls[line][1])) == 1:
                    for signal in common_sgnls[line][0]:
                        signals_to_remove.add(signal)
                        ret_dict.setdefault(signal, common_sgnls[line][1][0])
                        
        
        # shorten days of signals that are already in the dictionary
        for signal in signals_to_remove:
            for index, line in enumerate(days):
                while signal in line[0]:
                    days[index][0].remove(signal)
                    days[index][1].remove(ret_dict[signal]) # here I got some informations that there is a mistake
                    if len(line[0]) == 0:
                        lines_to_remove.add(index)
        # delete lines from days accordingly with lines_to_remove
        for line_to_remove in sorted(list(lines_to_remove), reverse=True):
            del days[line_to_remove]
            
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



if __name__ == '__main__':
    tests()
    # days = [(['9.9.2', '5.6.6', '2.6', '8.2'], ['Medical helicopters spotted', 'Pizza delivery spotted', 'Orange army charges', 'Infantry spotted']), 
    #        (['2.6', '8.9.3', '9', '9.9.2', '5.2.3', '8.2'], 
    #         ['Ceasefire called', 'Infantry spotted', 'Medical helicopters spotted', 'Tanks spotted', 'Ceasefire called', 'Orange army charges']), 
    #        (['9', '9.9.2', '8.9.3', '8.2', '8.3'], 
    #         ['Ceasefire called', 'Ambush in the jungle', 'Orange army charges', 'Ceasefire called', 'Infantry spotted']), 
    #        (['2.6', '5.6.6', '5.2.3', '8.2'], 
    #         ['Pizza delivery spotted', 'Medical helicopters spotted', 'Orange army charges', 'Tanks spotted'])]
    # print(find_common_signals(days))
    # print(decode_smoke_signals(days))
    