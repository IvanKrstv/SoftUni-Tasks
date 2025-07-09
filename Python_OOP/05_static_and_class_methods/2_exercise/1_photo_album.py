from math import ceil

class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos: list[list[str]] = [[] for _ in range(self.pages)] # matrix

    @classmethod
    def from_photos_count(cls, photos_count: int):
            return cls(pages=ceil(photos_count / 4))

    def add_photo(self, label: str):
        for i in range(len(self.photos)):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {self.photos[i].index(label) + 1}"
        return "No more free slots"

    def display(self):
        dash_row = f"{'-' * 11}\n"
        final_string = dash_row
        for page in self.photos:
            final_string += ' '.join(['[]' for _ in page]) + '\n'
            final_string += f'{dash_row}'
        return final_string.rstrip('\n')

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
