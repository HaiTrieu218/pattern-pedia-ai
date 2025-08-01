# file: src/guru_scraper/spiders/patterns_spider.py

import scrapy
import re

class PatternsSpider(scrapy.Spider):
    name = "patterns"
    start_urls = ["https://refactoring.guru/design-patterns/catalog"]

    def _clean_list(self, items):
        if not items: return []
        return [re.sub(r'\s+', ' ', item).strip() for item in items if re.sub(r'\s+', ' ', item).strip()]

    def _clean_text(self, text_or_list):
        if not text_or_list: return ""
        if isinstance(text_or_list, list):
            return ' '.join(self._clean_list(text_or_list))
        return re.sub(r'\s+', ' ', text_or_list).strip()

    def parse(self, response):
        """
        Xử lý trang Catalog: Lấy Category và các link thuộc về nó.
        """
        # Tìm các tiêu đề h3 của category
        category_headers = response.css('div.patterns-catalog > div[class*="-header"] h3')
        
        for header in category_headers:
            category_name = self._clean_text(header.css('::text').get())
            
            # Tìm khối div chứa các card pattern ngay sau header đó
            pattern_block = header.xpath('ancestor::div[1]/following-sibling::div[1]')
            
            pattern_links = pattern_block.css('a.pattern-card::attr(href)').getall()
            self.log(f'Tìm thấy {len(pattern_links)} pattern trong category: {category_name}')
            
            for link in pattern_links:
                yield response.follow(
                    link, 
                    callback=self.parse_pattern_detail,
                    cb_kwargs={'category': category_name}
                )

    def parse_pattern_detail(self, response, category):
        """
        Xử lý trang chi tiết với bộ selector đầy đủ và chính xác nhất.
        """
        name = self._clean_text(response.css('h1.title::text').get())
        intent = self._clean_text(response.css('div.section.intent ::text').getall())
        problem = self._clean_text(response.css('div.section.problem ::text').getall())
        solution = self._clean_text(response.css('div.section.solution ::text').getall())
        structure_text = self._clean_text(response.css('div.structure-container div.structure ::text').getall())
        pseudocode_text = self._clean_text(response.css('div.section.pseudocode ::text').getall())
        
        # Selector đã được xác thực cho ảnh UML
        uml_image_url = response.css('div.section.structure-container div.structure img::attr(src)').get()
        
        applicability_items = response.css('div.applicability-container div.applicability ::text').getall()
        applicability = self._clean_text(applicability_items)

        how_to_implement_items = response.css('div.section.checklist ol li ::text').getall()
        how_to_implement = self._clean_list(how_to_implement_items)
        
        pros_items = response.css('div.section.pros-cons .row > div:nth-child(1) ul li ::text').getall()
        pros = self._clean_list(pros_items)
        
        cons_items = response.css('div.section.pros-cons .row > div:nth-child(2) ul li ::text').getall()
        cons = self._clean_list(cons_items)
        
        relations_items = response.css('div.section.relations ul li ::text').getall()
        relations = self._clean_list(relations_items)

        extra_content_items = response.css('div.section.extras ul li ::text').getall()
        extra_content = self._clean_list(extra_content_items)
        
        yield {
            'name': name,
            'url': response.url,
            'category': category,
            'intent': intent,
            'problem': problem,
            'solution': solution,
            'structure_text': structure_text,
            'pseudocode': pseudocode_text,
            'uml_image_url': response.urljoin(uml_image_url) if uml_image_url else None,
            'applicability': applicability,
            'how_to_implement': how_to_implement,
            'extra_content': extra_content,
            'pros': pros,
            'cons': cons,
            'relations': relations,
        }