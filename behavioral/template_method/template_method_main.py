from behavioral.template_method.logic import LocalFileProcessor, WebFileProcessor

LOCAL_FILE_PATH = "data/behavioral_patterns.txt"
WEB_FILE_PATH = "https://raw.githubusercontent.com/Kozak24/Patterns/main/behavioral/template_method/" \
                "data/behavioral_patterns.txt"


def main() -> None:
    local_file_processor = LocalFileProcessor(LOCAL_FILE_PATH)
    local_file_processor.process()
    local_file_processor.print_content()

    web_file_processor = WebFileProcessor(WEB_FILE_PATH)
    web_file_processor.process()
    web_file_processor.print_content()


if __name__ == "__main__":
    main()
