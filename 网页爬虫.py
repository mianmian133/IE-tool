import requests
from bs4 import BeautifulSoup


def download_ppt(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # 在这里根据网页结构和元素选择器找到下载链接
    # 以下示例是从http://www.example.com网站中找到PPT下载链接的示例
    ppt_link = soup.select_one('.ppt-download-link')['href']

    # 下载PPT文件
    ppt_response = requests.get(ppt_link)
    with open('download.ppt', 'wb') as f:
        f.write(ppt_response.content)

    print('PPT文件下载完成！')


if __name__ == '__main__':
    url = 'https://wenku.baidu.com/view/79cc163f32126edb6f1aff00bed5b9f3f90f7280.html?fr=aladdin664466&ind=2&aigcsid=39485&qtype=0&hitsid=2&_wkts_=1698022077253&bdQuery=%E8%BE%A9%E8%AE%BA%E8%B5%9Bppt&needWelcomeRecommand=1'  # 替换为你要爬取的网页URL
    download_ppt(url)
