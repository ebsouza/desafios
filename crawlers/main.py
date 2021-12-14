from utils import (extract_info, extract_parent_element,
                   next_base_url, do_request, sort_info_list)


subthreads = "cats;brazil;worldnews"
subthreads = subthreads.split(";")
base_url = 'https://old.reddit.com/r/'

subthreads = ['cats', 'brazil']
subthreads = ['cats']

for subthread in subthreads:
    url = f"{base_url}{subthread}/"
    url_generator = next_base_url(url)

    url_final = next(url_generator)
    response = do_request(url_final)

    info_list = []

    while response.status_code == 200:

        print(f"URL: {url_final}") #debug

        all_elements = extract_parent_element(response.content)
        if not all_elements:
            break

        print(len(all_elements))  # debug

        for element in all_elements.contents:
            try:
                info = extract_info(element)
                print(info) # debug
                info_list.append(info)
            except Exception as e:
                #print(e)  # debug
                pass

        else:
            url_final = next(url_generator)
            url_final += f"&after={info['id']}"
            response = do_request(url_final)


    info_list = sort_info_list(info_list) # debug
    print(info_list[:20])




"""
# https://www.kite.com/python/examples/1709/BeautifulSoup-retrieve-the-contents-of-a-tag
with open("page.html", "r") as file:
    all_elements = extract_parent_element(file)
    count = 0
    for element in all_elements.contents:
        try:
            info = extract_info(element)
            print(info)
            print("---")
            count += 1
        except Exception as e:
            pass
        #break
    else:
        pass

    print(count)
"""