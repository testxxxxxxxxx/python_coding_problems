class Log():

    def __init__(self) -> None:
        self.i: int = 0
        self.order_id: int
        self.records: list = []
        self.N: int

    def countOfRecords(self) -> int:
        return len(self.records)

    def record(self, order_id: int) -> None:
        self.records.append(order_id)

    def get_last(self, i: int) -> int | None:
        self.N = self.countOfRecords()
        
        if i <= self.N:
            return self.records[i - 1]

log = Log()

log.record(1)
log.record(2)
log.record(3)
print(log.get_last(1))
print(log.get_last(2))
print(log.get_last(3))