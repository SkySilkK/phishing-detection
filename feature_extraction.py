def extract_features(url):
    url_length = len(url)
    url_count_dots = url.count(".")
    url_count_hyphens = url.count("-")

    digit_counter = 0

    for i in url:
        if i.isdigit():
            digit_counter += 1

    https_check = 0
    if url.startswith("https://"):
        https_check = 1
    else:
        https_check =  0


    return url_length,url_count_dots, url_count_hyphens, digit_counter, https_check
