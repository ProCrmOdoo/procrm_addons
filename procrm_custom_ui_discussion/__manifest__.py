{
    "name": "Custom UI discussion",
    "license": "LGPL-3",
    "version": "14.0.1.0.0",
    "author": "YevdokimovA",
    "application": "True",
    "depends": ["base", "web", "mail", "im_livechat", "multi_livechat"],
    "data": ["views/include.xml"],
    "qweb": [
        "static/src/xml/discussion_sidebar.xml",
        "static/src/xml/discuss_group_chat.xml",
        "static/src/xml/discuss_multi_livechat.xml",
    ],
    "installable": True,
}
