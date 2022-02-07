

length_conversions_dict = {
    "base": "inch(in)",
    "inch(in)-centimetres(cm)": 2.54,
    "inch(in)-foot(ft)": 0.0833333,
    "inch(in)-yard(yd)": 0.0277778,
    "inch(in)-millimetre(mm)": 25.4,
    "inch(in)-metre(m)": 0.0254,
    "inch(in)-kilometre(km)": (2.54 * (10**(-5))),
    "inch(in)-microns(µm)": 25400,
    "inch(in)-amstrongs(Å)": 254000000,
    "inch(in)-mile(miles)": (1.57828 * (10 **(-5))),
}


def length_conversions(convert_from_to):
    if convert_from_to in length_conversions_dict.keys():
        return length_conversions_dict[convert_from_to]

    else:
        split_converts = convert_from_to.split("-")
        if split_converts[0] == split_converts[1]:
            return 1
        else:
            reversed_conversion = split_converts[1] + '-' + split_converts[0]
            if reversed_conversion in list(length_conversions_dict.keys()):
                result = length_conversions_dict[reversed_conversion]
                result = 1 / result
                return result

            else:
                first_change_str = length_conversions_dict["base"] + '-' + split_converts[0]
                first_change_result = length_conversions_dict[first_change_str]
                first_change_result = 1 / first_change_result

                second_change_str = length_conversions_dict["base"] + '-' + split_converts[1]
                second_change_result = length_conversions_dict[second_change_str]

                return first_change_result * second_change_result
    

def convert_length(from_unit, to_unit):
    convert_from_to = from_unit + '-' + to_unit
    return length_conversions(convert_from_to)
