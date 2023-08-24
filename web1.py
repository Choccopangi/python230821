# web1.py
# 크롤링을 위한 선언
from bs4 import BeautifulSoup

# 페이지 로딩
page = open("c:\\work\\test01.html","rt", encoding="utf-8").read()
# 검색을 위한 객체
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())

# 문서 전체에서 <p> 검색
#print(soup.find_all("p"))
# 첫 번째 <p>를 검색
#print(soup.find("p"))

# 조건이 있는 경우: <p class="outer-text">
# class_는 키워드 충돌 때문에 사용 (클래스는 이미 있는 단어)
#print(soup.find_all("p", class_="outer-text"))
# 특정 속성을 지정할 때: attrs(attributes)
#print(soup.find_all("p", attrs={"class":"outer-text"}))
# 특정 id만 지정
#print(soup.find_all(id="first"))

# 태그 내부에 컨텐츠를 출력: .text, .get_text()
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n", "")
    print(title)