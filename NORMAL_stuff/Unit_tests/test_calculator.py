from testing import square
import pytest
def test_square2():
    try:
        assert square(3)==9
    except AssertionError:
        print("3 sqaure is not 9")
    #assert makes something absolutely true 
    try:
        assert square(-2)==4
    except AssertionError:
        print("-2 sqaure is not 4")
    #assert makes something absolutely true 
    try:
        assert square(0)==0
    except AssertionError:
        print("0 square was not zero")
    #assert makes something absolutely true 

def test_square():
    #with pytest terminal 
    # it tells the number of the test that it has passed
    #pytest directly could check the whole folder
    assert square(2)==4
    assert square(-3)==9

def test_str():
    with pytest.raises(TypeError):
        #raises typeError
        square("cat")

def test_float_conversion():
    # Addition and the adjusting of the tolerances the abs part is the tolerance
    assert square(0.053)==pytest.approx(0.002802, abs=1e-5)


