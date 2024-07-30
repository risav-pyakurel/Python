#file to collect data from the user,  validates the data, has input statement


from datetime import datetime


#IN THIS PROMPT WE ARE GOING TO ASK THE USER TO INOUT
# BEFORE THEY GIVE US THE DATE, we can be getting date in diff places
# allow default is going to tell us if we should have the default value of today's date
def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime



def get_amount():
    pass


def get_category():
    pass


def get_description():
    pass
