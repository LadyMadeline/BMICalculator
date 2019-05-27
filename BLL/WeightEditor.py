from DAL.BMIRepository import get_min_calorie_intake


def return_min_calorie_intake():
    return get_min_calorie_intake()


def max_lose_weight(weight, lower_threshold):
    max_lose = weight - lower_threshold
    return max_lose


def max_gain_weight(weight, upper_threshold):
    max_gain = upper_threshold - weight
    return max_gain


def weight_range(weight, desired_weight):
    if weight > desired_weight:
        user_weight_range = weight - desired_weight
        return user_weight_range

    elif weight < desired_weight:
        user_weight_range = desired_weight - weight
        return user_weight_range

    else:
        print("\nYour desired weight is equal to your current weight. Congratulations!"
              "\nThanks for using the app.\nThe process is complete.")
        quit()


def period_of_weight_change(change_weight_range, change_per_week):
    period = change_weight_range * 1000 / change_per_week
    return period


def user_basic_metabolism(weight, height, age):
    basic_metabolism = 9.99 * weight + 6.25 * height * 100 - 5 * age - 161
    return basic_metabolism


def calorie_difference_per_day(weight_change_per_week):
    calorie_difference = 7.716 * weight_change_per_week / 7
    return calorie_difference


def basic_calorie_consumption(basic_metabolism, min_calorie_intake):
    user_basic_calorie_consumption = basic_metabolism - min_calorie_intake
    return user_basic_calorie_consumption


def total_calorie_difference(weight, desired_weight, min_intake, calorie_difference, metabolism):
    if weight > desired_weight:
        user_total_calorie_difference = min_intake + calorie_difference
        return user_total_calorie_difference

    elif weight < desired_weight:
        user_total_calorie_difference = metabolism + calorie_difference
        return user_total_calorie_difference


def extra_difference_calorie(weight, desired_weight, min_calorie_intake, basic_metabolism, user_total_calorie_difference):
    if weight > desired_weight:
        user__difference_calorie = user_total_calorie_difference - basic_metabolism
        return user__difference_calorie

    else:
        user__difference_calorie = user_total_calorie_difference - min_calorie_intake
        return user__difference_calorie
