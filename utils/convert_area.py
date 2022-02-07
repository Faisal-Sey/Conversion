
area_conversions_dict = {
    "base": "square metre(m²)",
    "square metre(m²)-square centimetre(cm²)": 10000,
    "square metre(m²)-square inch(in²)": 1550,
    "square metre(m²)-square foot(ft²)": 10.7639,
    "square metre(m²)-square yard(yd²)": 1.19599,
    "square metre(m²)-acre(acres)": 0.000247105,
    "square metre(m²)-quart(qt)": (1 * (10 ** (-6))),  # need to verify value and those below
    "square metre(m²)-square kilometre(km²)": (1 * (10 ** (-6))),
    "square metre(m²)-hectares(ha)": 0.0001,
    "square metre(m²)-square mile(miles²)": (3.86102 * (10 ** (-7))),
    "square metre(m²)-square millimetre(mm²)": 1000000
}


def area_conversions(convert_from_to):
    if convert_from_to in area_conversions_dict.keys():
        return area_conversions_dict[convert_from_to]

    else:
        split_converts = convert_from_to.split("-")
        if split_converts[0] == split_converts[1]:
            return 1
        else:
            reversed_conversion = split_converts[1] + '-' + split_converts[0]
            if reversed_conversion in list(area_conversions_dict.keys()):
                result = area_conversions_dict[reversed_conversion]
                result = 1 / result
                return result

            else:
                first_change_str = area_conversions_dict["base"] + '-' + split_converts[0]
                first_change_result = area_conversions_dict[first_change_str]
                first_change_result = 1 / first_change_result

                second_change_str = area_conversions_dict["base"] + '-' + split_converts[1]
                second_change_result = area_conversions_dict[second_change_str]

                return first_change_result * second_change_result


def convert_area(from_unit, to_unit):
    convert_from_to = from_unit + '-' + to_unit
    return area_conversions(convert_from_to)
