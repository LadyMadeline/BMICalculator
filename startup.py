from BLL.WeightEditor import *
from PLL.UserController import *
from Helpers.ExceptionHandlingHelper import exception_handling


@exception_handling
def main():
    print("\nBody Mass Index Calculator\n")

    user_weight = get_user_weight(float(input("Enter your weight. For example 70 or 56.200 (kg): ")))
    user_height = get_user_height(float(input("Enter your height. For example 1.67 or 1.93 (m): ")))
    user_min_calorie_intake = return_min_calorie_intake()
    user_lower_threshold = get_lower_threshold(user_height)
    user_upper_threshold = get_upper_threshold(user_height)
    user_weight_interval = get_weight_interval(user_lower_threshold,
                                               user_upper_threshold
                                               )

    print_user_bmi(user_weight,
                   user_height
                   )
    ask_change_weight()

    user_gender = ask_user_gender(user_min_calorie_intake)
    user_age = ask_user_age()
    user_desired_weight = ask_desired_weight(user_lower_threshold,
                                             user_upper_threshold,
                                             user_weight_interval
                                             )
    change_weight_per_week = ask_weight_change_per_week(user_weight,
                                                        user_desired_weight
                                                        )
    user_weight_range = weight_range(user_weight,
                                     user_desired_weight
                                     )
    period = period_of_weight_change(user_weight_range,
                                     change_weight_per_week
                                     )
    basic_metabolism = user_basic_metabolism(user_weight,
                                             user_height,
                                             user_age
                                             )
    user_calorie_difference_per_day = calorie_difference_per_day(change_weight_per_week)
    user_total_calorie_difference = total_calorie_difference(user_weight,
                                                             user_desired_weight,
                                                             user_min_calorie_intake[user_gender],
                                                             user_calorie_difference_per_day,
                                                             basic_metabolism
                                                             )
    user_extra_difference_calorie = extra_difference_calorie(user_weight,
                                                             user_desired_weight,
                                                             user_min_calorie_intake[user_gender],
                                                             basic_metabolism,
                                                             user_total_calorie_difference
                                                             )

    print_user_weight_range(user_weight,
                            user_desired_weight,
                            user_weight_range
                            )
    print_period_of_weight_change(period)
    print_user_basic_metabolism(basic_metabolism)
    print_min_calorie_intake_per_day(user_min_calorie_intake[user_gender])
    print_calorie_difference_per_day(user_calorie_difference_per_day)
    print_total_calorie_difference(user_weight,
                                   user_desired_weight,
                                   user_total_calorie_difference
                                   )
    print_extra_difference_calorie(user_weight,
                                   user_desired_weight,
                                   user_extra_difference_calorie
                                   )


main()
