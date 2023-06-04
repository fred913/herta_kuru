from quart import Quart, render_template

app = Quart("herta_kuru")


@app.route('/')
async def hello():
    return await render_template("index.html")


if __name__ == '__main__':
    app.run(debug=False)
