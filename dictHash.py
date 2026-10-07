from csv import reader



class DictHash:
    def __init__(self):
        self.d={}
    def store(self,key,value):
        self.d[key] = value
    def __contains__(self, key):
        return key in self.d
    def search(self,key):
        return self.d[key]
    def __getitem__(self, key):
        return self.search(key)


if __name__ == '__main__':
    def read_drama():
        with open('kdrama.csv', newline='') as csvfile:
            kdrama = reader(csvfile)
            rubriker = next(kdrama)
            draman = DictHash()
            for rad in kdrama:
                draman.store(rad[0],rad)
        return draman

    draman = read_drama()

    print(draman['The Heirs'])
    print('Kalle Anka' in draman)
