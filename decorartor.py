def border(func):
    def display(*args, **kwargs):
        print("=" * 30)
        func(*args, **kwargs)
        print("=" * 30)
    return display

class Report:
    report_type = "General Report"

    def __init__(self, title, description):
        self.title = title
        self.description = description

    @classmethod
    def set_report_type(cls, new_type):
        cls.report_type = new_type

    def __str__(self):
        return (
            "Report Type : " + self.report_type +
            "\nTitle : " + self.title +
            "\nDescription : " + self.description
        )

    @border
    def display_report(self):
        print(self)


Report.set_report_type("College Report")

r1 = Report("Python Project", "This project explains decorators and classes.")

r1.display_report()