"""
Eingeloggte Bewohner*innen können eigene Beiträge erstellen, anzeigen,
bearbeiten, auf "erledigt" setzen und löschen.
"""
import functools
from flask import (Blueprint, abort, flash, g, redirect, render_template,
                   request, session, url_for)

from database import get_db
from forms import ConfirmForm, PostForm

# Alle URLs dieses Blueprints beginnen mit /beitraege
bp = Blueprint('posts', __name__, url_prefix='/beitraege')