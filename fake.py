from __future__ import absolute_import

import logging
import os

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sqd.settings")
# from django.core.wsgi import get_wsgi_application

# application = get_wsgi_application()

import threading
from datetime import datetime, timedelta
import random
import redis
import time

from api import tasks
from customer.models import UserToken
from product.models import Product
from purchase.models import Purchase

r = redis.Redis(host='localhost', port=6379, db=2)
logger = logging.getLogger("fake")

MYX = u"满溢享"
RJDJ = u"日进斗金"
DSCJ = u"点石成金"
YJB = u"赢金宝"
XSX = u"新手享"
YDB = u"盈锭宝"
TSDJ = u"淘沙得金"

PRODUCTS = [{MYX, RJDJ, DSCJ},
            {YJB, MYX},
            {XSX, MYX, YJB},
            {XSX, YJB, RJDJ},
            {YDB, DSCJ, TSDJ},
            {YDB, MYX},
            {YDB, TSDJ},
            {XSX, RJDJ}]

TOTAL_ORDERS = [(3, 5), (2, 3), (4, 6), (5, 7), (3, 4), (2, 3), (5, 7), (2, 3)]

TIME_SECTION = [(0, 1), (1, 7), (7, 9), (9, 12), (12, 15), (15, 19), (19, 22), (22, 24)]

CLOCKS = [0, 1, 2, 3, 4, 5, 6, 7]

HIT_AND_INCR = 20
HIT_NOT_INCR = 14
NOT_HIT_BUT_INCR = 5
NOT_HIT_AND_INCR = 1


def fake_order(token, pid):
    """
    测试刷单
    :param pid: 产品id
    :param token: 用户token
    :return:
    """
    now = datetime.now()
    order = now.strftime('%Y%m%d%H%M%S') + '{:0>4d}'.format(r.incr('today_order'))
    user = UserToken.objects.get_customer(token)
    product = Product.objects.get(pk=pid)
    amount = random.randint(1, 4) * product.min_purchase
    if int((product.sales_amount + amount) * 100 / product.funds_amount) > 70:
        products = Product.objects.filter(status=Product.STATUS_PUBLISHED)
        for pd in products:
            if pd.id != pid and int((pd.sales_amount + pd.min_purchase) * 100 / product.funds_amount) < 70:
                t = threading.Thread(target=fake_order, args=(token, pd.id))
                t.start()
                break
        logger.info('product over 70: {}'.format(product.id))
        return

    status = Purchase.TEST
    base_info = {
        'order_no': order,
        'customer': user,
        'product': product,
        'create_time': now.strftime('%Y-%m-%d %H:%M:%S'),
        'amount': amount,
        'terminal': Purchase.UNKNOWN,
        'status': status,
        'refund_status': False,
        'refund_type': Purchase.TO_BANKCARD,
        're_card_amount': amount,
        're_balance_amount': 0
    }
    purchase = Purchase(**base_info)
    purchase.save()
    logger.info('fake purchase: {}'.format(order))
    tasks.increase_sales_amount.delay(purchase.product.id, amount)


def random_order_num(clock):
    min_num, max_num = TOTAL_ORDERS[clock]
    return random.randint(min_num, max_num)


def chance_slice(result):
    weight_sum = 0
    segments = []
    for ret in result:
        weight_sum += ret[0]
    for i in range(len(result)):
        if i == 0:
            segments.append((0, result[0][0]))
        else:
            segments.append((segments[i - 1][1], segments[i - 1][1] + result[i][0]))
    return segments, weight_sum


def get_product_targets(clock):
    final = []  # [p.id, ...]
    result = []  # [[weight,name,num], ...]
    products = []
    products_query = Product.objects.filter(status=Product.STATUS_PUBLISHED)
    for p in products_query:
        if p.sales_percentage < 70:
            products.append(p)
    for product in products:
        fixed = False
        for name in PRODUCTS[clock]:
            if fixed:
                break
            if product.name.startswith(name):  # hit
                if product.interest_increase:  # hit and incr
                    result.append([HIT_AND_INCR, product.id, 0])
                else:
                    result.append([HIT_NOT_INCR, product.id, 0])  # hit but not incr
            else:  # miss
                if product.interest_increase:  # not hit but incr
                    result.append([NOT_HIT_BUT_INCR, product.id, 0])
                else:
                    result.append([NOT_HIT_AND_INCR, product.id, 0])  # neither hit nor incr
            fixed = True
    result = sorted(result, key=lambda l: l[0], reverse=True)
    num = random_order_num(clock)
    if len(result) == 0:
        return final
    if len(result) == 1:  # 仅一个
        for _ in range(num / 2):
            final.append(result[0])
        return final
    segments, weight_sum = chance_slice(result)
    for i in range(num):  # 按概率分配次数
        chance = random.randint(0, weight_sum)
        for j in range(len(segments)):
            low, high = segments[j][0], segments[j][1]
            if (low <= chance) and (chance < high):
                result[j][2] += 1
                break
    # 展开results,方便调用
    for ret in result:
        for _ in range(ret[2]):
            final.append(ret[1])
    random.shuffle(final)
    return final


def get_token():
    from django.db import connection
    cursor = connection.cursor()
    sql = """
              SELECT t.token FROM customer c
              JOIN purchase p ON p.customer_id=c.account_ptr_id
              JOIN user_token t ON t.customer_id=c.account_ptr_id
              WHERE p.amount<101
              AND p.status IN (1,5)
              AND p.create_time < Date("2015-10-15") GROUP BY p.customer_id;
          """
    cursor.execute(sql)
    result = cursor.fetchall()
    return random.sample(result, 1)[0][0]


def just_fake_it(clock):
    logger.info('time: {} fake started'.format(clock))
    targets = get_product_targets(clock)
    nums = len(targets)
    begin, end = TIME_SECTION[clock]
    slice = random.sample([i for i in range((end - begin) * 3600)], nums)
    # slice.sort()
    # logger.info('time: {}'.format(clock))
    logger.info('num: {}'.format(nums))
    gone = 0
    for i in range(nums):
        # time.sleep(1)0
        logger.info('thread sleep {}'.format(slice[i] - gone))
        time.sleep(slice[i] - gone)
        gone = slice[i]
        fake_order(get_token(), targets[i])
        t = threading.Thread(target=fake_order, args=(get_token(), targets[i]))
        t.start()
        return
    logger.info('time: {} fake finised'.format(clock))


def distributor():
    while 1:
        hour = datetime.now().hour
        for i in range(len(TIME_SECTION)):
            begin, end = TIME_SECTION[i]
            if (begin <= hour) and (hour < end):
                clock = i
                break
        t = threading.Thread(target=just_fake_it, args=(clock,))
        t.start()



def main():
    distributor()


def test():
    for c in CLOCKS:
        get_product_targets(c)


if __name__ == '__main__':
    logger.info("start")
    main()