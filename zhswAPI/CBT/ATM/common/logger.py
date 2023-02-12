import logging
import os
import time


class Log:

    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'log')
            log_file = os.path.join(log_path, f'atm_{time.strftime("%Y%m%d")}.log')
            logging.basicConfig(
                level=logging.INFO,
                format= '[%(asctime)s] %(levelname)s %(filename)s(%(lineno)s): %(message)s',
                handlers=[logging.FileHandler(log_file, encoding='utf8'),
                          logging.StreamHandler()]
            )
            cls.logger = logging.getLogger()
        return cls.logger