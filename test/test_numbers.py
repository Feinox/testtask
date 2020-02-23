import logging, pytest
from client import Client


@pytest.fixture
def num():
    resp = Client().request.text
    return int(resp)


@pytest.fixture()
def logger():
    logger = logging.getLogger('Some.Logger')
    logger.setLevel(logging.INFO)

    return logger


def test_number(num, logger):
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                logger.info(str(num) + " is not a prime number")
                print(num, "is not a prime number")
                break
        else:
            logger.info(str(num) + " is a prime number")
            print(num, "is a prime number")

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        logger.info(str(num) + " is not a prime number")
        print(num, "is not a prime number")
    assert (num % i != 0)