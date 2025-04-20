def age_over18_filter(users):
    result = []
    for dict in users:
        if dict['age'] >= 18:
            result.append(dict)
    return result
        
def active_True_filter(users):
    result = []
    for dict in users:
        if dict['is_active'] == True:
            result.append(dict)
    return result

def age18_activeTrue_filter(users):
    result = []
    for dict in users:
        if dict['age']>=18 and dict['is_active']==True:
            result.append(dict)
    return result