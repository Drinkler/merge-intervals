def merge(input):
    ''' Merge overlapping intervals.

    :param input: list of intervals
    :returns: list of merged intervals
    '''

    # Check for wrong input
    if not all(isinstance(interval, list) for interval in input):
        raise ValueError('A list of intervals must be given.')

    # no intervals in list
    if len(input) == 0:
        return []

    # sort intervals by start value in-place
    input.sort(key=lambda interval: interval[0])

    # create new list with first interval
    merged = [input[0]]

    # loop all intervals
    for interval in input:
        previous = merged[-1]

        # check if intervals overlap
        if interval[0] <= previous[1]:
            # set end value of overlapping intervals
            previous[1] = max(previous[1], interval[1])
        else:
            # append interval without overlap
            merged.append(interval)

    return merged


if __name__ == "__main__":
    input = [[25, 30], [2, 19], [14, 23], [4, 8]]

    try:
        output = merge(input)
    except ValueError as err:
        print('Error: {}'.format(err))
    else:
        print(output)
