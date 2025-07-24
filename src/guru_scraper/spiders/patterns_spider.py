import scrapy

class PatternsSpider(scrapy.Spider):
    """
    Spider này chịu trách nhiệm crawl dữ liệu từ trang Refactoring.Guru.
    Bước đầu tiên: Chỉ crawl trang catalog và lưu lại HTML để kiểm tra.
    """
    # Tên định danh của spider, dùng để chạy từ command line.
    name = "patterns"

    # Danh sách các URL mà spider sẽ bắt đầu crawl.
    start_urls = [
        "https://refactoring.guru/design-patterns/catalog"
    ]

    # Phương thức mặc định được gọi để xử lý response từ start_urls.
    def parse(self, response):
        # Lấy tất cả các link đến từng pattern
        pattern_links = response.css('a.pattern-card::attr(href)').getall()
        self.log(f'Tìm thấy {len(pattern_links)} card pattern trên trang {response.url}')

        for link in pattern_links:
            # Đi vào từng link và gọi hàm parse_pattern
            yield response.follow(link, callback=self.parse_pattern)

    def parse_pattern(self, response):
        # Trích xuất tên pattern
        pattern_name = response.css('h1.title::text').get()

        # Trích xuất và nối lại các đoạn mô tả vấn đề
        problem_paragraphs = response.css('h2#problem ~ p::text').getall()
        problem_description = ' '.join(problem_paragraphs)

        # Trích xuất và nối lại các đoạn mô tả giải pháp
        solution_paragraphs = response.css('h2#solution ~ p::text').getall()
        solution_description = ' '.join(solution_paragraphs)

        # Trích xuất URL của ảnh UML, dùng urljoin để có link tuyệt đối
        uml_image_url = response.urljoin(response.css('div.image a::attr(href)').get())

        
        # Xử lý các ví dụ code
        code_examples = []
        for code_block in response.css('pre.code'):
            language =code_block.attrib.get('id', 'unknown')
            code = ''.join(code_block.css('pre ::text').getall())
            
            code_examples.append({
                'language': language,
                'code': code.strip()
            })
        yield {
            'name': pattern_name.strip() if pattern_name else None,
            'url': response.url,
            'problem': problem_description.strip(),
            'solution': solution_description.strip(),
            'uml_image_url': uml_image_url,
            'code_examples': code_examples
        }