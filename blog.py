from logging import debug
from flask import Flask, redirect, render_template, g, request, session, url_for, Blueprint

import sqlite3 as sqli

from werkzeug.utils import escape
from werkzeug.security import check_password_hash, generate_password_hash




blog = Flask(__name__)


@blog.route('/')
def home():
    con = sqli.connect()
    cur = con.cursor()