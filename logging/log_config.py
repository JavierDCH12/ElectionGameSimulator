import logging

logging.basicConfig(
    level=logging.DEBUG,  
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename="game.log",
    filemode="a"  
)

logger = logging.getLogger("logger")