#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on April 2022
# This program uses loop to show cos table in radians

import math


def main():
    # this function calculates and print the Cos table in radians

    # process  & output
    for counter in range(
        0,
        181,
    ):

        # converts to radians
        cos_radians = math.radians(counter)
        # cos
        cos = math.cos(cos_radians)
        # rounds to 4 decimal points
        cos_round = round(cos, 4)
        # output
        print("Cos {}° : {} ".format(counter, cos_round))

    print("\nDone.")


if __name__ == "__main__":
    main()
