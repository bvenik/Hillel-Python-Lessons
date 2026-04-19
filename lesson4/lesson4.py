class SpaceTravelException(Exception):
    pass


class OutOfFuelException(SpaceTravelException):
    pass


class SpacePiratesException(SpaceTravelException):
    pass


class BlackHoleException(SpaceTravelException):
    pass


def space_travel(fuel: int, encounter: bool, navigate_blackhole: bool) -> None:
    """
    Створює функцію, та обробляє умови, які приводять до якого-небудь Exception
    :param fuel: Рівень палива, для хорошого кінця потрібно значення понад 10
    :param encounter: Стан, чи зустріли тебе космічні пірати, для хорошого кінця потрібно значення False
    :param navigate_blackhole: Стан, чи натрапив ти на чорну діру, для хорошого кінця потрібно значення False
    """
    try:
        if fuel < 50:
            raise OutOfFuelException("Out of fuel, you have been crushed by asteroid!")
        if encounter:
            raise SpacePiratesException("Space pirates attacked you!")
        if navigate_blackhole:
            raise BlackHoleException("Black hole absorbed you!")
        else:
            print("You survived!")
    except OutOfFuelException as oofe:
        print(f"You didn't survived. {oofe}")
    except BlackHoleException as bhe:
        print(f"You didn't survived. {bhe}")
    except SpaceTravelException as ste:
        print(f"You didn't survived. {ste}")


space_travel(60, True, False)
