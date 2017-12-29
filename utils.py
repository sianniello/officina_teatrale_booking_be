import re


def seat_map_encoding(seats):
    regex = r"([A-Z]+)([0-9]+)"
    res = []
    prev_row = ''
    for seat in seats:
        match = re.match(regex, seat['seat_id'], re.I)
        if match:
            row = match.groups()[0]
            column = match.groups()[1]
            if prev_row == '':
                prev_row = row
                res.append([])

            if row != prev_row:
                res.append([])

            res[len(res) - 1].append(seat_status_switch(seat))

            prev_row = row

    return res


def seat_status_switch(seat):
    if seat['status'] == 'available':
        return 'f'
    elif seat['status'] == 'unavailable':
        return 'b'
    elif seat['status'] == 'unavailable_child':
        return 'c'
    elif seat['status'] == 'reserved':
        return 'r'