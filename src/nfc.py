def split_units(split_id):
    units = [1, 2, 3, 5, 7, 10]
    test_units = [units.pop(split_id)]
    training_units = units
    return (test_units, training_units)
