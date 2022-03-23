import pytest

from activity.main import check_value

def test_exception():
    #Arrage
    dict = {
        "animal" : "dog",
        "fruit" : "apple",
        "food" : "bbq"
    }
    #Act
    with pytest.raises (KeyError):
        check_value(dict, "car")