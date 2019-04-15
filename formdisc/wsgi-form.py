from ws_form import app ,db1
application = app
if __name__ == "__main__":
    db1.create_all()
    app.run(port=5001)
