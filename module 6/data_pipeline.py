from abc import ABC, abstractmethod
from typing import Any, Protocol


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
        return self.processor.pop(0)


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
            print("Got Exception: Improper text data")
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
            print("Got Exception: Improper log data")
            return
        if not isinstance(data, list):
            data = [data]

        for i in data:
            level = i.get("log_level", "UNKNOWN")
            message = i.get("log_message", "")
            self.processor.append((self.signature, f"{level}: {message}"))
            self.signature += 1
            self.processed += 1


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass

class DataStream:
    def __init__(self):
        self.processors = []

    def register_processor(self, proc: DataProcessor) -> None:
        if not isinstance(proc, DataProcessor):
            print("No processor found, no data\n")
            return
        if proc not in self.processors:
            self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            data = []
            for _ in range(nb):
                if len(proc.processor) == 0:
                    break
                data.append(proc.output())
            if data:
                plugin.process_output(data)

class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = []
        for number, text in data:
            value = text.replace('"', '""')
            if "," in text or '"' in text or "\n" in text or "\r" in text:
                value ='"' + value + '"'
            values.append(value)
        print("CSV Output:")
        print(",".join(values))


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = []
        for number, text in data:
            text = text.replace("\\", "\\\\")
            text = text.replace('"', '\\"')
            text = text.replace("\n", "\\n")
            text = text.replace("\r", "\\r")
            text = text.replace("\t", "\\t")
            values.append(f'"item_{number}": "{text}"')
        print("JSON Output:")
        print("{" + ", ".join(values) + "}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...\n")
    print("== DataStream ==")
    data_stream = DataStream()
    data_stream.register_processor("InvalidProcessor")
    data_1 = ['Hello world', [3.14, -1, 2.71],
              [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'},
               {'log_level': 'INFO', 'log_message': 'User wil isconnected'}], 42, ['Hi', 'five']]
    print("Registering Processors")
    data_stream.register_processor(NumericProcessor())
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())
    print(f"Send first batch of data on stream: {data_1}")
    data_stream.process_stream(data_1)
    data_stream.print_processors_stats()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    data_stream.output_pipeline(3, CSVPlugin())
    data_stream.print_processors_stats()
    data_2 =  [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'], [{'log_level': 'ERROR', 'log_message': '500 server crash'}, {'log_level': 'NOTICE', 'log_message': 'Certificate expires in 10 days'}], [32, 42, 64, 84, 128, 168], 'World hello']
    print(f"\n Send another batch of data: {data_2}\n")
    data_stream.process_stream(data_2)
    data_stream.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    data_stream.output_pipeline(5, JSONPlugin())
    data_stream.print_processors_stats()
