grammar = {
    "E": ["TA"],
    "A": ["+TA", "e"],
    "T": ["FB"],
    "B": ["*FB", "e"],
    "F": ["(E)", "i"],
}

non_terminals = list(grammar.keys())
start_symbol = non_terminals[0]


def first(t):
    productions = grammar[t]
    print(productions)
    first_set = list()
    for production in productions:
        if production[0] == "e":
            continue
        if production[0].islower() or not production[0].isalnum():
            first_set.append(production[0])
        else:
            if production[0] in non_terminals:
                first_set.extend(first(production[0]))
    return first_set


def follow(nt):
    if nt == start_symbol:
        follow_set = ["$"]
    else:
        follow_set = []

    # finding the non terminal
    for left, right in grammar.items():
        for item in right:
            if nt in item:
                idx = item.index(nt)
                try:
                    if item[idx + 1].islower() or not item[idx + 1].isalnum:
                        follow_set.append(item[idx + 1])
                    else:
                        follow_set.append(first(item[idx + 1]))
                except:
                    if item[idx] == left:
                        if right[0][0].islower() or not right[0][0].isalnum():
                            follow_set.append(right[0][0])
                            print(right[0][0])
                        else:
                            follow_set.extend(first(right[0][0]))
                    else:
                        follow_set.extend(first(left))
    return follow_set
