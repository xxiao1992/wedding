import os
import codecs

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
            'SEPTEMBER',
            '九月'
        ).replace(
            'September',
            '九月'
        )
        
        p.seek(0)
        p.write(html)
        p.truncate()