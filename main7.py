class Record():

    def __init__(self, i: int,order_id: int) -> None:
        self.i = i
        self.order_id = order_id

class Log():

    def __init__(self) -> None:
        self.i: int = 0
        self.records: Record

    def record(self, order_id: int) -> None:
        self.i += 1
        self.records = Record(i=self.i, order_id=order_id)

    def get_last(self, i: int) -> int | None:
        if i == self.records.i:
            return self.records.order_id
        return None
    
log = Log()

log.record(1)

print(log.get_last(1))
    