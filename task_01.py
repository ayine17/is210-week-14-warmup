#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""week 14 warmup"""


import pet


class Dog(pet.Pet):
    """ dog class subclass of pet
    """
    def __init__(self, has_shots=False, **args):
        """a constructor for the Dog class that has two major parameters

        args:
            has_shot(boolean, optional):Defaults to False
            **args(dict): store pet information
        return:
            None
        """

        pet.Pet.__init__(self, **args)
        self.has_shots = has_shots
        self.args = args
