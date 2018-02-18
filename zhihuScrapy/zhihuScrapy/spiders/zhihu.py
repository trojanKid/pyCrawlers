# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json
from zhihuScrapy.items import UserItem


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&amp;' \
                  'offset={offset}&amp;limit={limit}'
    start_user = 'zhang-jia-wei'
    user_query = 'locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,' \
                 'following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,' \
                 'following_columns_count,answer_count,articles_count,pins_count,question_count,' \
                 'commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,' \
                 'marked_answers_text,message_thread_token,account_status,is_active,is_force_renamed,is_bind_sina,' \
                 'sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,' \
                 'mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,' \
                 'description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,' \
                 'org_homepage,badge[?(type=best_answerer)].topics'
    follows_query = 'url_token'
    search_depth = 2

    def __init__(self, *args, **kwargs):
        logger = logging.getLogger('scrapy.spidermiddlewares.httperror')
        logger.setLevel(logging.WARNING)
        super().__init__(*args, **kwargs)

    def start_requests(self):
        yield Request(self.user_url.format(user=self.start_user, include=self.user_query), self.parse_user,
                      meta={'depth': 0})

    def parse_user(self, response):
        # print(response.text)
        result = json.loads(response.text)
        items = UserItem()
        for field in items.fields:
            if field in result.keys():
                items[field] = result.get(field)
        yield items
        depth = response.meta['depth']
        print(depth)
        depth = depth + 1
        if depth <= self.search_depth:
            yield Request(
                self.follows_url.format(user=result.get('url_token'), include=self.follows_query, limit=20, offset=0),
                self.parse_follows,
                meta={'depth': depth})


    def parse_follows(self, response):
        results = json.loads(response.text)
        depth = response.meta['depth']

        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),
                              self.parse_user,
                              meta={'depth': depth})

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page,
                          self.parse_follows,
                          meta={'depth': depth})
