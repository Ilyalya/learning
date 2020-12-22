#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)
sweets = {
    'печенье': [
        {'shop': 'ашан', 'price': 10.99},
        {'shop': 'пятерочка', 'price': 9.99},
        {'shop': 'магнит', 'price': 11.99},
    ],
    'конфеты': [
        {'shop': 'ашан', 'price': 34.99},
        {'shop': 'пятерочка', 'price': 32.99},
        {'shop': 'магнит', 'price': 30.99},
    ],
    'карамель': [
        {'shop': 'ашан', 'price': 45.99},
        {'shop': 'пятерочка', 'price': 46.99},
        {'shop': 'магнит', 'price': 41.99},
    ],
    'пирожное': [
        {'shop': 'ашан', 'price': 67.99},
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99},
    ],
}
# Указать надо только по 2 магазина с минимальными ценами
sweets_pe = sweets['печенье']
sweets_ko = sweets['конфеты']
sweets_ka = sweets['карамель']
sweets_pi = sweets['пирожное']

if sweets['печенье'][0]['price'] < sweets['печенье'][1]['price'] < sweets['печенье'][2]['price']:
    print(sweets['печенье'][0]['shop'])
elif sweets['печенье'][1]['price'] < sweets['печенье'][2]['price']:
    print(sweets['печенье'][1]['shop'])
else:
    print(sweets['печенье'][2]['shop'])

if sweets['конфеты'][0]['price'] < sweets['конфеты'][1]['price'] < sweets['конфеты'][2]['price']:
    print(sweets['конфеты'][0]['shop'])
elif sweets['конфеты'][1]['price'] < sweets['конфеты'][2]['price']:
    print(sweets['конфеты'][1]['shop'])
else:
    print(sweets['конфеты'][2]['shop'])

if sweets['карамель'][0]['price'] < sweets['карамель'][1]['price'] < sweets['карамель'][2]['price']:
    print(sweets['карамель'][0]['shop'])
elif sweets['карамель'][1]['price'] < sweets['карамель'][2]['price']:
    print(sweets['карамель'][1]['shop'])
else:
    print(sweets['конфеты'][2]['shop'])

if sweets['пирожное'][0]['price'] < sweets['пирожное'][1]['price'] < sweets['пирожное'][2]['price']:
    print(sweets['пирожное'][0]['shop'])
elif sweets['пирожное'][1]['price'] < sweets['пирожное'][2]['price']:
    print(sweets['пирожное'][1]['shop'])
else:
    print(sweets['пирожное'][2]['shop'])