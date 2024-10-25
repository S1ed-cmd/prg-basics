
def cm_to_m(cm):
    return cm / 100
def m_to_cm(m):
    return m * 100
def cm_to_in(cm):
    return cm / 2.54
def ft_in_to_cm(feet, inches):
    cm_from_feet = feet * 30.48
    cm_from_inches = inches * 2.54
    return cm_from_feet + cm_from_inches