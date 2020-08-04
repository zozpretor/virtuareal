"""
Created on Tuesday Aug 18 16:23:20 2020
@author: zozpretor
"""
import sqlite3
import requests

Eine = 421267475
Ruki = 420249427
Ichigo = 434341786
Nana7mi = 434334701
Guangyi = 434401868
Muri = 455916618
Hano = 455965041
Waku = 472877684
nyatsuki = 472821519
plus = 472845978
miki = 477317922
Hoshimi = 477342747
mahiru = 477306079
Aza = 480680646
bamu = 480675481
Tabibito = 474369808
Roi = 480745939
seiya = 319810877
Saya = 490331391
Yukie = 56748733
Karu = 370687588
Shiki = 370687372
Pax = 370688671
Samael = 370689210
Chaos = 628292881
Kiyaro = 558070436
Chiharu = 558070433
vruid = [Eine, Ruki, Ichigo, Nana7mi, Guangyi, Muri, Hano, Waku, nyatsuki, plus, miki, Hoshimi, mahiru, Aza, bamu,
         Tabibito, Roi, seiya, Saya, Yukie, Karu, Shiki, Pax, Samael, Chaos, Kiyaro, Chiharu]

def creat():
    global conn
    conn = sqlite3.connect('vr.db')
    conn.execute("""
    create table if not exists vrfans(
    id INTEGER PRIMARY KEY,
    Eine_fan_uid int, Eine_fan_name varchar,
    Ruki_fan_uid int, Ruki_fan_name varchar,
    Ichigo_fan_uid int, Ichigo_fan_name varchar,
    Nana7mi_fan_uid int, Nana7mi_fan_name varchar,
    Guangyi_fan_uid int, Guangyi_fan_name varchar,
    Muri_fan_uid int, Muri_fan_name varchar,
    Hano_fan_uid int, Hano_fan_name varchar,
    Waku_fan_uid int, Waku_fan_name varchar,
    nyatsuki_fan_uid int, nyatsuki_fan_name varchar,
    plus_fan_uid int, plus_fan_name varchar,
    miki_fan_uid int, miki_fan_name varchar,
    Hoshimi_fan_uid int, Hoshimi_fan_name varchar,
    mahiru_fan_uid int, mahiru_fan_name varchar,
    Aza_fan_uid int, Aza_fan_name varchar,
    bamu_fan_uid int, bamu_fan_uid varchar,
    Tabibito_fan_uid int, Tabibito_fan_name varchar,
    Roi_fan_uid int, Roi_fan_name varchar,
    seiya_fan_uid int, seiya_fan_name varchar,
    Saya_fan_uid int, Saya_fan_name varchar,
    Yukie_fan_uid int, Yukie_fan_name varchar,
    Karu_fan_uid int, karu_fan_name varchar,
    Shiki_fan_uid int, Shiki_fan_name varchar,
    Pax_fan_uid int, Pax_fan_name varchar,
    Samael_fan_uid int, Samamel_fan_name varchar,
    Chaos_fan_uid int, Chaos_fan_name varchar,
    Kiyaro_fan_uid int, Kiyaro_fan_name varchar,
    Chiharu_fan_uid int,Chiharu_fan_name varchar)""")
    conn.execute("""
    create table if not exists fanresearch(
    id INTEGER PRIMARY KEY,
    whose_fan varchar,
    fan_uid int,
    fan_name varchar,
    fan_subscribe_uid int,
    fan_subscribe_name varchar
    )""")

def save():