
# Do not import this variable! Utilize api.globals.MEASUREMENTS instead
MEASUREMENTS_MAP = {
    'ounce': ['oz'],
    'pint': ['pt'],
    'teaspoon': ['tsp'],
    'tablespoon': ['tbsp', 'tbl'],
    'pound': ['lb']
}


def pluralized_measurement(measurement, quantity):
    '''
    Return a pluralized form of the given measurement if quantity if greater than 1.
    '''
    return f'{measurement}s' if quantity > 1 else measurement


def populate_measurements():
    '''
    Generate valid choices for measurements. Handles pluralized versions of measurements and their
    abbreviated form(s).
    :returns -> new measurements list containing tuples specifying allowed choices.
    '''
    new_measurements = []

    for name, abbrs in MEASUREMENTS_MAP.items():
        measurements = []
        measurements.append(
            (name, name)
        )
        measurements.append(
            (pluralized_measurement(name, quantity=2), pluralized_measurement(name, quantity=2))
        )
        for abbr in abbrs:
            measurements.append(
                (abbr, name)
            )
            measurements.append(
                (pluralized_measurement(abbr, quantity=2), pluralized_measurement(name, quantity=2))
            )
        new_measurements += measurements

    return new_measurements
