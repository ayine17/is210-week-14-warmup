#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task2.week 14 """

from data import FRUIT


def get_cost_per_item(shoplist):
    """ a fucion get cost of items
    args:
        shoplist(dict): a dictionary called shoplist which keys are item name
                        as found in FRUIT and the value should be an integer
                        indicating the number of units to purchase.
    return:
        None
    example:
        >>> print shoplist
        {'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1}
        >>> get_cost_per_item({'Lime': 12, 'Red Pear': 4,
                                'Peach': 24, 'Beet': 1})
        {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
    """

    results = {keys: shoplist[keys] * FRUIT[keys] for keys in shoplist.keys()
               if keys in FRUIT.keys()}

    return results


def get_total_cost(shoplist):
    """ a function named returns the total cost
    args:
        shoplist(dict): a dictionary called shoplist which keys are item name
                        as found in FRUIT and the value should be an integer
                        indicating the number of units to purchase

    return:
        Returns the total cost

    Examples

        >>> print shoplist
        {'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1}
        >>> get_total_cost({'Lime': 12, 'Red Pear': 4,
                            'Peach': 24, 'Beet': 1})
        112.80000000000001
    """

    results = get_cost_per_item(shoplist)

    retval = sum(result for result in results.values())
    return retval
