import { E } from "element";
import { Component, ComponentMap } from "component";
import {
    STATE, display_error, display_spinner, render_program_items, strip_zero,
    handle_date_select, handle_search_change
} from "ui";


function handle_index_file(data) {
    const select_year = STATE.comps.year.elem;
    const select_month = STATE.comps.month.elem;
    const select_day = STATE.comps.day.elem;
    STATE.date_map = data.date_map;
    const years = Object.keys(STATE.date_map);
    years.sort();
    for (const year of years) {
        select_year.appendChild(E("option", {value: year}, year));
        const months = Object.keys(STATE.date_map[year]);
        months.sort();
        for (const month of months) {
            select_month.appendChild(E("option", {value: month, "data-year": year}, strip_zero(month)));
            const days = STATE.date_map[year][month];
            days.sort();
            for (const day of days) {
                select_day.appendChild(E("option", {value: day, "data-year": year, "data-month": month}, strip_zero(day)));
                STATE.date_list.push(`${year}-${month}-${day}`);
            }
        }
    }
    return handle_date_select();
}


document.addEventListener("DOMContentLoaded", function () {
    fetch("./data/index.json")
        .then(response => response.json())
        .then(handle_index_file)
        .catch(error => display_error(error.toString()))
    ;
});

