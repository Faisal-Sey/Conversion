
mass_conversions_dict = {
    "base": "cubic metre(m³)",
    "cubic metre(m³)-cubic centimetre(cm³)": 1000000,
    "cubic metre(m³)-cubic inch(in³)": 61023.7,
    "cubic metre(m³)-cubic foot(ft³)": 35.3147,
    "cubic metre(m³)-quart(qt)": 1056.69,
    "cubic metre(m³)-litres(l)": 1000,
    "cubic metre(m³)-millilitres(ml)": 1000000,
    "cubic metre(m³)-U.S. gallon(gal)": 264.172,
    "cubic metre(m³)-U.K. gallon(gal)": 219.969,
    "cubic metre(m³)-Barrel(bbl)": 6.28981,
    "cubic metre(m³)-cubic decimetre(dm³)": 1e+9,
    "cubic metre(m³)-cubic millimetre(mm³)": 1000
}


def mass_conversions(convert_from_to):
    if convert_from_to in mass_conversions_dict.keys():
        return mass_conversions_dict[convert_from_to]

    else:
        split_converts = convert_from_to.split("-")
        if split_converts[0] == split_converts[1]:
            return 1
        else:
            reversed_conversion = split_converts[1] + '-' + split_converts[0]
            if reversed_conversion in list(mass_conversions_dict.keys()):
                result = mass_conversions_dict[reversed_conversion]
                result = 1 / result
                return result

            else:
                first_change_str = mass_conversions_dict["base"] + '-' + split_converts[0]
                first_change_result = mass_conversions_dict[first_change_str]
                first_change_result = 1 / first_change_result

                second_change_str = mass_conversions_dict["base"] + '-' + split_converts[1]
                second_change_result = mass_conversions_dict[second_change_str]

                return first_change_result * second_change_result


def convert_mass(from_unit, to_unit):
    convert_from_to = from_unit + '-' + to_unit
    return mass_conversions(convert_from_to)
