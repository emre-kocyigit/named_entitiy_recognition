import requests as re
import os


# 2 DEFINE A FUNCTION THAT SCRAPES AND RETURNS IT
def scrape_content(URL):
    response = re.get(URL)
    if response.status_code == 200:
        print("HTTP connection is succuessful! for the URL:", URL)
        return response
    else:
        print("HTTP connection is NOT successful! for the URL:", URL)
        return None


# 3 DEFINE A FUNCTION TO SAVE A HTML FILE OF THE SCRAPED WEBPAGE IN A DIRECTORY
def save_html(to_where, text, name):
    file_name = name + ".html"
    with open(os.path.join(to_where, file_name), "w") as f:
        f.write(text)


# 4 DEFINE A FUNCTION WHICH TAKES THE URL LIST and RUN STEP 2 and STEP 3 for EACH URL
def create_mini_dataset(to_where, URL_list):
    for i in range(0, len(URL_list)):
        content = scrape_content(URL_list[i])
        if content is not None:
            save_html(to_where, content.text, str(i))
        else:
            pass
    print("A dataset is created!")

















