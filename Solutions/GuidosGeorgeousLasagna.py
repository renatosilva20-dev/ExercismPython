EXPECTED_BAKE_TIME = 40
def bake_time_remaining(remaining_time):
    """calculate bake time remaining
    :param bake_time_remaining: int - the time remaining in minutes
    """
    return EXPECTED_BAKE_TIME - remaining_time
bake_time_remaining(30)
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes of Lasagna
    :param number_of_layers: int - the number of layers in the lasagna.
    This function take one interger representing the number of layers and result in minutes the preparation time.
    """
    number_of_layers = number_of_layers * 2
    return number_of_layers
preparation_time_in_minutes(2)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.
    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    number_of_layers = number_of_layers * 2
    return number_of_layers + elapsed_bake_time
elapsed_time_in_minutes(3, 20)