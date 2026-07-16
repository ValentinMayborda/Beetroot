class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def add_worker(self, worker):
        self.workers.append(worker)

    def __str__(self):
        return f'{self.name}'


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    def __str__(self):
        return f'Код працівника - {self.id}, Ім"я працівника -  {self.name}, Назва компанії - {self.company}, Бос - {self.boss}'

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, value):
        if not isinstance(value, Boss):
            raise ValueError("Boss має бути екземпляром класу Boss")

        self._boss = value
        if self not in value.workers:
            value.add_worker(self)


boss = Boss(1, "Директор", "Cisco")
boss1 = Boss(4, "Головний бухгалтер", "Cisco")

w1 = Worker(2, "Валентин", "Cisco", boss)
w2 = Worker(3, "Вадим", "Cisco", boss)
w3 = Worker(5, 'Світлана', "Cisco", boss1)

print(len(boss.workers))
print(w1)
print(w2)
print(len(boss1.workers))
print(w3)
