import asyncio
from playwright.async_api import async_playwright


async def cricket_updates():

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=False
        )

        page = await browser.new_page()

        await page.goto(
            "https://www.cricbuzz.com/cricket-news",
            wait_until="networkidle"
        )

        await page.wait_for_timeout(3000)

        headlines = await page.locator("h2, h3").all_inner_texts()

        print("\nCRICKET NEWS:\n")

        for i, news in enumerate(headlines[:10], start=1):
            print(f"{i}. {news}")

        await page.wait_for_timeout(10000)

        await browser.close()


asyncio.run(cricket_updates())