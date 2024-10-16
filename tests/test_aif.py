import numpy as np
import dcmri

def test_aif_parker():

    t = np.arange(0, 6*60, 1)
    ca = dcmri.aif_parker(t)

    # Test that this generates values in the right range
    assert np.round(np.amax(ca)) == 6

def test_aif_georgiou():

    # Not implemented yet so need to raise an error
    t = np.arange(0, 6*60, 1)
    try:
        ca = dcmri.aif_georgiou(t)
    except:
        assert True
    else:
        assert False

def test_aif_weinmann():

    # Not implemented yet so need to raise an error
    t = np.arange(0, 6*60, 1)
    try:
        ca = dcmri.aif_weinmann(t)
    except:
        assert True
    else:
        assert False

if __name__ == "__main__":

    test_aif_parker()
    test_aif_georgiou()
    test_aif_weinmann()

    print('All AIF tests passed!!')
