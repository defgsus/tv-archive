import { Component } from "component";


/** Little DOMElement creator */
export function E(tag, props, children) {
    //console.log(`E("${tag}", ${children})`);

    const elem = document.createElement(tag);
    if (props) {
        for (const key of Object.keys(props)) {
            const value = props[key]
            if (typeof value === "function") {
                elem.addEventListener(key, value);
            }
            else {
                elem.setAttribute(key, value);
            }
        }
    }
    _E_children(elem, children);
    return elem;
}

function _E_children(elem, children) {
    if (typeof children === "string") {
        elem.append(children);
    }
    else if (typeof children === "number") {
        elem.append(`${children}`);
    }
    else if (E.is_element(children)) {
        elem.appendChild(children);
    }
    else if (typeof children === "object") {
        for (const sub of Object.values(children)) {
            _E_children(elem, sub);
        }
    }
    else {
        console.log("unhandled children", children);
    }
}

E.is_element = function (x) {
    return (x && typeof x.addEventListener === "function");
}

E.hide_element = function (elem, hidden=true) {
    if (!hidden && elem.hasAttribute("hidden")) {
        elem.removeAttribute("hidden");
    } else if (hidden) {
        elem.setAttribute("hidden", "");
    }
}

E.replace_child_element = function (elem, child) {
    // TODO: this takes really long to delete all the elems
    elem.innerHTML = null;
    elem.appendChild(child);

}

export function to_slug(s) {
    return s.toLowerCase().replaceAll(/[\s\&\.]/g, "-")
}


