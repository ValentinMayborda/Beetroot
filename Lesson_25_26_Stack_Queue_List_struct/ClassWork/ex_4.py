class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.next = None
        self.prev = None

    def __str__(self):
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{self.title} by {self.artist} ({minutes}:{seconds:02d})"


class MusicPlaylist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0

    def add_song(self, title, artist, duration):
        new_song = Song(title, artist, duration)
        self.size += 1
        if not self.head:
            self.head = new_song
            self.tail = new_song
            self.current = new_song
        else:
            new_song.prev = self.tail
            self.tail.next = new_song
            self.tail = new_song
        print(f"Додано нову післю: {new_song}")

    def remove_song(self, title):
        current = self.head
        while current:
            if current.title == title:
                self.size -= 1
                # Якщо це поточна пісня, переключаємось на наступну
                if current == self.current:
                    self.play_next()
                    # Оновляємо посилання
                if current.prev:
                    current.prev.next = current.next
                else:  # Якщо це перша пісня
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:  # Якщо це остання пісня
                    self.tail = current.prev
                print(f'\nВидалено пісню: {current}')
                return
            current = current.next
        print(f'Пісня {title} не знайдена')

    def play_next(self):
        if not self.current:
            print("Плейлист порожній")
            return
        if self.current.next:
            self.current = self.current.next
            print(f"Відтворюється пісня: {self.current}")
        else:
            print("Це остання пісня у плейлисті")

    def play_previous(self):
        if not self.current:
            print("Плейлист порожній")
            return
        if self.current.prev:
            self.current = self.current.prev
            print(f"Відтворюється пісня: {self.current}")
        else:
            print("Це перша пісня у плейлисті")

    def show_playlist(self):
        if not self.head:
            print("Плейлист порожній")
            return
        print(f'Плейлист (всього {self.size} пісень):')
        current = self.head
        index = 1
        while current:
            status = ">" if current == self.current else " "
            print(f"{status} {index}. {current}")
            current = current.next
            index += 1

if __name__ == "__main__":
    playlist = MusicPlaylist()
    playlist.add_song("Du hust", "Rammstein", 300)
    playlist.add_song("It's my life", "Bon Jovi", 250)
    playlist.add_song("Time", "E-type", 255)
    playlist.add_song("Друга ночі", "Христина Соловій", 255)
    playlist.show_playlist()
    print('Переключаємо на наступну пісню')
    playlist.play_next()
    playlist.show_playlist()
    playlist.remove_song("Time")
    playlist.show_playlist()
    playlist.play_previous()
    playlist.show_playlist()
