"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40;
PREPARATION_TIME = 2;

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(ELAPSED_TIME):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - ELAPSED_TIME



def preparation_time_in_minutes(layers):
    """Calculate the preparation_time_in_minutes.

    Parameters:
        layers (int): no of layers in lasgna

    Returns:
        int: Preparation time in minutes (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the layers in the lasagna as
    an argument and returns how many minutes the lasagna needs to bake
    based on the `PREPARATION_TIME`.
    """
    return layers*PREPARATION_TIME



def elapsed_time_in_minutes(layers, time):
    """Calculate the preparation_time_in_minutes.

    Parameters:
        layers (int): no of layers in lasgna
        time (int): time required

    Returns:
        int: elapsed time in minutes (in minutes) derived from 'PREPARATION_TIME, layers, time'.

    Function that takes the layers, time in the lasagna as
    an argument and returns how many minutes elapsed the lasagna needs to bake
    based on the `PREPARATION_TIME`.
    """
    return layers*PREPARATION_TIME + time


