# /usr/bin/python3
# -*- coding : utf-8 -*-

"""
Quali'B models.
"""
import uuid

from datetime import datetime
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class TrainStop(Model):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    station = columns.Text(required=True)
    code = columns.Text()
    date = columns.DateTime(required=True)
    network = columns.Text(required=True)
