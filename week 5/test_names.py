from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest

def test_make_full_name():
    assert make_full_name ('Shawn', 'Nam') == 'Nam; Shawn'
    assert make_full_name ('White', 'David') == 'David; White'

def test_extract_given_name():
    assert extract_given_name('Nam; Shawn') == 'Shawn'
    assert extract_given_name('David; White') == 'White'

def test_extract_family_name():
    assert extract_family_name('Nam; Shawn') == 'Nam'
    assert extract_family_name('David; White') == 'David'

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])