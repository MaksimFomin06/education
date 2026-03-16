import json
from bs4 import BeautifulSoup
import requests


class Parser:
    save_dir = "config/configs"
    
    @staticmethod
    def parse(filename: str):
        filepath = f"{Parser.save_dir}/{filename}"

        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)

        url: str = data['url']
        selectors: dict[str, str] = data['selectors']
        requirements: list[dict[str, str]] = data['requirements']

        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.encoding = response.apparent_encoding

        if response.status_code != 200:
            print(f"Ошибка {response.status_code}")

        soup = BeautifulSoup(response.text, "html.parser")
        all_books_on_page = soup.select('article.product_pod')
        valid_books = []

        for book_card in all_books_on_page:
            current_results = {}
            for field, selector in selectors.items():
                element = book_card.select_one(selector)
                if element and element.name == 'a' and element.has_attr('title'):
                    current_results[field] = element['title']
                else:
                    current_results[field] = element.get_text(strip=True) if element else None
            
            is_valid = True
            for req in requirements:
                field_val = current_results.get(req["field"])
                if not field_val:
                    is_valid = False; break
                    
                import re
                clean_val = re.sub(r'[^\d.]', '', field_val)
                val_to_check = float(clean_val) if clean_val else 0
                limit = float(req['value'])

                if req['operator'] == 'gt' and not (val_to_check > limit): is_valid = False
                elif req['operator'] == 'lt' and not (val_to_check < limit): is_valid = False
                elif req['operator'] == 'eq' and not (val_to_check == limit): is_valid = False
                if not is_valid: break

            if is_valid:
                valid_books.append(current_results)
        
        return valid_books