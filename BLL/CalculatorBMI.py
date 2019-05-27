from DAL.BMIRepository import get_bmi_list
from DAL.BMIRepository import get_bmi_interval_list


def get_upper_threshold(height):
    upper_threshold = height ** 2 * 25
    return upper_threshold


def get_lower_threshold(height):
    lower_threshold = height ** 2 * 18.5
    return lower_threshold


def get_weight_interval(lower_threshold, upper_threshold):
    weight_interval = "{:.1f}".format(lower_threshold) + " - " + "{:.1f}".format(upper_threshold)
    return weight_interval


def calculate_bmi_interval(weight, height):
    bmi_list = get_bmi_list()
    bmi_interval_list = get_bmi_interval_list()
    formatted_bmi = calculate_bmi(weight, height)
    bmi_list.append(formatted_bmi)
    sorted_bmi_list = sorted(bmi_list)
    bmi_interval = str(sorted_bmi_list[sorted_bmi_list.index(formatted_bmi) - 1]) + " - " + str(
        sorted_bmi_list[sorted_bmi_list.index(formatted_bmi) + 1])
    return bmi_interval_list[bmi_interval]


def calculate_bmi(weight, height):
    user_bmi = weight / height ** 2
    formatted_user_bmi = float("%.2f" % user_bmi)
    return formatted_user_bmi


def get_user_weight(user_input_weight):
    return user_input_weight


def get_user_height(user_input_height):
    return user_input_height
