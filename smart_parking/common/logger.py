import logging
import os
import time


class Log:

    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'log')
            log_file = os.path.join(log_path, f'smark_parking_{time.strftime("%Y%m%d")}.log')
            # [2022-05-10 17:51:18] INFO process_login.py(37): 单击登录按钮。
            logging.basicConfig(
                level=logging.INFO,
                format='[%(asctime)s] %(levelname)s %(filename)s(%(lineno)s): %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
                handlers=[logging.FileHandler(log_file, encoding='utf8'),
                          logging.StreamHandler()]
            )
            cls.logger = logging.getLogger()
        return cls.logger
