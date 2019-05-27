from BLL.CalculatorBMI import *


def print_user_bmi(weight, height):
    print("\nYour body mass index: " +
          str(calculate_bmi(weight, height)) +
          "." +
          "\nYour body mass index range:" +
          str(calculate_bmi_interval(weight, height)) +
          " 18.5 - 25 are normal body mass index." +
          "\nYour normal weight range: " +
          str(get_weight_interval(get_lower_threshold(height), get_upper_threshold(height)))
          )


def ask_change_weight():
    while True:
        user_input_answer = input("\nDo you want to change your weight? Enter \"yes\" or \"no\": ")

        if user_input_answer.lower() == "no":
            print("\nThanks for using the app.\nThe process is complete.")
            quit()

        elif user_input_answer.lower() == "yes":
            break

        else:
            print("Incorrect data entered. Try again.")


def ask_user_gender(dictionary):
    user_input_gender = input("\nEnter your gender (male or female): ")

    if user_input_gender.lower() in dictionary:
        return user_input_gender

    else:
        print("Incorrect data entered. Try again.")
        ask_user_gender(dictionary)


def ask_user_age():
    user_input_age = float(input("\nEnter your age from 5 to 120. For example 18 or 38: "))

    if 5 <= user_input_age <= 120:
        return user_input_age

    else:
        print("Incorrect data entered. Try again.")
        ask_user_age()


def ask_desired_weight(lower_threshold, upper_threshold, interval):
    user_input_desired_weight = float(input("\nEnter your desired weight. "
                                            "For example 55 or 72.500 (kg)."
                                            "\nThe data entered must not exceed the normal weight range. "
                                            "Your normal weight range: " + interval + ". "))

    if lower_threshold <= user_input_desired_weight <= upper_threshold:
        return user_input_desired_weight

    else:
        print("Incorrect data entered. Try again.")
        ask_desired_weight(lower_threshold, upper_threshold, interval)


def print_user_weight_range(weight, desired_weight, user_weight_range):
    if weight > desired_weight:
        print("\nThe loss of your weight will be " + "{:.2f}".format(user_weight_range) + " kg.")

    elif desired_weight < weight:
        print("\nYour weight gain will be " + "{:.2f}".format(user_weight_range) + " kg.")


def ask_weight_change_per_week(weight, desired_weight):
    if weight > desired_weight:
        user_weight_change_per_week = int(input("\nHow many kg you want to lose in a week? "
                                                "Enter a number from 250 to 1000 (g): "))
        if 250 <= user_weight_change_per_week <= 1000:
            return user_weight_change_per_week

        else:
            print("Incorrect data entered. Try again.")
            ask_weight_change_per_week(weight, desired_weight)

    elif weight < desired_weight:
        user_weight_change_per_week = int(input("\nHow many kg you want to gain in a week? "
                                                "Enter a number from 250 to 1000 (g): "))
        if 250 <= user_weight_change_per_week <= 1000:
            return user_weight_change_per_week

        else:
            print("Incorrect data entered. Try again.")
            ask_weight_change_per_week(weight, desired_weight)


def print_period_of_weight_change(period):
    if period > 1:
        print("\nYou have achieved the desired weight in " +
              "{:.1f}".format(period) +
              " weeks."
              )

    elif period <= 1:
        print("\nYou have achieved the desired weight in " +
              "{:.1f}".format(period) +
              " week."
              )


def print_user_basic_metabolism(basic_metabolism):
    print("Your base metabolism (resting metabolism): " +
          str(int(basic_metabolism)) +
          " calories."
          )


def print_min_calorie_intake_per_day(min_intake):
    print("Your minimum calorie intake per day: " + str(min_intake) + " calories.")


def print_calorie_difference_per_day(difference):
    print("The difference between intake and consumption of calories should be equal to " +
          str(int(difference)) +
          " calories."
          )


def print_total_calorie_difference(weight, desired_weight, total_calorie_difference):
    if weight > desired_weight:
        print("You mast lose a total of " +
              str(int(total_calorie_difference)) +
              " calories per day."
              )

    else:
        print("You should get a total of " +
              str(int(total_calorie_difference)) +
              " calories per day."
              )


def print_extra_difference_calorie(weight, desired_weight, user_difference_calorie):
    if weight > desired_weight:
        print("In addition to the basic calorie consumption, you must lose an additional " +
              str(int(user_difference_calorie)) +
              " calories."
              )

    else:
        print("In order to achieve the desired weight, you must at least consume " +
              str(int(user_difference_calorie)) +
              " calories more than you lose."
              )
