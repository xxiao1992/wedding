import os
import re


pages = [x for x in os.listdir() if x.endswith('html')]

for page in pages:
    with open(page, 'r+', encoding='UTF-8') as p:
        html = p.read()
        html = html.replace(
            'https://www.theknot.com/us/and-sep-2023-e66b44c6-66a7-486f-a2fe-67ab8f10bebe/travel',
            'transportation.html'
        ).replace(
            'https://www.theknot.com/us/and-sep-2023-e66b44c6-66a7-486f-a2fe-67ab8f10bebe/q-a',
            'faq.html'
        ).replace(
            'https://www.theknot.com/us/and-sep-2023-e66b44c6-66a7-486f-a2fe-67ab8f10bebe/things-to-do',
            'things-to-do.html'
        ).replace(
            'https://www.theknot.com/us/and-sep-2023-e66b44c6-66a7-486f-a2fe-67ab8f10bebe/photos',
            'photos.html'
        ).replace(
            'https://www.theknot.com/us/and-sep-2023-e66b44c6-66a7-486f-a2fe-67ab8f10bebe',
            'index.html'
        ).replace(
            'SEPTEMBER ',
            '9.'
        ).replace(
            'September ',
            '9.'
        ).replace(
            'Home',
            '主页'
        ).replace(
            '中国',
            ''
        )

        html = re.sub(r'<div data-testid="header-countdown" class="css-1o9254d">\d+ Days To Go!</div>', '', html)


        p.seek(0)
        p.write(html)
        p.truncate()