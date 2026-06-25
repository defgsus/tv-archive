import { E, to_slug } from "element";
import { Component, ComponentMap } from "component";
import { load_program } from "program";


export const STATE = {
    date_map: null,
    date_list: [],
    program_map: {},
    program_id_map: {},
    comps: {
        year: new Component(document.querySelector("#select-year"), handle_date_select),
        month: new Component(document.querySelector("#select-month"), handle_date_select),
        day: new Component(document.querySelector("#select-day"), handle_date_select),
        channel: new Component(document.querySelector("#select-channel"), handle_channel_select),
        search: new Component(document.querySelector("#input-search"), handle_search_change, 300),
    },
    date: () => {
        const year = STATE.comps.year.get_value();
        const month = STATE.comps.month.get_value();
        const day = STATE.comps.day.get_value();
        return `${year}-${month}-${day}`;
    },
    channel: () => {
        return STATE.comps.channel.get_value();
    },
    program_items: (date) => {
        const index = STATE.date_list.indexOf(date);
        let items = [];
        if (index > 0) {
            items = [...STATE.program_map[STATE.date_list[index - 1]].filter(
                item => item.date.slice(0, 10) === date
            )];
        }
        if (index >= 0) {
            items = [...items, ...STATE.program_map[STATE.date_list[index]]];
        }
        return items;
    }
};

export function strip_zero(s) {
    if (s.startsWith("0"))
        return s.slice(1, s.length);
    return s;
}

export function display_error(message) {
    document.querySelector("#error").appendChild(
        E("div", {"class": "error"}, message)
    );
}

export function display_spinner(display=true) {
    for (const selector of ["#spinner", "#modal"]) {
        const elem = document.querySelector(selector);
        if (display) {
            elem.classList.add("visible");
        } else {
            elem.classList.remove("visible");
        }
    }
}

function handle_item_click(e) {
    const item_elem = e.currentTarget;
    const detail_elem = item_elem.querySelector(".item-detail");
    E.hide_element(detail_elem, !detail_elem.hasAttribute("hidden"));
}

export function render_program_items(items) {
    const channels = Array.from(new Set(items.map(item => item.channel)));
    channels.sort();

    return [channels, E("div", {"class": "program-channels"}, channels.map(channel => [
        E("div", {"class": "channel-column"}, [
            E("div", {"class": "channel", id: `channel-${to_slug(channel)}`}, channel),
            E("div", {"class": "program-items"},
                items.filter(item => item.channel === channel).map(item =>
                    E("div", {"class": "program-item", click: handle_item_click, "data-id": item.id}, [
                        E("div", {"class": "header"}, [
                            E("span", {"class": "time"}, item.date.replace("T", " ")),
                            " ",
                            //E("span", {"class": "length"}, item.length),
                            //" ",
                            E("span", {"class": "title"}, item.title),
                        ]),
                        E("div", {"class": "item-detail", hidden: ""}, Object.keys(item).map(key => {
                            let value = item[key];
                            if (value && typeof value === "object") {
                                value = Object.values(value).join(", ");
                            }
                            return E("div", {"class": "detail-item"}, [
                                E("b", null, `${key}:`), " ", `${value}`,
                            ]);
                        }))
                    ])
                )
            )
        ]),
    ]))];
}


export function handle_date_select() {
    let year = STATE.comps.year.get_value();
    if (!STATE.date_map[year]) {
        year = Object.keys(STATE.date_map)[STATE.date_map.length - 1];
        STATE.comps.year.set_value(year);
    }
    let month = STATE.comps.month.get_value();
    if (!STATE.date_map[year][month]) {
        month = Object.keys(STATE.date_map[year])[STATE.date_map[year].length - 1];
        STATE.comps.month.set_value(month);
    }
    let day = STATE.comps.day.get_value();;
    if (STATE.date_map[year][month].indexOf(day) < 0) {
        day = STATE.date_map[year][month][STATE.date_map[year][month].length - 1];
        STATE.comps.day.set_value(day);
    }

    for (const elem of STATE.comps.month.elem.querySelectorAll("option")) {
        E.hide_element(elem, elem.getAttribute("data-year") !== year);
    }
    for (const elem of STATE.comps.day.elem.querySelectorAll("option")) {
        E.hide_element(elem, !(elem.getAttribute("data-year") === year && elem.getAttribute("data-month") === month));
    }

    return load_program(STATE.date());
}

export function handle_channel_select() {

}

export function handle_search_change() {
    let expr = STATE.comps.search.get_value();
    if (expr) {
        expr = new RegExp(expr, "i");
    }
    for (const elem of document.querySelectorAll(".program-item")) {
        let hidden = !!expr;
        if (expr) {
            const item = STATE.program_id_map[elem.getAttribute("data-id")];
            for (const key of ["url", "title", "sub_title", "description"]) {
                if (item[key] && item[key].match(expr)) {
                    hidden = false;
                }
            }
        }
        E.hide_element(elem, hidden);
    }
}
