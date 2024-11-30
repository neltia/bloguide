from datetime import datetime


def calculate_date_difference(dates):
    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(dates["start_date"], date_format)
    end_date = datetime.strptime(dates["end_date"], date_format)
    difference = (end_date - start_date).days
    return {"difference": difference}


def calculate_percentage(total):
    part = total["part"]
    whole = total["whole"]
    percentage = (part / whole) * 100
    return {"percentage": percentage}


def calculate_increase(increase_data):
    original = increase_data["original"]
    new = increase_data["new"]
    increase = ((new - original) / original) * 100
    return {"increase": increase}
