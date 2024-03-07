from classes import WrongPasswordError
from datetime import date
from typing import Dict
from db import getsingledata, getallids, PASSWORD
import bcrypt


def isweekday(year : str, month : str, day : str) -> bool:
    """Returns true if its a week day and false if ain't

    Args:
        year (int): year
        month (int): month
        day (int): day

    Raises:
        ValueError: negative number or impossible numbers

    Returns:
        bool: true for weekdays e false for weekends
    """

    try:

        #Correcting types
        week_index = date(year = int(year), month = int(month), day = int(day)).isoweekday()

        if week_index <= 5:
            return True
        return False

    except ValueError:
        raise ValueError("Data inválida")

def getsingleprice(id : str, weekday : bool, quantity : Dict[str,int]) -> tuple[float,float, str]:
    """Returns the price of one petshop

    Args:
        id (int): id from the petshop
        day (int): 0 for weekdays and 1 for weekends
        quantity (Dict[int]): {"little" : int, "big" : int}

    Returns:
        tuple[float,float]: (price, distance)
    """
    if any(valor < 0 for valor in quantity.values()):
        raise ValueError("Um ou mais valores de quantidade negativos")

    data = getsingledata(id = id)
    if weekday:

        price : float = quantity["little"] * data.price["weekdays"]["little"] + quantity["big"] * data.price["weekdays"]["big"]

    elif data.usespercentage():

        price : float = quantity["little"] * data.price["weekdays"]["little"] * data.price["weekends"]["little"] + quantity["big"] * data.price["weekdays"]["big"] * data.price["weekends"]["big"]

    else:
        price : float = quantity["little"] * data.price["weekends"]["little"] + quantity["big"] * data.price["weekends"]["big"]

    return (price, data.distance, data.name)

def findbetterprice(budgets : list[tuple[float,float,str]]) -> dict:
    """Returns the better price in the list

    Args:
        budgets (list[tuple[float,float,str]]): list[tuple[price, distance, name]]

    Returns:
        _type_: _description_
    """

    ordered_budget = sorted(budgets, key = lambda x : (x[0], x[2]))
    return {'name': ordered_budget[0][2], 'price': ordered_budget[0][0]}

def checkpassword(password : str) -> bool:
    if bcrypt.checkpw(password.encode('utf-8'), PASSWORD):
        return True
    raise WrongPasswordError("Senha incorreta!")
