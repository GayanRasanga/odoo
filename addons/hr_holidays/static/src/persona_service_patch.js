/* @odoo-module */

import { personaService, PersonaService } from "@mail/core/common/persona_service";
import { deserializeDateTime } from "@web/core/l10n/dates";
import { _t } from "@web/core/l10n/translation";
import { patch } from "@web/core/utils/patch";
import { sprintf } from "@web/core/utils/strings";

const { DateTime } = luxon;

patch(personaService, "hr_holidays", {
    dependencies: [...new Set([...personaService.dependencies, "user"])],
});

patch(PersonaService.prototype, "hr_holidays", {
    setup(env, services) {
        this._super(env, services);
        this.userService = services.user;
    },

    outOfOfficeText(persona) {
        if (!persona.out_of_office_date_end) {
            return "";
        }
        const currentDate = new Date();
        const date = deserializeDateTime(persona.out_of_office_date_end);
        // const options = { day: "numeric", month: "short" };
        if (currentDate.getFullYear() !== date.year) {
            // options.year = "numeric";
        }
        let localeCode = this.userService.lang.replace(/_/g, "-");
        if (localeCode === "sr@latin") {
            localeCode = "sr-Latn-RS";
        }
        // const fdate = date.toLocaleString(DateTime.TIME_SHORT);
        const fdate = date.toLocaleString(DateTime.DATE_MED);
        // const formattedDate = date.toLocaleDateString(localeCode, options);
        return sprintf(_t("Out of office until %s"), fdate);
    },
});
