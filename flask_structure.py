from flask import Flask
import asyncio
from playwright.async_api import async_playwright

app = Flask(__name__)


async def get_cricket_news():

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=True
        )

        page = await browser.new_page()

        await page.goto(
            "https://www.cricbuzz.com/cricket-news",
            wait_until="networkidle"
        )

        await page.wait_for_timeout(3000)

        headlines = await page.locator("h2, h3").all_inner_texts()

        await browser.close()

        return headlines[:10]


@app.route('/')
def home():
    return """
    <h1>Flask Playwright App</h1>
    <a href='/news'>Get Cricket News</a>
    """


@app.route('/news')
def cricket_news():

    headlines = asyncio.run(get_cricket_news())

    html_output = "<h1>Latest Cricket News</h1><ol>"

    for news in headlines:
        html_output += f"<li>{news}</li>"

    html_output += "</ol>"

    return html_output


if __name__ == '__main__':
    app.run(debug=True)