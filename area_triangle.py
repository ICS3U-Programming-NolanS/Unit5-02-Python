#!/usr/bin/env python3

# Created by: Nolan Shami
# Created on: Dec 2nd 2022
# This program has a function that calculates the area of a triangle
# through the user's chosen base and height.


def calc_area():

    try:
        user_base_float = float(
            input("Please enter your chosen base of the triangle in centimeters (cm): ")
        )
        user_height_float = float(
            input(
                "Please enter your chosen height of the triangle in centimeters (cm): "
            )
        )
        print("")

        user_area = user_base_float * user_height_float / 2
        print(
            "With {:,.2f}cm being the base and {:,.2f}cm being the height, the area of the triangle is: {:,.2f}cm2 !".format(
                user_base_float, user_height_float, user_area
            )
        )
    except Exception:
        print("I feel like you didn't enter a number...YOU MUST ENTER A NUMBER!!!")


def main():
    calc_area()


if __name__ == "__main__":
    main()
