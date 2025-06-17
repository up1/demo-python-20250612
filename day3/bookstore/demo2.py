class ReportType1:
    def gen_header(self):
        pass
    def gen_body(self):
        pass
    def gen_footer(self):
        pass
    def generate_report(self):
        self.gen_header()
        self.gen_body()
        self.gen_footer()

class Report1(ReportType1):
    def gen_header(self):
        return "Header for Report 1"

    def gen_body(self):
        return "Body for Report 1"

    def gen_footer(self):
        return "Footer for Report 1"
    
class Report2(ReportType1):
    def gen_header(self):
        return "Header for Report 2"

    def gen_body(self):
        return "Body for Report 2"

    def gen_footer(self):
        return "Footer for Report 2"

r1 = Report2()
r1.generate_report()