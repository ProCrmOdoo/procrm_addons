odoo.define("procrm_custom_ui_discussion/static/src/components/discuss_group_chat.js", function (require) {
    const {patch} = require("web.utils");
    var pos_models = require("mail/static/src/components/discuss_sidebar/discuss_sidebar.js");
    patch(pos_models, "procrm_custom_ui_discussion/static/src/components/discuss_group_chat.js", {
        _triggerDiscussGroupChat(ev) {
            ev.stopPropagation();
            if (this.discuss.isHideGroupChat) {
                this.discuss.update({isHideGroupChat: false});
            } else {
                this.discuss.update({isHideGroupChat: true});
            }
            console.log(this.discuss.isHideGroupChat);
        },
    });
});
