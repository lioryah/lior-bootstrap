import liorsearch
from loguru import logger

def test_testsimple():
    x = liorsearch.load_tokens('/mnt/c/Users/liory/_wd/repos/lior-bootstrap/liorboot/interviewsimulation/simulation.26.2/tokens2.txt')
    logger.info(x)
    logger.info(x)
    # assert x == {}