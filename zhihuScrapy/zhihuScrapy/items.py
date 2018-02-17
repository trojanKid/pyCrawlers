# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    locations = scrapy.Field()
    employments = scrapy.Field()
    gender = scrapy.Field()
    educations = scrapy.Field()
    business = scrapy.Field()
    voteup_count = scrapy.Field()
    thanked_Count = scrapy.Field()
    follower_count = scrapy.Field()
    following_count = scrapy.Field()
    cover_url = scrapy.Field()
    following_topic_count = scrapy.Field()
    following_question_count = scrapy.Field()
    following_favlists_count = scrapy.Field()
    following_columns_count = scrapy.Field()
    avatar_hue = scrapy.Field()
    answer_count = scrapy.Field()
    articles_count = scrapy.Field()
    pins_count = scrapy.Field()
    question_count = scrapy.Field()
    columns_count = scrapy.Field()
    commercial_question_count = scrapy.Field()
    favorite_count = scrapy.Field()
    favorited_count = scrapy.Field()
    logs_count = scrapy.Field()
    included_answers_count = scrapy.Field()
    included_articles_count = scrapy.Field()
    included_text = scrapy.Field()
    message_thread_token = scrapy.Field()
    account_status = scrapy.Field()
    is_active = scrapy.Field()
    is_bind_phone = scrapy.Field()
    is_force_renamed = scrapy.Field()
    is_privacy_protected = scrapy.Field()
    is_blocking = scrapy.Field()
    is_blocked = scrapy.Field()
    is_following = scrapy.Field()
    is_followed = scrapy.Field()
    is_org_createpin_white_user = scrapy.Field()
    mutual_followees_count = scrapy.Field()
    vote_to_count = scrapy.Field()
    vote_from_count = scrapy.Field()
    thank_to_count = scrapy.Field()
    thank_from_count = scrapy.Field()
    thanked_count = scrapy.Field()
    description = scrapy.Field()
    hosted_live_count = scrapy.Field()
    participated_live_count = scrapy.Field()
    allow_message = scrapy.Field()
    industry_category = scrapy.Field()
    org_name = scrapy.Field()
    org_homepage = scrapy.Field()
