import json
import wikipedia

wikipedia.set_lang("en")


class Downloader:

    def __init__(self, start, end, file_write):
        self.start = start
        self.end = end
        self.file_output = open(file_write, 'w')

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        self.start += 1
        try:
            self.country_name = country_list[self.start]
            country_page = wikipedia.page(self.country_name)
            url = country_page.url
            self.file_output.write(f'{self.country_name} - {url} \n')
            return f'{self.country_name} - {url}'
        except UnicodeError:
            self.start += 1
        except wikipedia.exceptions.PageError:
            self.start += 1
        except wikipedia.exceptions.DisambiguationError:
            self.start += 1


if __name__ == '__main__':
    country_list = []
    with open('countries.json', encoding='utf-8') as file:
        json_data = json.load(file)
        for country_dict in json_data:
            country_common = country_dict['name']
            country_name = (country_common['official'])
            country_list.append(country_name)
        for item in Downloader(0, len(country_list), 'output_country.txt'):
            print(item)
