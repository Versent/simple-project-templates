# -*- coding: utf-8 -*-

import sys
import boto3
import click

@click.command()
class {{ cookiecutter.project_slug|title }}:
    def __init__(self):
        self.s3 = boto3.client('s3')

    def _list_buckets(self):
        return self.s3.list_buckets()

    def i_am_true(self):
        return True

    def _i_am_happy(self, happy):
        if not happy:
            sys.exit(1)
        return "happy"
