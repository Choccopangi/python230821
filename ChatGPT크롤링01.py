# ChatGPT크롤링01.py

# pip install requests
# pip install beautifulsoup4
# pip install openpyxl

import requests
from bs4 import BeautifulSoup
import os
from openpyxl import Workbook

def crawl_blog_info(search_keyword, page_num):
    base_url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={page_num * 10 + 1}"
    response = requests.get(base_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        blog_entries = soup.find_all('li', class_='sh_blog_top')

        data = []

        for entry in blog_entries:
            blog_name = entry.find('a', class_='sh_blog_title').text
            blog_post_url = entry.find('a', class_='sh_blog_title')['href']
            post_date = entry.find('span', class_='txt_inline').text
            data.append((blog_name, blog_post_url, post_date))

        return data
    else:
        print("Failed to retrieve the page.")
        return []

def save_to_excel(data, keyword):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Blog Data"
    
    sheet.append(["Blog Name", "Blog Post URL", "Post Date"])
    for row in data:
        sheet.append(row)
    
    save_path = os.path.join("c:\\work", f"{keyword}_blog_data.xlsx")
    workbook.save(save_path)
    print(f"Data saved to {save_path}")

if __name__ == "__main__":
    search_keyword = input("Enter the search keyword: ")
    all_data = []

    for page_num in range(100):
        page_data = crawl_blog_info(search_keyword, page_num)
        all_data.extend(page_data)

    if all_data:
        save_to_excel(all_data, search_keyword)
