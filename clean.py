import os
import codecs

pages = [x for x in os.listdir() if x.endswith('html')]

for page in pages:
    with open(page, 'r+', encoding='UTF-8') as p:
        html = p.read()
        html.replace(
            'https://www.theknot.com/us/and-sep-2023-e66b44c6-66a7-486f-a2fe-67ab8f10bebe/travel',
            'transportation.html'
        )

        html.replace(
            'https://www.theknot.com/us/and-sep-2023-e66b44c6-66a7-486f-a2fe-67ab8f10bebe/q-a',
            'faq.html'
        )

        html.replace(
            'https://www.theknot.com/us/and-sep-2023-e66b44c6-66a7-486f-a2fe-67ab8f10bebe/things-to-do',
            'things-to-do.html'
        )

        html.replace(
            'https://www.theknot.com/us/and-sep-2023-e66b44c6-66a7-486f-a2fe-67ab8f10bebe/photos',
            'photos.html'
        )

        html.replace(
            'https://www.theknot.com/us/and-sep-2023-e66b44c6-66a7-486f-a2fe-67ab8f10bebe',
            'index.html'
        )

        p.write(html)