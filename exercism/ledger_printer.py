''' exercise ledger printer '''
# -*- coding: utf-8 -*-
from datetime import datetime
          

class LedgerEntry:
    def __init__(self, date, description, change):
        self.date = date
        self.description = description
        self.change = change / 100


def create_entry(date, description, change):
    entry = LedgerEntry(datetime.fromisoformat(date), description, change)
    return entry


def format_entries(currency, locale, entries):
    headers = {'en_US': ['Date', 'Description', 'Change'],
               'nl_NL': ['Datum', 'Omschrijving', 'Verandering']}
    format_date = {'en_US': '%m/%d/%Y', 'nl_NL': '%d-%m-%Y'}
    format_change = {'en_US': '{curr}{change:,.2f}', 'nl_NL': '{curr} {change:-,.2f} '}
    format_currency = {'USD': '$', 'EUR': u'€'}
    lengths = [10, 25, 13]
    linker = ' | '
    entries = sorted(entries, key=lambda entry: (entry.date, entry.change))
    # generate header row
    header = linker.join([text.ljust(length) for text, length in zip(headers[locale], lengths)])
    ret_value = [header]
    # generate rows for entries
    for entry in entries:
        # add date in right format
        new_entry = [entry.date.strftime(format_date[locale])]
        # add description and shorten it if necessary
        new_entry.append(entry.description.ljust(lengths[1]) if len(entry.description) <= lengths[1] \
                         else entry.description[:22] + '...')
        # add change
        if locale == 'en_US' and entry.change < 0:
            new_entry.append(format_change[locale].format(curr = format_currency[currency], \
                                                      change = abs(entry.change)))
            new_entry[-1] = ('(' + new_entry[-1] + ')').rjust(lengths[2])
        else:
            new_entry.append(format_change[locale].format(curr = format_currency[currency], \
                                                      change = entry.change).rjust(lengths[2]))
            if locale == 'nl_NL':
                new_entry[-1] = new_entry[-1].replace(",", "X").replace(".", ",").replace("X", ".")
            else:
                new_entry[-1] = new_entry[-1][1:] + ' '
        # append new row it to ret_value
        ret_value.append(linker.join(new_entry))
    return '\n'.join(ret_value)
