#!/bin/bash
export PATH="~/anaconda3/bin:$PATH"
cd ~/mindset/formdisc
gunicorn -b localhost:5002 wsgi-form
