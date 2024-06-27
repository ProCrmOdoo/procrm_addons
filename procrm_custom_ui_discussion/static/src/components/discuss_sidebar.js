odoo.define("procrm_custom_ui_discussion/static/src/components/discuss_sidebar.js", function (require) {
    const {patch} = require("web.utils");
    var pos_models = require("mail/static/src/components/discuss_sidebar/discuss_sidebar.js");

    // Добавляет новую функцию к компоненету discuss_sidebar.js
    // odoo/addons/mail/static/src/components/discuss_sidebar/discuss_sidebar.js
    patch(pos_models, "procrm_custom_ui_discussion/static/src/components/discuss_sidebar.js", {
        _triggerDiscussSidebarList(ev) {
            ev.stopPropagation();
            if (this.discuss.isHideSidebarList) {
                this.discuss.update({isHideSidebarList: false});
            } else {
                this.discuss.update({isHideSidebarList: true});
            }
            console.log(this.discuss.isHideSidebarList);
        },
    });
});
