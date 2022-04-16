from .constants import dict_dim_conversions



def dim_conversions(convert_from_to, dim_conversions_dict):
    if convert_from_to in dim_conversions_dict.keys():
        return dim_conversions_dict[convert_from_to]

    else:
        split_converts = convert_from_to.split("-")
        if split_converts[0] == split_converts[1]:
            return 1
        else:
            reversed_conversion = split_converts[1] + '-' + split_converts[0]
            if reversed_conversion in list(dim_conversions_dict.keys()):
                result = dim_conversions_dict[reversed_conversion]
                result = 1 / result
                return result

            else:
                first_change_str = dim_conversions_dict["base"] + '-' + split_converts[0]
                first_change_result = dim_conversions_dict[first_change_str]
                first_change_result = 1 / first_change_result

                second_change_str = dim_conversions_dict["base"] + '-' + split_converts[1]
                second_change_result = dim_conversions_dict[second_change_str]

                return first_change_result * second_change_result


def convert_dim(from_unit, to_unit, dim):
    convert_from_to = from_unit + '-' + to_unit
    get_data = dict_dim_conversions(dim)
    return dim_conversions(convert_from_to, get_data)

