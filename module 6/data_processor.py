from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):

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
            return
        self.processor.append((self.signature, str(data)))
        self.signature += 1


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
                self.signature += 1
            return
        self.processor.append((self.signature, data))
        self.signature += 1


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
            return
        self.processor.append((self.signature, data))
        self.signature += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    print("\nTesting Numeric Processor...")
    NumProc = NumericProcessor()
    numdata = [1, 2, 3, 4, 5]
    textdata = ["Hello", "Nexus", "World"]
    logdata = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'}, {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    TextProc = TextProcessor()
    LogProc = LogProcessor()
    print(f"Trying to validate input '42': {NumProc.validate(42)}")
    print(f"Test invalid ingestion of string 'foo' without prior validation:")
    NumProc.ingest("foo")
    print("Processing data: [1, 2, 3, 4, 5]")
    NumProc.ingest(numdata)
    print("Extracting 3 values...")
    for _ in range(3):
        info = NumProc.output()
        print(f"Numeric value {info[0]}: {info[1]}")
    print("\n Testing Text Processor...")
    print(f"Trying to validate input '42': {TextProc.validate(42)}")
    print(f"Processing data: {textdata}")
    TextProc.ingest(textdata)
    print("extracting 1 value...")
    text_info = TextProc.output()
    print(f"Text value {text_info[0]}: {text_info[1]}\n")
    print("Testing Log Processor...")
    print(f"Trying to validate input 'Hello': {LogProc.validate('Hello')}")
    print(f"Processing data: {logdata}")
    LogProc.ingest(logdata)
    print("Extracting 2 values...")
    for _ in range(2):
        log_info = LogProc.output()
        print(f"Log entry {log_info[0]}: {log_info[1]}")
