types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}


def delete_duplicates(tickets):
    seen = set()
    tickets_updated = {}
    
    for key, values in tickets.items():
        unique_values = []
        for value in values:
            if value not in seen:
                unique_values.append(value)
                seen.add(value)
        tickets_updated[key] = unique_values       
    return tickets_updated


def final_dictionary(types,tickets):
    tickets_by_type = {}
    for type_id, ticket_list in tickets.items():
        type_name = types[type_id]
        tickets_by_type[type_name] = ticket_list
    return tickets_by_type



tickets_unique = delete_duplicates(tickets)
print(final_dictionary(types,tickets_unique))
