def mc_output(mc_result):
    '''
    This is a helper function used for demonstration of the results returned by arithmetic_asian_option or
    arithmetic_basket_option functions on the GUI
    :param arithmetic_result: A tuple of 3 floats returned by the arithmetic_asian_option or arithmetic_basket_option
    :return: a string used as the output result shown in the GUI
    '''

    return "Expected Value = {},\nwith a Confidence Interval of [{}, {}] \nat 95% confidence level".format(mc_result[0], \
                mc_result[1], mc_result[2])