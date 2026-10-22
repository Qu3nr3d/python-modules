from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):
    def __init__(self):
        self.processed = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        try:
            tup = self.processor[0]
            self.processor.pop(0)
            return (tup)
        except IndexError as e:
            print(f"{e}")
            


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self.processor = []
        self.signature = 1

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for i in data:
                if not (isinstance(i, int) or isinstance(i, float)):
                    return False
            return True
        return (isinstance(data, int) or isinstance(data, float))

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            print("Got Exception: Improper numeric data")
            return
        if isinstance(data, list):
            for i in data:
                self.processor.append((self.signature, str(i)))
                self.signature += 1
                self.processed += 1
            return
        self.processor.append((self.signature, str(data)))
        self.signature += 1
        self.processed += 1


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self.processor = []
        self.signature = 1

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for i in data:
                if not isinstance(i, str):
                    return False
            return True
        return (isinstance(data, str))

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            print("Got Exception: Improper numeric data")
            return
        if isinstance(data, list):
            for i in data:
                self.processor.append((self.signature, i))
                self.processed += 1
                self.signature += 1
            return
        self.processor.append((self.signature, data))
        self.signature += 1
        self.processed += 1


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self.processor = []
        self.signature = 1

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for i in data:
                if not isinstance(i, dict):
                    return False
            return True
        return isinstance(data, dict)

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            print("Got Exception: Improper numeric data")
            return
        if isinstance(data, list):
            for i in data:
                self.processor.append((self.signature, i))
                self.signature += 1
                self.processed += 1
            return
        self.processor.append((self.signature, data))
        self.signature += 1
        self.processed += 1


class DataStream(NumericProcessor, TextProcessor, LogProcessor):
    def __init__(self):
        super().__init__()
        self.processors = []

    def register_processor(self, proc: DataProcessor) -> None:
            if not isinstance(proc, DataProcessor):
                print("No processor found, no data\n")
                return
            if proc not in self.processors:
                self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        self.register_processor
        for data in stream:
            handled = False
            for proc in self.processors:
                if proc.validate(data):
                    proc.ingest(data)
                    handled = True
                    break
            if handled is False:
                print(f"Data Stream error - Can't process element in stream: {data}")

    def print_processors_stats(self) -> None:
        print("=== DataStream statistics ===")
        for proc in self.processors:
            remaining = len(proc.processor)
            print(
                f"{type(proc).__name__}: "
                f"total {proc.processed} items processed, "
                f"remaining {remaining} on processor"
            )
                

if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    print("== DataStream ==")
    data_stream = DataStream()
    data_stream.register_processor("Dupa")
    data_1 = ['Hello world', [3.14, -1, 2.71], [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, {'log_level': 'INFO', 'log_message': 'User wil isconnected'}], 42, ['Hi', 'five']]
    print("Registering Numeric Processor")
    data_stream.register_processor(NumericProcessor())
    print(f"Send first batch of data on stream: {data_1}")
    data_stream.process_stream(data_1)
    data_stream.print_processors_stats()
    print("Registering other data processors")
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())
    print("Send the same batch again")
    data_stream.process_stream(data_1)
    data_stream.print_processors_stats()
    print("Consume some elements from the data processors: Numeric 3, Text 2, Log 1")
    for i in range(3):
        if i < 1:
            x = data_stream.processors[2].output()
        if i < 2:
            x = data_stream.processors[1].output()
        if i < 3:
            x = data_stream.processors[0].output()
    data_stream.print_processors_stats()






