odoo.define("procrm_custom_ui_discussion/static/src/models/discuss_group_chat.js", function (require) {
    const {registerFieldPatchModel} = require("mail/static/src/model/model_core.js");
    const {attr} = require("mail/static/src/model/model_field.js");

    registerFieldPatchModel("mail.discuss", "procrm_custom_ui_discussion/static/src/models/discuss_group_chat.js", {
        isHideGroupChat: attr({
            default: false,
        }),
    });
});
