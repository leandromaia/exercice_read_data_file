import json


class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


def main():
    print('Read People data from file!')
    resp = input('Do you want to see everyone in my db?[y/n]\n')
    
    if resp == 'y':
        raw_data = None
        with open('data_file.txt') as f:    
            raw_data = json.loads(f.read())

        people = []
        for item in raw_data['people']:
            person = Person(item['first_name'], item['last_name'])
            people.append(person)

        print(f'\nIn our db we have {len(people)} people. Here they are:')

        for item in people:
            print(item.full_name)
    else:
        print('Goodbye!')


if __name__ == "__main__":
    main()
