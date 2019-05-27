def exception_handling(func):
    def wrapper():
        try:
            return func()

        except ZeroDivisionError:
            print("\nError! Your height should not be zero.")

        except ValueError:
            print("\nError! Please enter a number. Check your data and try again.")

        except IndexError:
            print("\nError! Impossible body mass index. Check your data and try again.")

        except KeyError:
            print("\nError! Incorrect data entered. Correct the mistake and try again.")

        except RuntimeError as ex:
            print("\nError! " + str(ex))

        except Exception as ex:
            print("\nError: " + str(ex))

    return wrapper
