from classes import data
import os
import csv

#The password for the api consumation, its '123456789' hashed
PASSWORD = b'$2b$12$gaANuhBnXQOSkFyIqWGhbeQlALykNQ/7VTiUxfSlYsdV9GmQetXU.'

#Globals used to make the path through DB
ROOT_TO_DB: str = "DB"                                  #Path to the DB dir from root
this_dir = os.path.dirname(os.path.abspath(__file__))   #Path to this dir
db_dir = os.path.join(os.path.dirname(this_dir),ROOT_TO_DB)              #Path from this dir to DB dir
petshop = os.path.join(db_dir, "petshop.csv")           #Path to Petshop DB
pricewknd = os.path.join(db_dir, "pricewknd.csv")       #Path to Price Weekday DB
pricewkday = os.path.join(db_dir,"pricewkday.csv")      #Path to Price Weekend DB

def getsingledata(id : str)-> data:
    """Gets all the data for a given ID

    Args:
        id (str): id from a petshop

    Returns:
        data: object with all the information from this petshop
    """

    #Gathering all the data
    temp_data = {}

    #Getting the ID, Name and Distance
    with open(petshop,'r',newline='') as file:

        #Opening csv reader and skipping the header
        reader = csv.reader(file)
        next(reader)

        #Finding and typing the desired data
        for line in reader:

            if line[0] == id:

                temp_data["id"] = int(line[0])
                temp_data["name"] = line[1]
                temp_data["distance"] = float(line[2])
                break

    #Using ID as a foreign key to get the weekdays prices
    with open(pricewkday,'r',newline='') as file:

        #Opening csv reader and skipping the header
        reader = csv.reader(file)
        next(reader)

        #Finding and typing the desired data
        for line in reader:

            if line[0] == id:

                temp_data["priceweekdays"] = {
                "little": float(line[1]),
                "big": float(line[2])
                }

                break

    #Using ID as a foreign key to get the weekends prices
    with open(pricewknd,'r',newline='') as file:

        #Opening csv reader and skipping the header
        reader = csv.reader(file)
        next(reader)

        #Finding and typing the desired data
        for line in reader:

            if line[0] == id:

                temp_data["priceweekends"] = {
                "little": float(line[1]),
                "big": float(line[2]),
                "percentage": (line[3])
                }
                break

    #Returning de object with the data
    return data(id = temp_data["id"],
                name = temp_data["name"],
                priceweekdays=temp_data["priceweekdays"],
                priceweekend = temp_data["priceweekends"],
                distance = temp_data["distance"],
                percentage = temp_data["priceweekends"]["percentage"])

def getallids()-> list:
    """Acces the DB to get all the ids

    Returns:
        list: a list of strings with all the ids
    """

    with open(petshop,"r",newline="")as file:

        #Skipping header
        reader = csv.reader(file)
        next(reader)

        #Returning a list with all the ids
        return [line[0] for line in reader]
