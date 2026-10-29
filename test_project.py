import pytest
from project import clean_name, earnings, date_formatting
from datetime import date

def test_correct_name():
    assert clean_name("andres") == "Andres"
    assert clean_name("   Andres Bohorquez    ") == "Andres Bohorquez"
    assert clean_name("JOHN SMITH") == "John Smith"

    with pytest.raises(ValueError):
        clean_name("")
    with pytest.raises(ValueError):
            clean_name("     ")
    with pytest.raises(ValueError):
            clean_name("67")

def test_earnings():
      assert earnings(1, 350) == 350.0
      assert earnings(2.5, 200) == 500.0
      assert earnings(0.5, 250) == 125.0
      assert earnings(0, 250) == 0.0
      assert earnings(1, 0) == 0.0


      with pytest.raises(ValueError):
            earnings(-1, 1500)
      with pytest.raises(ValueError):
            earnings(67, -9)
      with pytest.raises(ValueError):
            earnings(-6, 70)
      with pytest.raises(ValueError):
            earnings(896, -1)

def test_date_formatting():
      today = date.today().strftime("%Y-%m-%d")
      assert date_formatting("") == today
      assert date_formatting("   ") == today

      assert date_formatting("2026-10-09") == "2026-10-09"
      assert date_formatting("2008-12-31") == "2008-12-31"

      with pytest.raises(ValueError):
            date_formatting("20-12-2025")
      with pytest.raises(ValueError):
            date_formatting("cat")
      with pytest.raises(ValueError):
            date_formatting("20/12/2025")
      with pytest.raises(ValueError):
            date_formatting("2025-12-32")
