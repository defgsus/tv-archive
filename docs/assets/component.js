export class Component {

    constructor(elem, onchange=null, debounce=0) {
        this.elem = elem;
        this.onchange = onchange;
        this.debounce = debounce;
        this._timeout = null;

        const handler = (e) => {
            if (!this.debounce) {
                this.emit();
            }
            else {
                if (this._timeout) {
                    clearTimeout(this._timeout);
                }
                this._timeout = setTimeout(this.emit, this.debounce);
            }
        }

        if (this.elem.tagName === "INPUT") {
            this.elem.onkeyup = handler;
        } else {
            this.elem.onchange = handler;
        }
    }

    get_value = () => {
        return this.elem.value;
    }

    set_value = (value, emit=false) => {
        this.elem.value = value;
        if (emit) {
            this.emit();
        }
    }

    emit = () => {
        if (this.onchange) {
            this.onchange(this.get_value());
        }
    }
}


export class ComponentMap {

    constructor(components, onchange=null) {
        this.components = components;
        this.onchange = onchange;

        for (const comp of Object.values(this.components)) {
            comp.onchange = () => {
                if (this.onchange) {
                    this.onchange(this.get_value());
                }
            }
        }
    }

    get_value = () => {
        const data = {};
        for (const key of Objects.keys(this.components)) {
            data[key] = this.components[key].get_value();
        }
        return data;
    }

    set_value = (values, emit=false) => {
        for (const key of Object.keys(values)) {
            this.components[key].set_value(values[key]);
        }
        if (emit && this.onchange) {
            this.onchange(this.get_value());
        }
    }
}
