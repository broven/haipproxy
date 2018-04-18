"""
We use this validator to filter ip that can access mobile zhihu website.
"""
from config.settings import (
    TEMP_BAIDU_QUEUE, VALIDATED_BAIDU_QUEUE,
    TTL_BAIDU_QUEUE, SPEED_BAIDU_QUEUE)
from ..redis_spiders import ValidatorRedisSpider
from .base import BaseValidator


class BaiduValidator(BaseValidator, ValidatorRedisSpider):
    """This validator checks the liveness of zhihu proxy resources"""
    name = 'baidu'
    urls = [
        'https://www.baidu.com'
    ]
    task_queue = TEMP_BAIDU_QUEUE
    score_queue = VALIDATED_BAIDU_QUEUE
    ttl_queue = TTL_BAIDU_QUEUE
    speed_queue = SPEED_BAIDU_QUEUE
    success_key = ''
