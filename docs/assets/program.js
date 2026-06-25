import { E } from "element";
import {
    STATE, display_error, display_spinner, render_program_items,
    handle_search_change
} from "ui";

export const DATA_HOST = (
        window.location.host.startsWith("127.0.0.1") || window.location.host.startsWith("localhost")
    )
    ? "http://localhost:8001"
    : "https://github.com/defgsus/tv-archive/raw/refs/heads/master/data";


/** fetch program of a single date, store items in STATE.program_map */
export function fetch_program(date) {
    console.log("fetch program", date);

    let [year, month, day] = date.split("-");

    return fetch(`${DATA_HOST}/${year}/${month}/${year}-${month}-${day}.ndjson`)
        .then(response => {
            if (response.status >= 400) throw `${response.url}: status ${response.status}`;
            return response;
        })
        .then(response => response.text())
        .then(response => {
            const items = [];
            for (const line of response.split("\n")) {
                if (line) items.push(JSON.parse(line));
            }
            items.sort((a, b) => a.title.localeCompare(b.title))
            items.sort((a, b) => a.date.localeCompare(b.date))
            STATE.program_map[date] = items;
            for (const item of items) {
                STATE.program_id_map[item.id] = item;
            }
            return items;
        });
}

/** load program and render to screen */
export function load_program(date) {
    const index = STATE.date_list.indexOf(date);
    if (index < 0) {
        display_error(`Date ${date} out of range`); return;
    }

    let promise = new Promise((resolve) => {
        display_spinner(true);
        resolve();
    });
    if (!STATE.program_map[date]) {
        promise = promise.then(() => fetch_program(date));
    }
    if (index > 1 && !STATE.program_map[STATE.date_list[index - 1 ]]) {
        promise = promise.then(() => fetch_program(STATE.date_list[index - 1]));
    }
    return promise.then(() => {
        const items = STATE.program_items(date);
        const [channels, elem] = render_program_items(items);

        const sel_elem = STATE.comps.channel.elem;
        document.querySelector('label[for="select-channel"]').textContent = `channel (${channels.length})`;
        sel_elem.innerHTML = "";
        sel_elem.appendChild(
            E("option", {value: "_all_"}, "all channels")
        );
        for (const channel of channels) {
            sel_elem.appendChild(
                E("option", {value: channel}, channel)
            );
        };

        E.replace_child_element(document.querySelector("#program"), elem);
        handle_search_change();
    })
    .catch(error => display_error(error.toString()))
    .finally(() => { display_spinner(false); });
}
