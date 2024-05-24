odoo.define("procrm_custom_ui_discussion/static/src/components/discuss_multi_livechat.js", function (require) {
    const {patch} = require("web.utils");
    var pos_models = require("mail/static/src/components/discuss_sidebar/discuss_sidebar.js");
    patch(pos_models, "procrm_custom_ui_discussion/static/src/components/discuss_multi_livechat.js", {
        _triggerDiscussSidebarGroupLiveChat(ev) {
            ev.stopPropagation();
            const $sidebarList = $(ev.target).parent().parent().find(".o_DiscussSidebar_list");
            const isVisible = $sidebarList.is(":visible");

            if (isVisible) {
                $sidebarList.hide();
            } else {
                $sidebarList.show();
            }
        },
    });
});
