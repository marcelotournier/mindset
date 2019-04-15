from ws_compra import app ,db
application = app
if __name__ == "__main__":
    db.create_all()
    app.run()
