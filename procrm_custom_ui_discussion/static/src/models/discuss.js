odoo.define("procrm_custom_ui_discussion/static/src/models/discuss.js", function (require) {
    const {registerFieldPatchModel} = require("mail/static/src/model/model_core.js");
    const {attr} = require("mail/static/src/model/model_field.js");

    // Добавляет новый аттрибут к моделе mail.discuss
    // odoo/addons/mail/static/src/models/discuss/discuss.js
    registerFieldPatchModel("mail.discuss", "procrm_custom_ui_discussion/static/src/models/discuss.js", {
        isHideSidebarList: attr({
            default: false,
        }),
    });
});
